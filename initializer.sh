#!/bin/sh


echo $1

git init
git add .

git commit -m "first commit"

git branch -M main


git remote add origin "https://github.com/GIORGl/$1.git"

git push -u origin main
