sudo unlink /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/etc/hello.py /etc/gunicorn.d/hello
sudo /etc/init.d/nginx restart
# sudo service gunicorn restart
gunicorn -b 0.0.0.0:8080 hello:app
