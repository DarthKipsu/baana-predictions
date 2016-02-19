i#!/bin/bash
cd /home/kipsu/baana
/usr/bin/git pull
/usr/bin/python update_predictions.py
/usr/bin/git add -A
/usr/bin/git commit -m 'add daily predictions'
/usr/bin/git push
/usr/bin/git push heroku master
