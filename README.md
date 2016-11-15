![Flask from scratch](https://guides.nanobox.io/assets/quickstart-icons/flask.png)

#### Clone the repo

```bash
# clone the code
git clone https://github.com/nanobox-quickstarts/nanobox-flask.git

# cd into the flask app
cd nanobox-flask
```

#### Run the app

```bash
# Run flask as you would normally, with Nanobox
nanobox run python hello.py
```

#### Check it out

```bash
# Add a convenient way to access your app from the browser
nanobox dns add local flask.dev
```

Visit your app -> [flask.dev:5000](http://flask.dev:5000)

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
For more details about running flask apps with nanobox visit [guides.nanobox.io/python/flask/](https://guides.nanobox.io/python/flask/)
