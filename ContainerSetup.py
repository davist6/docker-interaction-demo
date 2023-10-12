import subprocess
import sys

# Checking if docker is installed...
try:
    docker_check = subprocess.run(['docker', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if docker_check.returncode != 0:
        raise FileNotFoundError
except FileNotFoundError:
    print('Docker is not installed. Try running "DockerInstallScript.py". If that doesn\'t work, manual Docker \ninstallation is required.')
    sys.exit(1)

# Check complete, code has exited if docker not found.
# pulling the NGINX and Ubuntu images...

pullCommands = ["sudo docker pull nginx:latest","sudo docker pull ubuntu:latest"]

for pull in pullCommands:
    result = subprocess.run(pull, shell=True)
    if result.returncode != 0:
        print(f"Error while running: {pull}")
        raise Exception(f"Error while running: {pull}, terminating script.")

# Images are pulled.
# Running the docker-compose file (which will attempt to start two nginx and ubuntu containers that will interact w/ each other.
# If successful, ubuntu container will download nginx server contents to CurlOutput directory.

try:
    result = subprocess.run("docker-compose up -d", shell=True)
except:
    print("An error occurred while attempting the docker-compose function. Terminating script.")
    sys.exit(1)

