# Welcome to the Oregon Transfer App Docs

<br>

This documentation serves as a record of the creation of the Oregon Transfer App. 

The Oregon Transfer app is a web app that shows how an Engineering class completed at an Oregon Community College can be transferred to an engineering class in an Oregon 4-year School.  Written in Django and Python.

<br>

The GitHub repo for the project can be found here: 

 > [https://github.com/ProfessorKazarinoff/oregon-transefer-app](https://github.com/ProfessorKazarinoff/oregon-transfer-app)

<br>

Click the menu items on the left to view the development steps.

Or click the arrows at the bottom of each page.

[![Next Setup Arrow](images/next_button.png)](part1_motivation.md)

<br>

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
 
 ## To work on the project locally
 
 Install the [Anaconda distribution of Python](https://anaconda.com/downloads). Open the Anaconda Prompt. Run the following commands:
 
 ```text
 git clone https://github.com/professorkazarinoff/oregon-transfer-app.git transfer
 cd transfer
 conda create -n transfer python=3.7
 conda activate transfer
 conda install django
 pip install django-crispy-forms
 manage.py runserver
 ```

 [Ctrl]-[c] to exit.