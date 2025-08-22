#!/bin/bash

gnome-terminal -- bash -c "export LIDAR_MODEL="TMINIPRO" && export ROBOT_MODEL="DONKEYBOTI" && source /opt/ros/humble/setup.bash && source ~/ros2_ws/install/setup.bash && cd ~/robot_server && python3 robot_app.py; exec bash"
