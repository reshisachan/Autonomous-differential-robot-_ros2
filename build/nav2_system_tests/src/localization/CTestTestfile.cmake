# CMake generated Testfile for 
# Source directory: /home/supro/supro_ws/src/navigation2/nav2_system_tests/src/localization
# Build directory: /home/supro/supro_ws/build/nav2_system_tests/src/localization
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(test_localization "/usr/bin/python3" "-u" "/opt/ros/foxy/share/ament_cmake_test/cmake/run_test.py" "/home/supro/supro_ws/build/nav2_system_tests/test_results/nav2_system_tests/test_localization.xml" "--package-name" "nav2_system_tests" "--generate-result-on-success" "--env" "TEST_MAP=/home/supro/supro_ws/src/navigation2/nav2_system_tests/maps/map_circular.yaml" "TEST_EXECUTABLE=/home/supro/supro_ws/build/nav2_system_tests/src/localization/test_localization_node" "TEST_WORLD=/home/supro/supro_ws/src/navigation2/nav2_system_tests/worlds/turtlebot3_ros2_demo.world" "GAZEBO_MODEL_PATH=/home/supro/supro_ws/src/navigation2/nav2_system_tests/models" "--command" "/home/supro/supro_ws/src/navigation2/nav2_system_tests/src/localization/test_localization_launch.py")
set_tests_properties(test_localization PROPERTIES  TIMEOUT "180" WORKING_DIRECTORY "/home/supro/supro_ws/build/nav2_system_tests/src/localization" _BACKTRACE_TRIPLES "/opt/ros/foxy/share/ament_cmake_test/cmake/ament_add_test.cmake;118;add_test;/home/supro/supro_ws/src/navigation2/nav2_system_tests/src/localization/CMakeLists.txt;9;ament_add_test;/home/supro/supro_ws/src/navigation2/nav2_system_tests/src/localization/CMakeLists.txt;0;")
