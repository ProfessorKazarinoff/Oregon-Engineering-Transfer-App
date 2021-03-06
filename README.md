# Oregon-Engineering-Transfer-App

A web app that shows how an Engineering classes completed at an Oregon Community College can transfer to an Engineering class at an Oregon 4-year University.  Written in Django and Python.

Documentation on building the Oregon Engineering Transfer Web App can be found here:

 > [https://professorkazarinoff.github.io/Oregon-Engineering-Transfer-App/](https://professorkazarinoff.github.io/Oregon-Engineering-Transfer-App/)

## Goals

 * Web App is useful to student users that want to find transfer classes and useful to administrators that want to post transfer class equivalencies

 * User interface is easy to use and intuitive. Easy for students to select colleges and major and see transfer class equivalencies

 * Administrators at 4-year Universities and 2-year Community Colleges can make changes to the courses offered and transfer class equivalencies

 * Authorization model that allows 4-year college administrators to change transfer equivalencies, but protects student users from changing equivalencies

 * Class-to-class, multiclass-to-multiclass, class-to-multiclass and multiclass-to-class equivalencies are included in Web App model. Two courses at a Community College can transfer as 1 class at a 4-year University. All 1-1, many-1, 1-many and many-many course equivalencies allowed.

 * New 4-year Universities and 2-year Community Colleges can be added to the web app

 * New transfer equivalencies can be added to the web app

 * Web app is well-documented and upgradable

 * Web app is secure to modern standards
 
 ## To work the Oregon Engineering Transfer App on locally
 
Install the [Anaconda distribution of Python](https://anaconda.com/downloads). Open the Anaconda Prompt from the Windows 10 start menu. Enter in the following commands at the Anacoda Prompt:
 
 ```text
 $ git clone https://github.com/professorkazarinoff/oregon-transfer-app.git transfer
 $ cd transfer
 $ conda create -n transfer python=3.7
 $ conda activate transfer
 (transfer)$ pip install -r requirements.txt
 (transfer)$ python manage.py runserver
 ```
 