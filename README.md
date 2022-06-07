# Iam Benyamin

## start app

### compile scss files

install scss with ``` npm install -g scss ```\
compile files with ``` scss --watch  file1.scss:file1.css file2.scss:file2.css ```\
``` sass --watch --no-source-map static/css/scss/base.scss:static/css/base.css home/static/css/scss/home.scss:home/static/css/home.css blog/static/css/scss/blog.scss:blog/static/css/blog.css ```

### start django

``` pip3 install venv ```\
``` python3 -m venv env_name ```\
``` pip3 install -r requirements.txt ```\
``` python3 manage.py makemigrations ```\
``` python3 manage.py migrate ```\
``` python3 manage.py runserver ```

### TODO's Version Beta

- [ ] refactor code after above todo
- [ ] Responsive 1200px, 992px, 768px, 597px
- [ ] find better and simple way to use scss in django
- [ ] Dont repeat variables.scss

<!-- UI modeled on -->
<!-- https://demo.ayroui.com/templates/business-template/ -->