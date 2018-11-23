# Deployment on AWS

[TOC]

## Sign up for Amazon Web Services (AWS) account

Sign up for an AWS account. We will use the AWS free tier to deploy this Django project.

## Update requirements.txt and push to GitHub

```
$ conda activate transfer
(transfer)$ cd transfer
(transfer)$ pwd
/home/Documents/transfer
(transfer)$ ls
requirments.txt manage.py 
(transfer)$ pip freeze > requirements.txt
```

Take a look at the ```requirments.txt``` file. Ensure the file contains Django, django-crispy-forms and django-bootstrap.

Add, commit and push the changes to GitHub

```
$ git add .
$ git commit -m "updated requirements.txt"
$ git push origin master
```

## Create and log into an AWS instance

Open the Git Bash command window. Start an AWS ec2 instance of Ubuntu 16.04.  Add the following to the security access

SSH - your personal IP, should be auto-populated
HTTP - everyone, all IPs
HTTPS - everyone, all IPs


## Update the server

```
$ sudo apt-get update
```

## Install packages with apt

```
$ sudo apt-get intall python-pip python-dev nginx git tree curl wget
$ sudo apt-get update
```

## Clone the GitHub repo

```
$ git clone https://github.com/ProfessorKazarinoff/Oregon-Engineering-Transfer-App.git repo_name
```

##  Install virtualenv

```
$ sudo pip install virtualenv
```

## Create a new virtual environement

```
$ cd repo_name
$ ls
manage.py requirements.txt
$ virtualenv venv --python=python3
$ source venv/bin/activate
```

## Install Python packages

```
$ pip install -r requirements.txt
```

The packages we need are below. When these are pip installed, the terminal window should output ```requirement already satisfied```

```
$ pip install django
$ pip install django-crispy-forms
$ pip install django-bootstrap4
```

## Install gunicorn, bcrypt and django-extensions

```
$ pip install gunicorn
$ pip install bcrypt django-extensions
```

## Modify ```settings.py```

```
$ cd transfer_project
$ ls
$ nano settings.py
```

Add the AWS instance IP address to the allowed hosts, set debug to False.

```
#transfer_project/settings.py
DEBUG = False
ALLOWED_HOSTS =['aws instance IP address']
```

At the bottom of ```settings.py``` add a line for the static root file path:

```
# At the bottom of /transfer_project/settings.py

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
```

Ctrl-x to and [yes] to save and exit

## Collect Static

```
$ cd ~/repo_name
$ python manage.py collectstatic
```

## Test gunicrn

```
$ gunicorn --bind 0.0.0.0:8000 transfer_project.wsgi:application
deactivate
```

## Create gunicorn.service file

```
$ sudo vim /etc/systemd/system/gunicorn.service
```

Fill out the ```gunicorn.service``` file as below:

```
[Unit]
Description=gunicorn daemon
After=network.target
[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/repo_name
ExecStart=/home/ubuntu/repo_name/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/repo_name/transfer_project.sock transfer_project.wsgi:application
[Install]
WantedBy=multi-user.target

```

## Run gunicorn service

```
$ sudo systemctl daemon-reload
$ sudo systemctl start gunicorn
$ sudo systemctl enable gunicorn
$ sudo systemctl status gunicorn
```

## Create nginx configuration
   
```   
$ sudo vim /etc/nginx/sites-available/transfer_project
```

Fill out the ```transfer_project``` file as below:

```
server {
  listen 80;
  server_name AWS_server_IP_no_quotes;
  location = /favicon.ico { access_log off; log_not_found off; }
  location /static/ {
        root /home/ubuntu/repo_name;
  }
  location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/repo_name/transfer_project.sock;
  }
}

```

## Link the nginx configuration and restart nginx

```
$ sudo ln -s /etc/nginx/sites-available/transfer_project /etc/nginx/sites-enabled
$ sudo nginx -t
#should be no errors
$ rm /etc/nginx/sites-enabled/default
$ sudo service nginx restart
```

## View site at AWS instance IP address

When everything works, browse to the IP address of the AWS instance. You see the following

[image of transfer app running](#)
