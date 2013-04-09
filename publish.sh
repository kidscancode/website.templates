#!/bin/bash
rsync -a --delete --exclude 'img' --exclude 'font' --exclude '.git' --exclude 'blog' --exclude 'CNAME' --exclude 'README.md' build/ /Users/chris/Documents/kidscancode.github.com/
