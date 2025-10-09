# Robot Server Installation Instructions

## Step 1: Install Flask
`pip3 install flask`

## step 2: Check `server_start.sh` and modify model names if necessary
Edit the following lines in `server_start.sh`:
```
export LIDAR_MODEL="TMINIPRO"
export ROBOT_MODEL="R2MINI"
export MOTOR_MODEL="NEW"
```

## step 3: Check `robot_app.py` and modify remote_server_ip
Edit the following line in `robot_app.py`:
```
remote_server_ip = 'http://<remote_server_ip>'
Example:
remote_server_ip = 'http://192.168.1.148'
```

## step 4: Setup Startup Applications
1. Open Startup Applications Preferences
    - ubuntu main button -> Startup Applications Preferences
2. Click Add:
    - Name: robot_server
    - Command: > Browser > \robot_server\server_start.sh
3. Click Add, then Close.

## step 5: Reboot and verify the server
After reboot, check if remote_server runs properly (it should open a gnome-terminal).  
You should see output like:
```
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:8080
* Running on http://192.168.1.85:8080
```
