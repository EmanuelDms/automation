#!/bin/bash

# Install firacode (by nikhita :) )
cd /usr/share/fonts
sudo mkdir fira-code && cd fira-code
for type in Bold Light Medium Regular Retina; 
  do 
    sudo wget -O FiraCode-$type.ttf "https://github.com/tonsky/FiraCode/blob/master/distr/ttf/FiraCode-$type.ttf?raw=true"; 
  done
fc-cache -f

cd