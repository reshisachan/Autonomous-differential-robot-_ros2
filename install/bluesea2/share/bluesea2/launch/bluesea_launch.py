from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	return LaunchDescription([
		Node(
			package='bluesea2',
			executable='bluesea_node_1',
			name='bluesea_node_1'
		),
		Node(
			package='tf2_ros',
			executable='static_transform_publisher',
			name='laser_transform',
			arguments = ["0", "0", "0", "0", "0", "0", "1", "base_link", "LH_laser_front"]
		),
	])
