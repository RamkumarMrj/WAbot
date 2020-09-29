# WhatsApp Bot 
*WhatsApp Bot Developed using Twilio and Python Flask*

<div>

<h2>Try WhatsApp bot :</h2>
<a href="https://api.whatsapp.com/send?phone=+14155238886&text=join%20major-noise">Shortcut Link for Api
</a>

To Join :
```join major-noise```

Example : 
```tell me a joke```

To Stop : 
```stop```

</div>

<div>

## 1. Setup a Python Virtual Environment
 - A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them.

## Create a Project Folder.
 - Run following command to create a new virtual environment inside your project folder:

```python -m venv myvenv```
 - After running above command, a folder named myvenv will get created in your project folder.

 - Activate the virtual environment by running following command:
For ubuntu and mac users:

  ```source myvenv/bin/activate```

For windows users:

  ```myvenv\Scripts\activate```

## 2. Install required Python Packages:
flask : 
    ```pip install flask```

twilio : 
    ```pip install twilio```


## 3. Create a Flask App (app.py)
 - Create Flask App and Run 

```python app.py```

(or)

*Manual Flask Run :*

For CMD :

```$ export FLASK_APP=hello.py```

```$ export FLASK_DEBUG=1```

```$ flask run ```

For PowerShell :

```$env:FLASK_APP = "hello.py"```

```$env:FLASK_DEBUG = 1```

```flask run```

<a href="https://flask.palletsprojects.com/en/1.1.x/quickstart/">Refer flask docs</a>

</div>


*Upload code to git then config heroku*


<div>
<h2>Heroku Installation and Deploy Method :</h2>

- Install the Heroku CLI
Download and install the Heroku CLI.

 - If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

```
$ heroku login
```
## Clone the repository 
 - Use Git to clone wbhelper's source code to your local machine.

```
$ heroku git:clone -a reponame
$ cd reponame
```

 - Deploy your changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.

```
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```

</div>


<div>

*Note :*

*Environment creation :*

```
python -m venv myvenv
myvenv\Scripts\activate

$env:PATH
```

<div>