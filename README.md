![Sinatra from scratch](https://guides.nanobox.io/assets/quickstart-icons/flask.png)

#### Clone the repo

```bash
# clone the code
git clone https://github.com/nanobox-quickstarts/nanobox-flask.git

# cd into the flask app
cd nanobox-flask
```

#### Run the app
Run Flask as you would normally, with Nanobox

```bash
nanobox run python app.py
```

#### Check it out
Add a convenient way to access your app from the browser

```bash
nanobox dns add local flask.dev
```

Visit your app at <a href="http://flask.dev:5000" target="\_blank">flask.dev:5000</a>

#### Explore
With Nanobox, you don't have to have anything installed on your machine to run your app:

```bash
# drop into a Nanobox console
nanobox run

# where python is installed,
python -v

# your packages are available,
pip list

# and your code is mounted
ls
```

#### Now What?
For more details about running Flask apps with nanobox visit [guides.nanobox.io/python/flask/](https://guides.nanobox.io/python/flask/)
