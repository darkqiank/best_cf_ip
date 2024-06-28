#!/bin/bash
cd /home/ubuntu/cf
./CloudflareST -cfcolo OKA,NRT,FUK,KIX -tl 300 -p 60 -dd
cd /home/ubuntu/best_cf_ip
/home/ubuntu/miniconda3/bin/python update.py /home/ubuntu/cf/result.csv 20
git add .
git commit -m "Automated commit"
git push origin master

