# docker-interaction-demo

The purpose of this project is to demonstrate the capabilties of:
  1.) Docker containers interacting with eachother; in this case, NGINX and Ubuntu. (Ubuntu container will be used to download the content of an NGINX container)
  2.) Docker-compose being utilized to deploy our containers simultaniously.
  3.) Python scripts automating the Docker installation process (Docker GPG key configuration -> Configuring Docker repo with Apt sources -> Docker package installation -> Docker-compose installation.)
  4.) Python scripts automating the pulling of NGINX and Ubuntu images, and the deployment of our containers via docker-compose.

Instructions for properly executing the scripts included within this demo:
 0.) Prerequisite A: Ensure that the host machine is running Ubuntu 22.04 (check via bash command: "lsb_release -a")
     Prerequisite B: Ensure that the host machine has Python 3 installed (check via bash command: "python3 --version")
     
 1.) After cloning this repo to a directory of choice, within the shell, ensure the root directory of the project is the current working directory.
 
 2.) Run the script "DockerInstallScript.py" to install Docker and Docker-Compose. This script will auto-detect if Docker is already installed.
     (This can be ran via bash command: "python3 DockerInstallScript.py")
     
 3.) Run the script "ContainerSetup.py", which will both: pull the Docker images, and start the Docker-compose action.
     (This can be ran via bash command: "python3 ContainerSetup.py")
     
 4.) Observe as the Docker-compose action starts both our NGINX webserver container, and our Ubuntu container.
     - The Ubuntu container will install Curl onto itself, and then use Curl to install the HTML content of the NGINX webserver.
     - The downloaded content will be output to "CurlOutput", a file within the root directory of our project. This is possible because docker-compose mounted CurlOutput within the Ubuntu container's filesystem.

 5.) After conclusion of the download operation, easily clean up the containers with the bash command: "docker-compose down".
 
