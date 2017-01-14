![Flask from scratch](https://guides.nanobox.io/assets/quickstart-icons/flask.png)

# Flask from scratch

Run a Flask app locally, install nothing besides nanobox. 

<a href="https://nanobox.io/download"><img src="https://guides.nanobox.io/assets/quickstart-icons/download.png" /></a>

## Clone the repo

```bash
# clone the code
git clone https://github.com/nanobox-quickstarts/nanobox-flask.git

# cd into the flask app
cd nanobox-flask
```

## Run the app

```bash
# Add a convenient way to access your app from the browser
nanobox dns add local flask.dev

# Run Flask as you would normally, with Nanobox
nanobox run python app.py
```

## Check it out

Visit your app at <a href="http://flask.dev:5000" target="\_blank">flask.dev:5000</a>

## Explore
With Nanobox, you don't have to have anything installed on your machine to run your app:

```bash
# drop into a Nanobox console
nanobox run

# where python is installed,
python --version

# your packages are available,
pip list

# and your code is mounted
ls
```

## Now What?
For more details about running Flask apps with nanobox visit [guides.nanobox.io/python/flask/](https://guides.nanobox.io/python/flask/)

<a href="https://nanobox.io"><img src="https://guides.nanobox.io/assets/quickstart-icons/footer.png" /></a>
