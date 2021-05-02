#/bin/bash

##change the directory to the path of  sacli command
cd /usr/local/openvpn_as/scripts/ 

#generate the autologin ovpn file 
sudo ./sacli --user $1 AutoGenerateOnBehalfOf

##save the output to ~/ovpn/userid.ovpn
sudo ./sacli --user $1 GetAutologin >~/ovpn/$1.ovpn
