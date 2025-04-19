# python run_all.py

import subprocess
import sys

# Kill all processes
subprocess.run([sys.executable, "kill_processes.py"])

# # run Database
# subprocess.run([sys.executable, "app_database.py"])

# Start FastAPI
print("Starting FastAPI...")
subprocess.Popen(["uvicorn", "app_fastapi:app"])

# Start Flask
subprocess.Popen([sys.executable, "app_flask.py"])

# # Start Socket Server
# subprocess.Popen([sys.executable, "socket_server.py"])

# Start Tkinter App
subprocess.Popen([sys.executable, "app_tkinter.py"])