import os
import math
import time
import rclpy
import signal
import requests
import threading
import subprocess
import numpy as np
from rclpy.node import Node
from PIL import Image, ImageDraw
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import OccupancyGrid
from rclpy.qos import qos_profile_sensor_data
from rclpy.executors import MultiThreadedExecutor
from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/launch_bringup', methods=['POST'])
def launch_bringup():
    try:
        subprocess.Popen([
            "gnome-terminal", "--",
            "bash", "-c",
            "echo $$ > /tmp/bringup.pid; ros2 launch omorobot_bringup bringup_launch.py; exec bash"
        ])
        return "bringup successfully", 200
    except Exception as e:
        return str(e), 500

@app.route('/cancel_bringup', methods=['POST'])
def cancel_bringup():
    try:
        with open('/tmp/bringup.pid', 'r') as f:
            pid = int(f.read().strip())
        os.killpg(os.getpgid(pid), signal.SIGTERM)
        os.remove('/tmp/bringup.pid')
        return "bringup terminated", 200
    except Exception as e:
        return str(e), 400

@app.route('/launch_cartographer', methods=['POST'])
def launch_cartographer():
    try:
        subprocess.Popen([
            "gnome-terminal", "--",
            "bash", "-c",
            "echo $$ > /tmp/cartographer.pid; ros2 launch omorobot_cartographer cartographer_launch.py; exec bash"
        ])
        return "cartographer successfully", 200
    except Exception as e:
        return str(e), 500

@app.route('/cancel_cartographer', methods=['POST'])
def cancel_cartographer():
    try:
        with open('/tmp/cartographer.pid', 'r') as f:
            pid = int(f.read().strip())
        os.killpg(os.getpgid(pid), signal.SIGTERM)
        os.remove('/tmp/cartographer.pid')
        return "cartographer terminated", 200
    except Exception as e:
        return str(e), 400

@app.route('/save_map', methods=['POST'])
def save_map():
    try:
        proc = subprocess.Popen([
            "gnome-terminal", "--",
            "bash", "-c",
            "ros2 run nav2_map_server map_saver_cli -f ~/map; echo 'close in 5sec'; sleep 1; echo 'close in 4sec'; sleep 1; echo 'close in 3sec'; sleep 1; echo 'close in 2sec'; sleep 1; echo 'close in 1sec'; sleep 1; exit"
        ])
        return "map save successfully", 200
    except Exception as e:
        return str(e), 500
    
@app.route('/launch_navigation', methods=['POST'])
def launch_navigation():
    try:
        subprocess.Popen([
            "gnome-terminal", "--",
            "bash", "-c",
            "echo $$ > /tmp/navigation.pid; ros2 launch omorobot_navigation2 navigation2_launch.py map:=$HOME/map.yaml; exec bash"
        ])
        return "navigation successfully", 200
    except Exception as e:
        return str(e), 500

@app.route('/cancel_navigation', methods=['POST'])
def cancel_navigation():
    try:
        with open('/tmp/navigation.pid', 'r') as f:
            pid = int(f.read().strip())
        os.killpg(os.getpgid(pid), signal.SIGTERM)
        os.remove('/tmp/navigation.pid')
        return "navigation terminated", 200
    except Exception as e:
        return str(e), 400

server_ip = 'http://192.168.1.201'

@app.route('/launch_teleop', methods=['POST'])
def launch_teleop():
    requests.post(server_ip + ":9090/launch_teleop")

@app.route('/cancel_teleop', methods=['POST'])
def cancel_teleop():
    requests.post(server_ip + ":9090/cancel_teleop")

@app.route('/launch_cartographer_rviz', methods=['POST'])
def launch_cartographer_rviz():
    requests.post(server_ip + ":9090/launch_cartographer_rviz")

@app.route('/cancel_cartographer_rviz', methods=['POST'])
def cancel_cartographer_rviz():
    requests.post(server_ip + ":9090/cancel_cartographer_rviz")

@app.route('/launch_navigation_rviz', methods=['POST'])
def launch_navigation_rviz():
    requests.post(server_ip + ":9090/launch_navigation_rviz")

@app.route('/cancel_navigation_rviz', methods=['POST'])
def cancel_navigation_rviz():
    requests.post(server_ip + ":9090/cancel_navigation_rviz")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
