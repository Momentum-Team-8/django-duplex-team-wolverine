# Code Snippets
Authored by Logan Atkinson and Roan Blanchard

# Description
Code Snippets allows you create and keep track of small bits of code that you want to use frequently.
A user will be able to create, edit, and delete code snippets. Once created, the user can access them and use the COPY
button to quickly copy the code onto their clipboard. A user can only edit or delete their own snippets.

# Installation and running the program
1. Copy the HTTPS code link on the main page of the repo. Press the green code button to access this.
1. Open your terminal and navigate to the directory that you would like the project to be stored.
1. Type `git clone <REPO URL>` into your terminal and hit return. REPO URL being the HTTPS url given to you by GitHub.
1. Type `django-admin startproject code_snippets` into your terminal and hit return.
1. Naviagte into the new code_snippets directory.
1. Type `pipenv install` into your terminal and hit return.
1. Type `pipenv shell` into your terminal and hit return.
1. Type `python manage.py runserver` into your terminal and hit return. This should give you a localhost url to ⌘+click which will open the project in your default browser.

