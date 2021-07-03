#! bin/sh
cp ~/qtile-demon-slayer/qtile/config.py ~/.config/qtile
cp ~/qtile-demon-slayer/kitty/kitty.conf ~/.config/kitty
cp ~/qtile-demon-slayer/zsh/.zshrc ~/
cd ~/.config/qtile
mkdir icon
mv ~/qtile-demon-slayer/qtile/icon/icon.png ~/config/qtile/icon
sudo chsh -l
sudo chsh -s /usr/bin/zsh

