
# Welcome to your CDK Python project for Sprint 6!


## Technologies used:

- Flask
- ECR
- ECS
- Fargate
- Docker
- Images

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
 
## Docker Commands
* `docker ps`      current containers
* `docker run`     create and start the container
* `docker create`  create container
* `dokcer exec`    to run commnads in container for once
* `docker volume`  create a docker volume
* `docker network` create a docker network
* `docker rm`      remove container 
* `docker images`  list the images
* `docker rmi`     remove image
* `docker build`   build a new image from dockerfile
* `docker push`    push your image to docker repo
* `docker pull`    download an image from docker repo
* `docker commit`  create an image from container

Flask
=====

Flask is a lightweight `WSGI`_ web application framework. It is designed
to make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around `Werkzeug`_
and `Jinja`_ and has become one of the most popular Python web
application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or
project layout. It is up to the developer to choose the tools and
libraries they want to use. There are many extensions provided by the
community that make adding new functionality easy.

.. _WSGI: https://wsgi.readthedocs.io/
.. _Werkzeug: https://werkzeug.palletsprojects.com/
.. _Jinja: https://jinja.palletsprojects.com/


Installing
----------

Install and update using `pip`_:

.. code-block:: text

    $ pip install -U Flask

.. _pip: https://pip.pypa.io/en/stable/getting-started/


A Simple Example
----------------

.. code-block:: python

    # save this as app.py
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello, World!"

.. code-block:: text

    $ flask run
      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Enjoy!
