#!/bin/bash

# Stop hostapd and dnsmasq services
systemctl --user stop hostapd
systemctl --user stop dnsmasq
# Désactiver les services hostapd et dnsmasq
systemctl --user disable hostapd
systemctl --user disable dnsmasq


# Restore the original dnsmasq configuration file if it exists
if [ -f $HOME/dnsmasq.conf.orig ]; then
  mv $HOME/dnsmasq.conf.orig $HOME/dnsmasq.conf
fi

# Restore the original dhcpcd.conf file by removing the added lines
sed -i '/interface wlan0/d' $HOME/dhcpcd.conf
sed -i '/static ip_address=192.168.4.1\/24/d' $HOME/dhcpcd.conf
sed -i '/denyinterfaces eth0/d' $HOME/dhcpcd.conf
sed -i '/denyinterfaces wlan0/d' $HOME/dhcpcd.conf

# Restore the original network interfaces file if it exists
if [ -f $HOME/interfaces.orig ]; then
  mv $HOME/interfaces.orig $HOME/interfaces
fi

# Enable and start the wpa_supplicant service to allow connection to other Wi-Fi networks
systemctl --user unmask wpa_supplicant
systemctl --user enable wpa_supplicant
systemctl --user start wpa_supplicant

echo "The network configuration has been restored to normal."
