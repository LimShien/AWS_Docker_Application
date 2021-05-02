#/bin/bash

SERVER="ec2-52-209-119-68.eu-west-1.compute.amazonaws.com" ##change this
USER=$1
TARGET="openvpnas@${SERVER}"

##copy the ovpn file from remote server
sudo scp -i "/home/kali/College/AWS_Docker/web/.aws/linux_instance.pem" $TARGET:~/ovpn/$USER.ovpn /tmp/ovpn/