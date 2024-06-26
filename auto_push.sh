#!/bin/bash
cd /home/ubuntu/best_cf_ip
/home/ubuntu/miniconda3/bin/python update.py /home/ubuntu/cf/result.csv 60
git add .
git commit -m "Automated commit"
git push origin master

