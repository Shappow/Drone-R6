#!/bin/bash

# Restaurer la configuration par défaut de dhcpcd.conf
sudo sed -i '/interface wlan0/d' /etc/dhcpcd.conf
sudo sed -i '/static ip_address=192.168.4.1\/24/d' /etc/dhcpcd.conf
sudo sed -i '/nohook wpa_supplicant/d' /etc/dhcpcd.conf

# Arrêter les services
sudo systemctl stop hostapd
sudo systemctl stop dnsmasq

# Désactiver les services
sudo systemctl disable hostapd
sudo systemctl disable dnsmasq

# Restaurer le fichier dnsmasq.conf original
sudo mv /etc/dnsmasq.conf.orig /etc/dnsmasq.conf

# Redémarrer le service dhcpcd
sudo service dhcpcd restart

# Instructions de fin
echo "Le Raspberry Pi a été réinitialisé pour se connecter à un réseau
Wi-Fi existant."
