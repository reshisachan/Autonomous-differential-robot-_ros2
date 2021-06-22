import serial
import time
import math
import numpy as np

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

ser = serial.Serial('/dev/ttyS4', 115200, timeout=0.01)
serialString = ""                           # Used to hold data coming over UART

encoder1 = ""
encoder2 = ""
curr_encoder1 = 0
curr_encoder2 = 0
prev_encoder1 = 0
prev_encoder2 = 0
curr_time = 0.0
millis = 0.0
first_init = 0

#euler to quaternion
def quaternion_from_euler(roll, pitch, yaw):
    """
    Converts euler roll, pitch, yaw to quaternion (w in last place)
    quat = [x, y, z, w]
    Bellow should be replaced when porting for ROS 2 Python tf_conversions is done.
    """
    cy = math.cos(yaw * 0.5)
    sy = math.sin(yaw * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)
    cr = math.cos(roll * 0.5)
    sr = math.sin(roll * 0.5)
    #yaw-heading pitch-attitude roll-bank
    q = [0] * 4
    q[0] = sy * sp * cr + cy * cp * sr
    q[1] = sy * cp * cr + cy * sp * sr
    q[2] = cy * sp * cr - sy * cp * sr
    q[3] = cy * cp * cr - sy * sp * sr

    return q

#odom parameters
theta = 0.0
th = 0.0
vx = 0.0
vy = 0.0
vth = 0.0
x = 0.0
y = 0.0

#Bot parameters
radius = 0.1
base_length = 0.35

left_wheel_encoder_count = ""
right_wheel_encoder_count = ""

#ROS2 node initialization
rclpy.init(args=None)
node = rclpy.create_node('odom_replicate')
publisher = node.create_publisher(Odometry, 'odom_temp', 10)

while rclpy.ok():
    millis = time.time()
    ser.write(b"?C 1\r")
    left_wheel_encoder_count=ser.readline(100)
    # print(left_wheel_encoder_count)

    ser.write(b"?C 2\r")
    right_wheel_encoder_count=ser.readline(100)
    # print(right_wheel_encoder_count)
    
    encoder1_start = 0
    encoder2_start = 0
    encoder1 = ""
    encoder2 = ""
    left_wheel_encoder_count = str(left_wheel_encoder_count)
    right_wheel_encoder_count = str(right_wheel_encoder_count)

    for i in left_wheel_encoder_count:
        if(i == "="):
            encoder1_start = 1
            continue
        if(encoder1_start == 1):
            encoder1 += i
    encoder1 = encoder1[:-3]

    for i in right_wheel_encoder_count:
        if(i == "="):
            encoder2_start = 1
            continue
        if(encoder2_start == 1):
            encoder2 += i
    encoder2 = encoder2[:-3]
    
    curr_encoder1 = int(encoder1)
    curr_encoder2 = int(encoder2)

    if(first_init == 0):
        prev_encoder1 = curr_encoder1
        prev_encoder2 = curr_encoder2
        curr_time = millis
        first_init = 1

    difference1 = curr_encoder1 - prev_encoder1
    difference2 = curr_encoder2 - prev_encoder2

    prev_encoder1 = curr_encoder1
    prev_encoder2 = curr_encoder2

    curr_time = millis - curr_time
    try:
        rpm1 = (float(difference1)*60/4096/curr_time)
        rpm2 = (float(difference2)*60/4096/curr_time)
    except:
        rpm1 = 0
        rpm2 = 0
    disp1 = (float(difference1)/4096*2*math.pi*radius)
    disp2 = (float(difference2)/4096*2*math.pi*radius)

    th = (disp2 - disp1)/base_length
    try:
        vx += (((disp1 + disp2) / 2)/curr_time)
        vth += (th/curr_time)
    except:
        vx = 0.0
        vth = 0.0
    theta += th
    x += (((disp1 + disp2)/2) * math.cos(theta))
    y += (((disp1 + disp2)/2) * math.sin(theta))

    curr_time = millis

    #######ROS2 node#######
    q = quaternion_from_euler(0.0, 0.0, theta)
    odom_temp_msg = Odometry()
    odom_temp_msg.header.frame_id = "odom1"
    odom_temp_msg.pose.pose.position.x = x
    odom_temp_msg.pose.pose.position.y = y
    # print(theta)
    # print(q)
    odom_temp_msg.pose.pose.orientation.z = q[1]
    odom_temp_msg.pose.pose.orientation.w = q[3]

    odom_temp_msg.twist.twist.linear.x = vx
    odom_temp_msg.twist.twist.linear.y = 0.0
    odom_temp_msg.twist.twist.angular.z = vth

    publisher.publish(odom_temp_msg)

node.destroy_node()
rclpy.shutdown()