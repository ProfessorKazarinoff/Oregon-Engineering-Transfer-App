# Deployment on AWS

In this section, we are going to deploy the Oregon Engineering Transfer App on Amazon Web Services (AWS). More specifically, we are going to deploy this Django web app on an AWS EC2 instance. An instance is AWS speak for a virtual private server. This same type of virtual private servers are available from Digital Ocean and Linode. AWS calls them EC2 _instances_. Digital Ocean calls them _Droplets_.

 An advantage of AWS, compared to Digital Ocean or Linode, is a free trier which includes one EC2 instance (one server). Therefore, running our Django App running on AWS should be free.

The steps to deploy our Django App on AWS are a slight modification of a procedure from [Coding Dojo](https://www.codingdojo.com/). Coding Dojo hosts coding boot camps to get programmers ready for jobs quickly. Their coding bootcamps are 14 weeks long. The Coding Dojo bootcamps include Python, Django and Flask in the curriculum. 

A summary of steps to deploy our Django App on AWS is below:

[TOC]

## Sign up for Amazon Web Services (AWS) account

Sign up for an Amazon Web Services (AWS) account here:

 > [https://aws.amazon.com/](https://aws.amazon.com/)

We will use the AWS free tier to deploy this Django project. Once you sign up for an account, you have to go to your email and activate your aws account. After your account is active, log into AWS by clicking the [Sign into Console] button.

![AWS sign into console](images/aws_sign_into_console_button.png)

Once signed in, you are greeted by the ASW managment console:

![AWS Management Console](images/aws_management_console.png)

## Update requirements.txt and push to GitHub

Back at the local machine, open the Anaconda Prompt and activate the ```(transfer)``` virtual environment. Then ```cd``` into the ```transfer``` project. Use ```pip freeze``` to create a ```requirement.txt``` file. On Windows, the command ```pip freeze > requirements.txt``` was needed. Note the ```>``` character in the middle of the command. The ```requirements.txt``` file contains all the Python packages used in the ```(transfer)``` virtual environment.

Later, we will install these same Python packages on the server. 

```text
$ conda activate transfer

(transfer)$ cd transfer
(transfer)$ pwd
/home/Documents/transfer
(transfer)$ ls
courses/           docs/       pages/            templates/
db.sqlite3         LICENSE     README.md         transfer_project/  manage.py*  users/

(transfer)$ pip freeze > requirements.txt
```

Take a look at the ```requirments.txt``` file. Ensure the file contains Django, django-crispy-forms and django-bootstrap. A partial listing of the ```requirements.txt``` file is below:

```text
certifi==2018.10.15
Click==7.0
Django==2.1.2
django-crispy-forms==1.7.0
Jinja2==2.10
livereload==2.5.2

...
```

Add, commit and push the changes to GitHub. 

```
(transfer)$ git add .
(transfer)$ git commit -m "updated requirements.txt"
(transfer)$ git push origin master
```

Do a quick check that the Django project runs without errors and works as expected on the local machine. 

If the Django project doesn't run on the local machine, there is no way the Django project will work on the AWS server. Start the development server on the local machine with the command:

```text
(transfer)$ pwd
# make sure manage.py is in the current working directory

(transfer)$ python manage.py runserver

Django version 2.1.2, using settings 'transfer_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Point a web browser to:

 > [http://localhost:8000/](http://localhost:8000/)

See the Oregon Transfer App in all it's glory:

![Transfer App home page](images/home_page_login_button.png)

Use [Ctrl]-[c] to shut down the development server

The following tasks are now complete:

 * ```requirements.txt``` created
 * changes pushed to GitHub
 * the Django App runs locally as expected with no errors. 

Now close the Anaconda Prompt. We'll use the Git Bash terminal (instead of the Anaconda Prompt) later in the deployment.

## Create and log into the AWS instance

Open the Git Bash command window. Start an AWS EC2 instance of Ubuntu 16.04.  Add the following to the security access:

SSH - your personal IP, should be auto-populated
HTTP - everyone, all IPs
HTTPS - everyone, all IPs


## Update the server

```text
$ sudo apt-get update
```

## Install packages with apt

```text
$ sudo apt-get intall python-pip python-dev nginx git tree curl wget
$ sudo apt-get update
```

## Clone the GitHub repo

```text
$ git clone https://github.com/ProfessorKazarinoff/Oregon-Engineering-Transfer-App.git repo_name
```

##  Install virtualenv

```text
$ sudo pip install virtualenv
```

## Create a new virtual environement

```text
$ cd repo_name
$ ls
manage.py requirements.txt
$ virtualenv venv --python=python3
$ source venv/bin/activate
```

## Install Python packages

```text
$ pip install -r requirements.txt
```

The packages we need are below. When these are pip installed, the terminal window should output ```requirement already satisfied```

```text
$ pip install django
$ pip install django-crispy-forms
$ pip install django-bootstrap4
```

## Install gunicorn, bcrypt and django-extensions

```text
$ pip install gunicorn
$ pip install bcrypt django-extensions
```

## Modify ```settings.py```

```text
$ cd transfer_project
$ ls
$ nano settings.py
```

Add the AWS instance IP address to the allowed hosts, set debug to False.

```text
#transfer_project/settings.py
DEBUG = False
ALLOWED_HOSTS =['aws instance IP address']
```

At the bottom of ```settings.py``` add a line for the static root file path:

```text
# At the bottom of /transfer_project/settings.py

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
```

Ctrl-x to and [yes] to save and exit

## Collect Static

```text
$ cd ~/repo_name
$ python manage.py collectstatic
```

## Test gunicrn

```text
$ gunicorn --bind 0.0.0.0:8000 transfer_project.wsgi:application
deactivate
```

## Create gunicorn.service file

```text
$ sudo vim /etc/systemd/system/gunicorn.service
```

Fill out the ```gunicorn.service``` file as below:

```text
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

```text
$ sudo systemctl daemon-reload
$ sudo systemctl start gunicorn
$ sudo systemctl enable gunicorn
$ sudo systemctl status gunicorn
```

## Create nginx configuration
   
```  text 
$ sudo vim /etc/nginx/sites-available/transfer_project
```

Fill out the ```transfer_project``` file as below:

```text
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

```text
$ sudo ln -s /etc/nginx/sites-available/transfer_project /etc/nginx/sites-enabled
$ sudo nginx -t
#should be no errors
$ rm /etc/nginx/sites-enabled/default
$ sudo service nginx restart
```

## View site at AWS instance IP address

When everything works, browse to the IP address of the AWS instance. You see the following

[image of transfer app running](#)
