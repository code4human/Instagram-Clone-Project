Code were written in a virtual environment supported by virtualenv(pip3).
The version of django in myvenv is 2.1.5 and version of python (in local computer) is 3.7.4.

***to start virtual environment***
call myvenv/Scripts/activate
***to come out from virtual environment***
deactivate

***to start server***
python manage.py runserver 
***to stop server***
ctrl+c

***to check changes related to DB***
python manage.py makemigrations  
python manage.py makemigrations [appname]
***to load to DB***
python manage.py migrate