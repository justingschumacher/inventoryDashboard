20 Apr 2018
#Machine Setup
Django has the concept of a project and an application (app). Generally speaking, you have many apps in a project.
A project has machine specific configuration, while the app is where the actual code is.

In this case the setup will entail how to get a local testing environment, close the app from gitlab, and pushing
changes to 'production'.

Some good resources for setting up Django/nginx/gunicorn:
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04
http://cheng.logdown.com/posts/2015/01/29/deploy-django-nginx-gunicorn-on-mac-osx-part-2

For server setup, the top link for Ubuntu details the steps on setting up the server using gunicorn and nginx.

We use Bootstrap cdn for page formatting:
https://getbootstrap.com/docs/4.0/getting-started/introduction/

And of course, Django docs:
https://docs.djangoproject.com/en/2.0/

##Machine Setup
* Install: python3, pip3, virtualenv.
* Create a directory for the project and change to that directory
* Create a virtualenv: virtualenv {projectname}_env
* Start the virtualenv: source {projectname}_env/bin/activate
* Pip install Django
* Run: django-admin startproject {projectname} .  (the dot at the end tells the project to be built in the current directory)
* Run: python manage.py startapp {appname}     (inventoryDashboard for nordstrom_inventory_dashboard, formEntry fort goaldashboard,  inventorysearch for nordstrom_inventory_search/manager)

To clone to a non empty directory (https://stackoverflow.com/questions/2411031/how-do-i-clone-into-a-non-empty-directory), we need to do the following:
* Make directory: temp
* Change to directory: temp
* Clone the repo's .git folder: git clone --no-checkout repo-to-clone . (again, trailing dot indicates current directory)
* Move the .git to the project directory: mv .git ..
* Remove the temp dir: rm -rf temp
* Clone the repo's content: git reset --hard HEAD

This should get you the current app in the right place. It should look like this (replace project/app names as appropriate):

     -> nordstrom_inventory_dashboard       (project name)
        -> Readme.md                        (this doc!)
        -> inventoryDashboard               (application itself)
            -> __init__.py
            -> __pycache__
            -> admin.py                     (configures the prebuilt admin site)
            -> apps.py                      (configures the apps the project will be aware of)
            -> filters.py
            -> forms.py                     (configure application forms, unused yet)
            -> migrations                   (django's tracking of database changes it makes)
                -> 0001_initial.py
                -> __pycache__
                -> __init.py__
            -> models.py                    (configure database model to table coorelation)
            -> static                       (directory, where you put css, images... referenced in urls.py or settings.py)
            -> templates
                -> admin
                    -> app_index.html
                -> inventoryDashboard       (application name, application specific html)
                    -> base.html            (base html doc that we import into others that includes Bootstrap config, etc)
                    -> index.html           (html rendering to the client, pulling in from views, base.html, etc)
                    -> ...                  (all others)
            -> tests.py                     (tests to be included for testing)
            -> urls.py                      (map urls to templates (html pages))
            -> views.py                     (configure the view from which the html is rendered)
        -> manage.py
        -> nordstrom_inventory_dashboard    (project config files)
            -> __init__.py
            -> __pycache__
            -> settings.py                  (configure this for database, apps, and static file locations)
            -> urls.py                      (configure this to point traffic to the apps)
            -> wsgi.py
        -> nordstrom_inventory_dashboard_env     (virtualenv files)
        -> requirements.txt                 (project python package requirements)
        -> .git
        -> .gitlab-ci.yml                   (this file makes gitlab put any checkin through the ci/cd pipeline)
        
Once you have created the project, the app and cloned the repo from above steps, you must configure the project to know where to find aspects of the app.
Using the above dir structure...
Update urls.py in nordstrom_inventory_dashboard (not inventoryDashboard the app!) to look like this: <br>

```
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('', include('inventoryDashboard.urls')),
    path('admin/', admin.site.urls),
]
```
Next, modify the settings.py with the following:
* In the INSTALLED_APPS section, add the following to the end of the list
```
    'widget_tweaks',
    
    'django_pandas',
    
    'inventoryDashboard',
```
* In the DATABASES section modify the database definition to include the correct connection info:
```
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'inventory',
        'USER': 'inventory_bi',
        'PASSWORD': 'redacted',
        'HOST': 'itr-rds-postgresql-singleaz-inventoryv2.cnruvikcaov9.us-west-2.rds.amazonaws.com',
        'PORT': '5432',
    },
```
* At the end of the file, add the staticfiles location:
```
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
```
  

From here, there's a few Django commands to note:

* python manage.py runserver   (this runs a minor web server on 127.0.0.1:8000 for you to test)
* python manage.py inspectdb --database (database name, must be in settings.py) (tablename)

You should now have a functional local test environment. There may be additional tweaks depending on your environment, changes in Django, etc.

