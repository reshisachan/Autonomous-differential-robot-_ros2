# CMake generated Testfile for 
# Source directory: /home/supro/supro_ws/src/navigation2/nav2_system_tests/src/recoveries/backup
# Build directory: /home/supro/supro_ws/build/nav2_system_tests/src/recoveries/backup
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(test_backup_recovery "/usr/bin/python3" "-u" "/opt/ros/foxy/share/ament_cmake_test/cmake/run_test.py" "/home/supro/supro_ws/build/nav2_system_tests/test_results/nav2_system_tests/test_backup_recovery.xml" "--package-name" "nav2_system_tests" "--generate-result-on-success" "--env" "TEST_MAP=/home/supro/supro_ws/src/navigation2/nav2_system_tests/maps/map_circular.yaml" "TEST_EXECUTABLE=/home/supro/supro_ws/build/nav2_system_tests/src/recoveries/backup/test_backup_recovery_node" "TEST_WORLD=/home/supro/supro_ws/src/navigation2/nav2_system_tests/worlds/turtlebot3_ros2_demo.world" "GAZEBO_MODEL_PATH=/home/supro/supro_ws/src/navigation2/nav2_system_tests/models" "BT_NAVIGATOR_XML=navigate_w_replanning_and_recovery.xml" "--command" "/home/supro/supro_ws/src/navigation2/nav2_system_tests/src/recoveries/backup/test_backup_recovery_launch.py")
set_tests_properties(test_backup_recovery PROPERTIES  TIMEOUT "180" WORKING_DIRECTORY "/home/supro/supro_ws/build/nav2_system_tests/src/recoveries/backup" _BACKTRACE_TRIPLES "/opt/ros/foxy/share/ament_cmake_test/cmake/ament_add_test.cmake;118;add_test;/home/supro/supro_ws/src/navigation2/nav2_system_tests/src/recoveries/backup/CMakeLists.txt;12;ament_add_test;/home/supro/supro_ws/src/navigation2/nav2_system_tests/src/recoveries/backup/CMakeLists.txt;0;")