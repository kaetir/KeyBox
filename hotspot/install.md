 # Installation du hot-spot wifi et du portail captif



https://github.com/billz/raspap-webgui

```bash
sudo raspi config 
# change local and keyboard layout 
# enable i2c and GPIO
sudo apt-get update
sudo apt-get dist-upgrade
sudo reboot
curl -sL https://install.raspap.com | bash
sudo systemctl disable lighttpd
sudo systemctl disable raspap
sudo apt install git
git clone https://github.com/kaetir/KeyBox

```

