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

### TODO's for versions 1

- [ ] testimonials section
    - [ ] home page style
    - [ ] model and functionality
    - [ ] show all 
    - [ ] secound page
- [ ] portfolio section
- [ ] push notifications (django, javascript)
- [ ] Send me email when someone send me message (Connect me form in home view) 
- [ ] find better and simple way to use scss in django
- [ ] Dont repeat variables.scss
- [ ] refactor code after above
    - [ ] header for mobile
- [ ] add comment sections for blog posts
    - [ ] contact me form
- [ ] SEO


<!-- UI modeled on -->
<!-- https://demo.ayroui.com/templates/business-template/ -->