# Flask with Nanobox
This is the companion application for the [Flask: Getting Started](https://guides.nanobox.io/flask/) guide on [guides.nanobox.io](https://guides.nanobox.io) and is pre-configured and ready to run with [nanobox](https://desktop.nanobox.io/)!

## Up and Running

``` bash

# clone the code
git clone https://github.com/nanobox-quickstarts/nanobox-flask.git

# cd into the flask app
cd nanobox-flask

# start the dev environment
nanobox dev start

# add a convenient way to access your app from the browser
nanobox dev dns add flask.nanobox.dev

# console into the dev environment
nanobox dev console

# run the application
python hello.py
```

Visit the app from your favorite browser at: `flask.nanobox.dev:8000`

### Now What?
For more details about how this works or for more advanced topics related to running Flask applications with nanobox visit [guides.nanobox.io/flask/](https://guides.nanobox.io/flask/)
