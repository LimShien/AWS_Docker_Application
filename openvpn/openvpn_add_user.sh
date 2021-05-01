/bin/bash 

##pass the username that need to be created as first arguement 


##change the directory to the path of  sacli command
cd /usr/local/openvpn_as/scripts/ 

##create  user
sudo ./sacli --user $1 --key "type" --value "user_connect" UserPropPut

#add the user to group 'student 

sudo ./sacli --user $1 --key "conn_group" --value "student"  UserPropPut


##set password
sudo ./sacli --user $1 --new_pass $1 SetLocalPassword

##reload 
sudo ./sacli start


