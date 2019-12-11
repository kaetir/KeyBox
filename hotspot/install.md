 # Installation du hot-spot wifi et du portail captif



https://github.com/billz/raspap-webgui

```bash
sudo apt-get update
sudo apt-get dist-upgrade
sudo reboot
curl -sL https://install.raspap.com | bash
```



## Portail captif

https://pimylifeup.com/raspberry-pi-captive-portal/

```bash
sudo apt install git libmicrohttpd-dev
cd ~
git clone https://github.com/nodogsplash/nodogsplash.git
cd ~/nodogsplash
make
sudo make install
```

```
sudo nano /etc/nodogsplash/nodogsplash.conf
```

add to **/etc/nodogsplash/nodogsplash.conf**

```
GatewayInterface wlan0
GatewayAddress 192.168.10.1
MaxClients 250
AuthIdleTimeout 480
```

```bash
sudo nodogsplash
```

**Now if you connect to your WiFi hotspot, you should be greeted by the captive portal**

```bash
sudo nano /etc/rc.local
```

**Find:**

```
exit 0
```

**Add above:**

```
nodogsplash
```

```bash
sudo nano /etc/nodogsplash/htdocs/splash.html
```