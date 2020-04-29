#!/usr/bin/env bash
echo "Fetching most recent CICD commit"
cd $1
git pull
