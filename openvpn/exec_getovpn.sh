#/bin/bash

SERVER="54.247.96.244" ##change this
USER=$1
TARGET="openvpnas@${SERVER}"

##copy the ovpn file from remote server
sudo scp -i "/home/kali/College/AWS_Docker/web/.aws/VPN-KP.pem" $TARGET:~/ovpn/$USER.ovpn /tmp/ovpn/