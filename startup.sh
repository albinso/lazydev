#!/usr/bin/env bash
cd /home/pi/Devel/sunrise
git pull
date +"%T" >> time.txt
sudo systemctl restart mopidy
sudo systemctl restart apache2
sudo systemctl restart AWP
sudo systemctl restart djbeat
sudo systemctl restart djbeatscheduler
