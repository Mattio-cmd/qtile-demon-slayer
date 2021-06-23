#! bin/sh
cp ~/demon_slayer/qtile/config.py ~/.config/qtile
cp ~/demon_slayer/kitty/kitty.conf ~/.config/kitty
cp ~/demon_slayer/zsh/.zshrc ~/
cd ~/.config/qtile
mkdir icon
mv ~/demon_slayer/qtile/icon/icon.png ~/config/qtile/icon
sudo chsh -l
sudo chsh -s /usr/bin.zsh

