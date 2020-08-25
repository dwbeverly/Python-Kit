import os
import sys
import subprocess

#################################################
#  Simply output images and running containers  #
#################################################

def check_containers():
    subprocess.call("sudo docker images", shell=True)
    subprocess.call("sudo docker ps", shell=True)