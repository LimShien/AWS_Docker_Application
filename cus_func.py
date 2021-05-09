import subprocess
from subprocess import *
import time
import json
from flask import send_file
#this function execute the script at openvpn/exec_adduser.sh 
def create_user(user):
    stmt = "sh /home/kali/College/AWS_Docker/web/openvpn/exec_adduser.sh createuser " + user
    subprocess.Popen(stmt,  shell=True)
    print(stmt)
    
def create_ovpn(user):
    stmt = "sudo sh /home/kali/College/AWS_Docker/web/openvpn/exec_adduser.sh createovpn " + user
    subprocess.Popen(stmt,  shell=True)
    print("OVPN onfiguration file generated")
    print(stmt)
    
def get_ovpn(user):
    stmt = "sh /home/kali/College/AWS_Docker/web/openvpn/exec_getovpn.sh " + user
    subprocess.Popen(stmt,  shell=True)
    print("OVPN configuration file transferred")

            
    #print(stmt)
def download_path(user):
    ##absolute path for the file
	path = "/tmp/ovpn/" + str(user) + '.ovpn'

	return path

def launch(instance):
    stmt= "aws ec2 start-instances --instance-ids " + instance
    print(stmt)
    subprocess.Popen(stmt,  shell=True)
    
def stop(instance):
    stmt= "aws ec2 stop-instances --instance-ids " + instance
    print(stmt)
    subprocess.Popen(stmt,  shell=True)

def get_instance():
    
    stmt="sudo aws ec2 describe-instances --query 'Reservations[].Instances[].[InstanceId,PublicIpAddress,PrivateIpAddress,Tags[?Key==`Name`] |[0].Value]' --output json > /tmp/ovpn/aws_output.json; sudo chmod 777 /tmp/ovpn/aws_output.json"           
    subprocess.Popen(stmt,  shell=True)
    #print("Saving CLi output")
    try:
        f = open("/tmp/ovpn/aws_output.json")
        data = json.load(f)
    except:
        data = "Error"

    return data
    #print("done")
