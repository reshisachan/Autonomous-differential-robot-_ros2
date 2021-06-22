import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

import time
import math

import tf2_ros
import tf2_msgs.msg
import geometry_msgs.msg

global odom_x, odom_y, odom_w, odom_z
odom_x = 0.0; odom_y = 0.0; odom_w = 1.0; odom_z = 0.0

rclpy.init(args=None)
node = rclpy.create_node('odom_publish')
publisher_odom = node.create_publisher(Odometry, 'odom', 10)
publisher_tf = node.create_publisher(tf2_msgs.msg.TFMessage, '/tf', 10)

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

    q = [0] * 4
    q[0] = cy * cp * cr + sy * sp * sr
    q[1] = cy * cp * sr - sy * sp * cr
    q[2] = sy * cp * sr + cy * sp * cr
    q[3] = sy * cp * cr - cy * sp * sr

    return q


def callback(data):
    global odom_x, odom_y, odom_w, odom_z
    odom_msg = Odometry()
    odom_msg.header.frame_id = "odom"
    odom_msg.child_frame_id = "base_footprint"
    odom_msg.header.stamp = node.get_clock().now().to_msg()
    odom_msg.pose.pose.position.x = data.pose.pose.position.x
    odom_msg.pose.pose.position.y = data.pose.pose.position.y
    odom_msg.pose.pose.orientation.z = data.pose.pose.orientation.z
    odom_msg.pose.pose.orientation.w = data.pose.pose.orientation.w

    odom_msg.twist.twist.linear.x = data.twist.twist.linear.x
    odom_msg.twist.twist.linear.y = 0.0
    odom_msg.twist.twist.angular.z = data.twist.twist.linear.z
    odom_x = data.pose.pose.position.x
    odom_y = data.pose.pose.position.y
    odom_z = data.pose.pose.orientation.z
    odom_w = data.pose.pose.orientation.w

    publisher_odom.publish(odom_msg)

subscriber_odom_temp = node.create_subscription(Odometry, 'odom_temp', callback, 10)

while rclpy.ok():
    #######ROS2 node#######
    br = tf2_ros.TransformBroadcaster(node)
    t = geometry_msgs.msg.TransformStamped()
    t.header.frame_id = "odom"
    t.child_frame_id = "base_footprint"
    t.header.stamp = node.get_clock().now().to_msg()
    t.transform.translation.x = odom_x
    t.transform.translation.y = odom_y
    t.transform.translation.z = 0.0

    t.transform.rotation.x = 0.0
    t.transform.rotation.y = 0.0
    t.transform.rotation.z = odom_z
    t.transform.rotation.w = odom_w

    br.sendTransform(t)
    rclpy.spin_once(node)
    

node.destroy_node()
rclpy.shutdown()