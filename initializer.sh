#!/bin/sh
NAME= $1

git init
git add .

git commit -m "first commit"

git branch -M main

git remote add origin https://github.com/GIORGl/$NAME.git

git push -u origin main
