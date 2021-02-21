## The Makefile includes instructions on environment setup for running locally and lint tests

## Create python virtualenv & source it at terminal 
# setup: Manually setup at terminal
# python3.8 -m venv venv
	## activate venv: 
# source venv/bin/activate 

install:
	# This should be run from inside a virtualenv	
	pip install --upgrade pip &&\
		pip install -r requirements.txt 

	# Install hadolint	
	wget -O ./hadolint https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64 &&\
	chmod +x ./hadolint

lint:
	
	# hadolint is linter for Dockerfiles
	./hadolint Dockerfile

	# This is a linter for Python source code linter: https://www.pylint.org/	
	# This should be run from inside a virtualenv
	# --load-plugins pylint_flask and pylint_flask_sqlalchemy are for linting flask app
	
	pylint --disable=R,C,W1203 --load-plugins pylint_flask_sqlalchemy --load-plugins pylint_flask app.py
	pylint --disable=R,C forms.py
	pylint --disable=R,C hypothyroid.py

all: install lint 
