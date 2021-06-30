#!/usr/bin/python3

import os
import sys

try:
    email = sys.argv[1]
    option = sys.argv[2]
except IndexError:
    print("You must:\n* past your email on first argument\n* choose your option (0 for ubuntu and 1 for archlinux).")
else:
    # apt method
    if (option == 0):
        instructions = f"""
        sudo apt install xclip -y;
        echo "xclip was successfully installed.";
        ssh-keygen -t rsa -b 4096 -C "{email}";
        echo "SSH key was successfully generated to {email}.";
        xclip -sel clip < ~/.ssh/id_rsa.pub;
        echo "Your SSH key is on your clipboard... just paste it!"
        """
    # pacman method
    else:
        instructions = f"""
        sudo pacman -S xclip;
        echo "xclip was successfully installed.";
        ssh-keygen -t rsa -b 4096 -C "{email}";
        echo "SSH key was successfully generated to {email}.";
        xclip -sel clip < ~/.ssh/id_rsa.pub;
        echo "Your SSH key is on your clipboard... just paste it!"
        """
    os.system(instructions)
