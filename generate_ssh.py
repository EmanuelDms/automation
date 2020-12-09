#!/usr/bin/python3

import os
import sys

try:
    email = sys.argv[1]
except IndexError:
    print("You must past your email on first argument.")
else:
    instructions = f"""
    sudo apt install xclip -y;
    echo "xclip was successfully installed.";
    ssh-keygen -t rsa -b 4096 -C "{email}";
    echo "SSH key was successfully generated to {email}.";
    xclip -sel clip < ~/.ssh/id_rsa.pub;
    echo "Your SSH key is on your clipboard... just paste it!"
    """
    os.system(instructions)
