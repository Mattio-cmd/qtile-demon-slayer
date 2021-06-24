#! bin/sh
cp ~/qtile_demon_slayer/qtile/config.py ~/.config/qtile
cp ~/qtile_demon_slayer/kitty/kitty.conf ~/.config/kitty
cp ~/qtile_demon_slayer/zsh/.zshrc ~/
cd ~/.config/qtile
mkdir icon
mv ~/qtile_demon_slayer/qtile/icon/icon.png ~/config/qtile/icon
sudo chsh -l
sudo chsh -s /usr/bin.zsh

