#!/usr/bin/python3

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import LifecycleNode
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.actions import LogInfo

import lifecycle_msgs.msg
import os


def generate_launch_description():
    share_dir = get_package_share_directory('bluesea2')
    node_name = 'bluesea_node'



    driver_node = LifecycleNode( name='bluesea_node_2', namespace='/', package='bluesea2', executable='bluesea_node', output='screen', emulate_tty=True,)

    tf2_node = Node(package='tf2_ros',
                    executable='static_transform_publisher',
                    name='static_tf_pub_laser',
                    arguments=['0', '0', '0.02','0', '0', '0', '1','base_link','LH_laser_back'],
                    )

    return LaunchDescription([
        driver_node,
        #tf2_node,
    ])
