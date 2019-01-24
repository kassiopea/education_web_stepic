#!/bin/sh

# sudo apt-get install python3.5
# sudo apt-get install gunicorn
pip3 install Django==2.0.0
# sudo pip3 install --upgrade django
# pip install Django==2.0.7
sudo rm /etc/nginx/sites-enabled/default

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo ln -sf /home/box/web/etc/gunicorn-wsgi.conf /etc/gunicorn.d/test-wsgi.conf
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test-django.conf

sudo /etc/init.d/nginx restart
# sudo python3 manage.py runserver 0:8000

# gunicorn -c /etc/gunicorn.d/test-django.conf ask.wsgi:application


# gunicorn -c /home/box/web/etc/gunicorn-django.conf ask.wsgi:application
etc/init.d/gunicorn strat
