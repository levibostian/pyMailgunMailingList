#!/bin/bash

sudo easy_install pip
sudo pip install requests

cd `dirname $0`

python send_email.py

echo "\n"
echo "SUCCESS"
