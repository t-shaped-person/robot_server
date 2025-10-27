# Robot Server Installation Instructions

## Step 1: Git clone
`git clone https://github.com/t-shaped-person/robot_server.git`

## Step 2: Install Flask
`pip3 install flask`

## Step 3: Check `server_start.sh` and modify model names if necessary
Edit the following lines in `server_start.sh`:
```
export LIDAR_MODEL="TMINIPRO"
export ROBOT_MODEL="R2MINI"
export MOTOR_MODEL="NEW"
```

## Step 4: Check `robot_app.py` and modify remote_server_ip
Edit the following line in `robot_app.py`:
```
remote_server_ip = 'http://<remote_server_ip>'
Example:
remote_server_ip = 'http://192.168.1.148'
```

## Step 5: Setup Startup Applications
1. Open Startup Applications Preferences
    - ubuntu main button -> Startup Applications Preferences
2. Click Add:
    - Name: robot_server
    - Command: > Browser > \robot_server\server_start.sh
3. Click Add, then Close.

## Step 6: Reboot and verify the server
After reboot, check if remote_server runs properly (it should open a gnome-terminal).  
You should see output like:
```
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:8080
* Running on http://192.168.1.85:8080
```
