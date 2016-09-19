### Quickstart for Flask on Nanobox
This is the companion application for the [Flask: Getting Started](https://guides.nanobox.io/flask/) guide on [guides.nanobox.io](https://guides.nanobox.io) and is pre-configured and ready to run on [nanobox](https://desktop.nanobox.io/)!

After cloning the repo, **cd into the directory** and run the following commands:

``` bash

# build the code
/nanobox-flask $ nanobox build

# start the dev environment
/nanobox-flask $ nanobox dev start

# add a convenient way to access your app from the browser
/nanobox-flask $ nanobox dev dns add flask.nanobox.dev

# run the app
/nanobox-flask $ nanobox dev console
/app $ pip install Flask
/app $ python hello.py
```

Visit the app from your favorite browser at: `flask.nanobox.dev:8080`

### Now What?
For more details about how this works or for more advanced topics related to running Flask applications on nanobox visit [guides.nanobox.io/flask/](https://guides.nanobox.io/flask/)
