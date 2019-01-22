sudo unlink /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart
# GUNICORN_CMD_ARGS="--bind=127.0.0.1 --workers=3" gunicorn hello:app
# gunicorn -b 0.0.0.0:8080 wsgi
# sudo gunicorn -b 0.0.0.0:8080
# gunicorn -c hello:app
# sudo gunicorn -c /etc/gunicorn.d/hello.py hello:app
sudo gunicorn -b 127.0.0.1:8000 hello:app
