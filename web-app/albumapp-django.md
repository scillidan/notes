### [Album App for Django](https://github.com/jobsta/albumapp-django)

![](https://img.shields.io/github/license/jobsta/albumapp-django?style=flat-square)

````{tab} From source
```sh
git clone --depth=1 https://github.com/jobsta/albumapp-django
cd albumapp-django
uv venv
.venv\Scripts\activate.bat
uv pip install django reportbro-lib
python manage.py makemigrations albums
python manage.py migrate
python manage.py compilemessages
python manage.py runserver localhost:8010
```
````

Visit `localhost:8010/albums`.