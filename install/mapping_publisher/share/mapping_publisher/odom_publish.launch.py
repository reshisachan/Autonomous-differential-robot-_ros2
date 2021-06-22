from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mapping_publisher',
            namespace='',
            executable='odom_publish',
            name='odom_publish'
        ),
        Node(
            package='mapping_publisher',
            namespace='',
            executable='Encoder',
            name='Encoder'
        )
    ])