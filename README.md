# Iam Benyamin

## start app

### compile scss files

install scss with ``` npm install -g scss ```\
compile files with ``` scss --watch  file1.scss:file1.css file2.scss:file2.css ```\
or
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
    - [ ] home page style
    - [ ] model and functionality
    - [ ] show all by time
    - [ ] show all project categorey
    - [ ] secound page
- [ ] links page
- [ ] push notifications (django, javascript)
- [ ] Send me mail, message in telegram when someone send me message (Connect me form in home view)
    - [ ] Telegram
    - [ ] Mail
- [ ] find better and simple way to use scss in django
- [ ] Dont repeat variables.scss
- [ ] refactor code after above
    - [ ] header for mobile
- [ ] add comment sections for blog posts
    - [ ] contact me form
- [ ] site online chat (waich connect to telegram)
- [ ] send me mail and telegram message with error happed
- [X] loading page
- [ ] SEO


<!-- UI modeled on -->
<!-- https://demo.ayroui.com/templates/business-template/ -->
<!-- https://codesandbox.io/s/f78yv4?file=/index.html:231-358 -->
