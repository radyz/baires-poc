# Exercise API

## Requirements
* Python 3.5+. A great tool to handle different environments and versions [venv](https://virtualenv.pypa.io/en/stable/)

## Features

* Users are able to submit reviews to the API
* Users are able to retrieve reviews that they submitted
* Users cannot see reviews submitted by other users
* Use of the API requires a unique auth token for each user
* Review Rating between 1 - 5
* Review Title - no more than 64 chars
* Review Summary - no more than 10k chars
* Review IP Address - IP of the review submitter
* Review Submission date - the date the review was submitted
* Review Company
* Reviewer Metadata
* Unit tests must be included providing 100% code coverage
* Provide an authenticated admin view that allows me to view review submissions

## Installation
All commands are assumed to be run from within your shell and in a python
compatible version

### Install dependencies
```sh
> pip install -r requirements.txt
```

### Setup Django
Within the top level `poc` folder execute the following commands to setup
django's db (sqlite) and create the initial admin user
```sh
> ./manage.py migrate
> ./manage.py createsuperuser
```

### Run application
```sh
> ./manage.py runserver 0.0.0.0:8000
```


## Development

### Api docs
Documentation is located at `http://<hostname>:8000/docs` where an interactive
client is available for adhoc tests of services.

All available endpoints are listed. Note that in order to view authenticated
endpoints the user has to also be authenticated (there's an option to login
within the same UI)


### Tests
Although Django offers an excellent test suite, this project has opted for
`pytest` which offers more flexibility while integrating with Django

In order to run all tests execute the following command from within the top
level `poc` folder
```sh
> pytest --cov=.
```

## Usage
Assumes the application is running at port `8000`

### Admin Dashboard
Navigate to `http://<hostname>:8000/admin` to authenticate and access the main
dashboard. From there you can view all reviews created

### Api
Navigate to `http://<hostname>:8000/v1/reviews/review` to authenticate and
access your reviews. Due note that from the API access is restricted to reviews
created by the same user.
