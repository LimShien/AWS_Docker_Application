#/bin/bash

##this script runs the script  on the access server  that creates user.
## with the command sudo ssh -i "linux_instance.pem" openvpnas@ec2-52-209-119-68.eu-west-1.compute.amazonaws.com "sudo /home/openvpnas/script/create_user.sh 'lim'" 

SERVER="ec2-52-209-119-68.eu-west-1.compute.amazonaws.com" ##change this
USER=$2
TARGET="openvpnas@${SERVER}"


if [ "$1" = 'createuser' ]
then
    T_PATH='/home/openvpnas/script/create_user.sh'
elif [ "$1" = 'createovpn' ] 
then
    T_PATH='sudo /home/openvpnas/script/get_ovpn.sh'
else
    T_PATH='/home/openvpnas/script/'
fi



#ssh to the target and execute the script
sudo ssh -i "/home/kali/College/AWS_Docker/web/.aws/linux_instance.pem" $TARGET "$T_PATH $USER"


