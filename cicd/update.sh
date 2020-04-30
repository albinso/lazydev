#!/usr/bin/env bash
echo "Fetching most recent CICD commit"
cd $1
git stash
git checkout master
git pull
