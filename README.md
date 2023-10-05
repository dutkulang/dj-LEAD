# dj-LEAD

This repo is to Convert the official [LEAD](https://lead.asknet.community) (Local Expert Action Directory) from running using jekyll to Django framework (Python3)

---
## How to setup
 
`Python 3.8 upwards and pip3 must be installed on your system`

1. clone the repo from [dj-LEAD on GitHub](https://github.com/dutkulang/dj-LEAD)

2. change into the directory created from either terminal or git bash

```sh
cd dj-LEAD
```

3. install virtual environment and activate

    - A virtual environment will help isolate your working environment dependencies.

    ```sh
    pip3 install virtualenv; virtualenv myenv ; source myenv/bin/activate
    ```

 4. Install the project's requirements 
 
```sh
 pip install -r requirements.txt
 ```

 5. Make and run migrations, then create super user

 ```sh
 python3 manage.py makemigrations ; python3 manage.py migrate ;
 ```
6. Create a superuser. Remember the username and password that you give to the superuser, that information will be used to login to the admin page
```sh
python3 manage.py createsuperuser
```


 7. run server

 ```sh
python3 manage.py runserver 
 ```

 8. visit http://localhost:8000 to check out the demo. By default it will be empty. 

 9. Visit admin page and start adding profiles

http://localhost:8000/admin
