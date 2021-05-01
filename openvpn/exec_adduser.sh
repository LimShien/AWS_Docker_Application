#/bin/bash

##this script runs the script  on the access server  that creates user.
## with the command sudo ssh -i "linux_instance.pem" openvpnas@ec2-52-209-119-68.eu-west-1.compute.amazonaws.com "sudo /home/openvpnas/script/create_user.sh 'lim'" 

SERVER="ec2-52-209-119-68.eu-west-1.compute.amazonaws.com" ##change this
USER=$1 
TARGET="openvpnas@${SERVER}"
# change directory to the private key file
cd ../.aws

#ssh to the target and execute the script
sudo ssh -i "/home/kali/College/AWS_Docker/web/.aws/linux_instance.pem" $TARGET "sudo /home/openvpnas/script/create_user.sh ${USER}"
