#!/bin/bash
rsync -a --delete --exclude 'img' --exclude 'font' --exclude '.git' --exclude 'blog' --exclude 'CNAME' --exclude 'README.md' build/ ../kidscancode.github.com/
rsync -a img/ ../kidscancode.github.com/img
