#!/bin/bash

# Install Spaceship
git clone https://github.com/denysdovhan/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt"

# Creates a Symbolic Link
sudo ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"

# Set spaceship as theme
sudo sed -i "/ZSH_THEME/c\ZSH_THEME='spaceship'" ~/.zshrc

# Restart terminal
source ~/.zshrc