import subprocess
from subprocess import *
import time
from flask import send_file
#this function execute the script at openvpn/exec_adduser.sh 
def create_user(user):
    stmt = "sh /home/kali/College/AWS_Docker/web/openvpn/exec_adduser.sh createuser " + user
    subprocess.Popen(stmt,  shell=True)
    #print("success Create Profile")
    print(stmt)
    
def create_ovpn(user):
    stmt = "sh /home/kali/College/AWS_Docker/web/openvpn/exec_adduser.sh createovpn " + user
    subprocess.Popen(stmt,  shell=True)
        
    #print(stmt)
    print("success generate conf")

    
def get_ovpn(user):
    stmt = "sh /home/kali/College/AWS_Docker/web/openvpn/exec_getovpn.sh " + user
    subprocess.Popen(stmt,  shell=True)
            
    #print(stmt)
    print("success download conf")
def download_path(user):
	path = "/tmp/ovpn/" + str(user) + '.ovpn'      ##absolute path for the file
	return path
