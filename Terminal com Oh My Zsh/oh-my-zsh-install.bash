#!/bin/bash
echo -e "#################### \nZSH \n####################"
echo -e "I'm assuming that you're using Ubuntu linux..."

# Install ZSH
sudo apt-get install zsh

# Install cURL for Oh My Zsh
sudo apt-get install cURL

clear

# Install Oh My Zsh
echo -e "#################### \nOH MY ZSH \n####################"

sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# Set zsh as default
# chsh -s $(which zsh)