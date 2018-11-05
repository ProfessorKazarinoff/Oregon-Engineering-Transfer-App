Title: Oregon Engineering College Transfer App - Part 3: Front Page App
Date: 2018-10-16 12:40
Modified: 2018-10-16 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-3-front-page-app
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 3
Summary: This is the third part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges that want to transfer to 4-year Universities. The transfer web app will show which classes from their community college engineering program will transfer to which classes in a 4-year University engineering program. In this third post, I'll review building the first pages app. The first app to add to the django project. This includes creating the app at the command line, adding the app to the project, creating a view, and creating a urlpattern. Then we'll run the server locally and see if the pages app works.

This is the third part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges that want to transfer to 4-year Universities. The transfer web app will show which classes from their community college engineering program will transfer to which classes in a 4-year University engineering program. In this third post, I'll review building the first pages app. The first app to add to the django project. This includes creating the app at the command line, adding the app to the project, creating a view, and creating a urlpattern. Then we'll run the server locally and see if the pages app works.

## Django Apps

What is a Django app and how is it different from a Django project? A djano app is part of a Django project. One Django project can have many apps.

## Create the pages app

To show our front page and about page, we are going to create a pages app in our Django project.

## Add the pages app to the list of installed apps

```python
# transfer_project/settings.py

# Application definition

INSTALLED_APPS = [
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # project specific
    'pages.apps.PagesConfig',
]

```

## Define a homepage view

In ```pages/views.py``` add the following code:

```python
# pages/views.py

from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('College Transfer App')
```

## Configure the homepage URL pattern in the pages app

In ```pages/urls.py``` add the following code:

```python
# pages/urls.py

from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
```

## Configure the homepage URL pattern in the overall transfer project

In ```transfer_project/urls.py``` add the following code:

```python
# transfer_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
]

```

## Test the server locally

Test the server locally with the ```runserver command```. Make sure you are in the ```(transfer)``` virtual environment when the command is run.

```text
$ conda activate transfer
$ ls
# (should see manage.py)
(transfer)$ manangy.py runserver
```

Browse to:

 > [http://localhost:8000](http://localhost:8000)

## Summary

In this step of developing the Oregon Engineering Transfer App project we added a home page and an about page to the site. We did this by creating a new ```Pages``` app in our ```transfer_project```. We edited the following files:

 * ```transfer_project/settings.py``` - added the ```Pages``` app
 * ```pages/views.py``` - added a pages view function
 * ```pages/urls.py``` - added a home page url route 
 * ```transfer_project/urls.py``` - added a url route to point to the ```Pages``` url routes

 Finally we ran the server locally using ```manage.py runserver``` to view the additions we made.
 