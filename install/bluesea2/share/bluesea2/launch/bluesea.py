import os
from ament_index_python.packages import get_package_share_directory
from launch.exit_handler import restart_exit_handler, ignore_exit_handler,
from ros2run.api import get_executable_path
from launch import LaunchDescription
from launch_ros.actions import Node


def launch(launch_descriptor, argv):
    ld = launch_descriptor
    package = 'bluesea2'
    ld.add_process(
        cmd=[get_executable_path(package_name=package, executable_name='bluesea_node1')],
        name='bluesea_node1',
        exit_handler=restart_exit_handler,
    )
    package = 'tf2_ros'
    ld.add_process(
        # The XYZ/Quat numbers for base_link -> laser_frame are taken from the
        # turtlebot URDF in
        # https://github.com/turtlebot/turtlebot/blob/931d045/turtlebot_description/urdf/sensors/astra.urdf.xacro
        cmd=[
            get_executable_path(
                package_name=package, executable_name='static_transform_publisher'),
            '0', '0', '0',
            '0', '0', '0', '1',
            'base_footprint',
            'LH_laser_back'
        ],
        name='static_tf_pub_laser',
        exit_handler=restart_exit_handler,
    )
    return ld
