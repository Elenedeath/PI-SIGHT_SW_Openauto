#!/bin/bash

#Update ssid / password of hotspot
ssid=$(grep -Po '(?<=ssid=").*(?=")' /boot/crankshaft/hotspot.conf)
password=$(grep -Po '(?<=password=").*?(?=")' /boot/crankshaft/hotspot.conf)
sudo sed -i "s/^\(ssid\s*=\s*\).*\$/\1$ssid/" /etc/hostapd/hostapd.conf
sudo sed -i "s/^\(wpa_passphrase\s*=\s*\).*\$/\1$password/" /etc/hostapd/hostapd.conf

sleep 1

sudo iwconfig wlan0 txpower 10

sleep 1

#Detect camera connection
string=$(vcgencmd get_camera)
substring="detected=1"
if test "${string#*$substring}" != "$string"
then
    sudo DISPLAY=:0 python3.7 /boot/crankshaft/openauto_controller-cam.py &    # Camera connected
else
    sudo DISPLAY=:0 python3.7 /boot/crankshaft/openauto_controller-noncam.py &    # Camera not connected
fi

#Remote controller pair function
sudo python3.7 /boot/crankshaft/remote_pairing.py &

sleep 1

#Detect remote controller / turn on wifi
sudo python3.7 /boot/crankshaft/BT_detect.py &
