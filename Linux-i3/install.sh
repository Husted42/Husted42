#!/usr/bin/env bash

set -e

SCRIPT_DIR=$(cd -- "$(dirname -- "$0")" && pwd)

cd "$SCRIPT_DIR"

sudo apt update

xargs sudo apt install -y < packages.txt

if ! command -v alacritty >/dev/null 2>&1; then
	echo "alacritty was not installed from current apt sources. Trying universe repo..."
	sudo apt install -y software-properties-common
	sudo add-apt-repository -y universe
	sudo apt update
	sudo apt install -y alacritty
fi

mkdir -p ~/.config

cp -r .config/i3 ~/.config/
cp -r .config/i3status ~/.config/
cp -r .config/alacritty ~/.config/
cp -r .config/rofi ~/.config/
cp -r .config/picom ~/.config/
cp -r .config/gtk-3.0 ~/.config/
mkdir -p ~/.config/Code/User
cp .config/Code/User/settings.json ~/.config/Code/User/settings.json

cp shell/.bashrc ~/.bashrc
cp shell/.Xresources ~/.Xresources
cp shell/.gitconfig ~/.gitconfig

xrdb -merge ~/.Xresources

echo "Setup complete."