#!/bin/bash

# Install Gnome Terminal
sudo apt-get install dconf-cli

sudo apt-get install git

cd ~/Downloads

git clone https://github.com/dracula/gnome-terminal
cd gnome-terminal
./install.sh

# ...follow the steps.

clear

cd