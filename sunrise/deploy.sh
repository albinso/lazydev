#!/usr/bin/env bash
cd $1
#sudo systemctl restart mopidy
sudo systemctl restart apache2
#sudo systemctl restart AWP
sudo systemctl restart djbeat
sudo systemctl restart djbeatscheduler
