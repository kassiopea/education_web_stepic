#!/bin/sh

#переходим в директорию, куда будем пушить проект из гитхаб
sudo cd /var/www/

#после того, как скопировали проект с гитхаб на локальную машину, устанавливаем виртуальное окружение
sudo cd /var/www/web/
sudo pip3 install virtualenv

# создание директории для виртуальной среды. venv - произвольное название
virtualenv venv

# активация среды (deactivate - деактивация вирт.среды)
source venv/bin/activate

# устанавливаем nginx (у меня он был установлен ранее)
sudo apt-get update
sudo apt-get install nginx

# устанавливаем зависимости
sudo pip3 install -r requirements.txt

# удаляем дефолтный файл с настройками сервера
sudo rm /etc/nginx/sites-enabled/default

# создаем символьные ссылки на наши настройки
sudo ln -sf /home/"<username>"/web/etc/nginx_real.conf /etc/nginx/sites-enabled/test.conf
sudo ln -sf /home/"<username>"/web/etc/gunicorn-wsgi_real.conf /etc/gunicorn.d/test-wsgi.conf
sudo ln -sf /home/"<username>"/web/etc/gunicorn-django_real.conf /etc/gunicorn.d/test-django.conf

#переходим в директорию, где лежит manage.py
sudo cd ask
# перезапускаем сервер, проверяем миграции и запускаем django сервер не для боевого сервера (в этом случае запускаем gunicorn вместо django manage.py)
sudo /etc/init.d/nginx restart
python3 manage.py makemigrations
python3 manage.py migrate
sudo python3 manage.py runserver 0:8000
# etc/init.d/gunicorn start
