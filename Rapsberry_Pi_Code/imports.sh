# Mise à jour de la liste des paquets
sudo apt-get update

# Installation des dépendances nécessaire pour setup le réseau wifi
sudo apt-get install -y hostapd dnsmasq iptables

# Installation de Python et pip (si non installé)
sudo apt-get install -y python3-pip

# Installation des dépendances système pour OpenCV
sudo apt-get install -y python3-opencv

# Installation des bibliothèques Python nécessaires
pip3 install opencv-python # Utilisée pour le traitement d'image et la vidéo
pip3 install flask # Framework web Python minimaliste utile pour sa légèreté et simplicité
pip3 install gevent # Bibliothèque python pour créer un serveur WSGI plus performant que celui proposé par flask

# Normalement déjà présent sur la machine mais si absent installation de RPi.GPIO 
pip3 install RPi.GPIO # Permet de gérer les ports GPIO de la raspberry pi