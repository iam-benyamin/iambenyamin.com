# start app on local

### compile scss files

install scss with ``` npm install -g scss ```\
change dirctory to app ``` cd project_dirctory/app/ ```
compile files with ``` scss --watch  file1.scss:file1.css file2.scss:file2.css ```\
or
``` sass --watch --no-source-map static/css/scss/base.scss:static/css/base.css home/static/css/scss/home.scss:home/static/css/home.css blog/static/css/scss/blog.scss:blog/static/css/blog.css static/css/scss/sections/loading.scss:static/css/loading.css links/static/css/scss/links.scss:links/static/css/links.css portfolio/static/css/scss/portfolio.scss:portfolio/static/css/portfolio.css ```

### start django

``` pip3 install venv ```\
``` python3 -m venv env_name ```\
``` pip3 install -r requirements.txt ```\
``` python3 manage.py makemigrations ```\
``` python3 manage.py migrate ```\
"``` python3 manage.py runserver --settings=config.settings.development ```" or "``` python3 manage.py runserver --settings=config.settings.production ```"


<!-- https://demo.ayroui.com/templates/business-template/ -->
<!-- https://fontawesome.com/ -->
<!-- https://codepen.io/ -->