import subprocess
import time

try:
    docker_check = subprocess.run(['docker', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if docker_check.returncode != 0:
        raise FileNotFoundError
except FileNotFoundError:
    print("Docker is not installed. Installing Docker...")

    # Commands for configuring Docker GPG key
    gpgKeyCommands = [
        "sudo apt-get update",
        "sudo apt-get install -y ca-certificates curl gnupg",
        "sudo install -m 0755 -d /etc/apt/keyrings",
        "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg",
        "sudo chmod a+r /etc/apt/keyrings/docker.gpg"
    ]
    # Executing commands...
    print("Configuring Docker GPG key")

    for command in gpgKeyCommands:
        result = subprocess.run(command, shell=True)
        if result.returncode != 0:
            print(f"Error while running: {command}")
            raise Exception("An error occurred during Docker GPG key configuration. The script is terminating")

    print("Finished configuring Docker GPG key.")
    # Docker GPG is finished configuring at this point. Script will now attempt to add the Docker Repo to Apt sources.

    print("Adding the Docker repository to Apt sources...")
    aptSourceComm = r'''
    echo \
      "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
      "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    '''
    result = subprocess.run(aptSourceComm, shell=True)

    if result.returncode != 0:
        raise Exception("An error occurred while adding Docker Repo to Apt sources. The script is terminating")
    print("Docker repo successfully added to Apt sources.")

    # Docker repo is added to Apt sources at this point.
    # Now installing Docker packages

    print("Now installing Docker packages...")
    dockerInstallComm = "sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin"
    result = subprocess.run(dockerInstallComm, shell=True)

    if result.returncode != 0:
        raise Exception("An error occurred while installing Docker Packages. The script is terminating")

    print("Docker packages successfully installed.")
    # Docker packages successfully installed at this point.
    # Now we will install docker-compose, so that we may deploy multiple packages at once.

    result = subprocess.run("sudo apt-get install docker-compose", shell=True)
    if result.returncode != 0:
        raise Exception("An error occurred while installing Docker-Compose. Manual installation may be necessary. The script is terminating.")
    # At this point, we have successfully installed Docker and Docker-Compose
    # Script is finished.

    print("Docker and Docker-Compose successfully installed.")
    time.sleep(5)



else:
    print("Docker is already installed.")
    time.sleep(5)
