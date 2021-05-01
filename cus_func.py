import subprocess
from subprocess import *

#this function execute the script at openvpn/exec_adduser.sh 
def create_user(user):
    stmt = "sh /home/kali/College/AWS_Docker/web/openvpn/exec_adduser.sh " + user
    subprocess.Popen(stmt,  shell=True)
    print("success")
    print(stmt)
    