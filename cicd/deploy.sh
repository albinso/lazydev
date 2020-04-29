#!/usr/bin/env bash
echo "Deploying CICD server"
cd $1
sudo systemctl restart CICD
