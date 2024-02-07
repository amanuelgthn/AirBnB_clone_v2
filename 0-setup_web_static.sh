#!/usr/bin/env bash
#Bash script that sets up the web servers for the deployment of web_static

if ! command -v nginx &>/dev/null ; then
    sudo apt-get install nginx
fi

if ! [ -d "/data" ]; then
    sudo mkdir /data
fi

if ! [ -d "/data/web_static" ]; then
    sudo mkdir /data/web_static
fi

if ! [ -d "/data/web_static/releases" ]; then
    sudo mkdir /data/web_static/releases
fi

if ! [ -d "/data/web_static/shared" ]; then
    sudo mkdir /data/web_static/shared
fi

if ! [ -d "/data/web_static/releases/test" ]; then
    sudo mkdir /data/web_static/releases/test
fi

echo "<!DOCTYPE html>\
<html lang=\"en\">
    <head>
        <title>Amanuel Bikora developer</title>
    </head>
    <body>
        <h1>Welcome to Amanuel Bikora developer Website</h1>
        <h2>More to come soon</h2>
    </body>
</html>" > /data/web_static/releases/test/index.html

sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data
sudo sed -i "s|/var/www/html|/data/web_static/current|g" /etc/nginx/sites-enabled/default
sudo service nginx restart
exit 0