# OSBU Forecast

[![Build Status](https://travis-ci.org/18F/forecast.svg?branch=master)](https://travis-ci.org/18F/forecast)[![Code Climate](https://codeclimate.com/github/18F/forecast/badges/gpa.svg)](https://codeclimate.com/github/18F/forecast)[![codecov.io](https://codecov.io/github/18F/forecast/coverage.svg?branch=master)](https://codecov.io/github/18F/forecast?branch=master)

An API that provides an interface for the OSBU Forecast Tool, which is an MVP of a better version of http://www.gsa.gov/portal/content/101163. To learn more about the Office of Small Business Utilization at GSA, visit http://www.gsa.gov/portal/category/21015.

# Features
Support for storage via Elastic Search or Django Models.
Separation of API into a read and a write portion.

# Installation

The OSBU Forecast tool is a simple Django application. First, make sure that Python 3 is installed and that you have a version of `virtualenv`:

```
python3 --version
virtualenv --version
```

If you receive errors, install [Python 3](https://docs.python.org/3.5/using/index.html) and/or [virtualenv](https://virtualenv.readthedocs.org/en/latest/installation.html).

Then, installation is as easy as:

```
git clone https://github.com/18F/forecast.git && cd forecast   # Clone the repository
virtualenv .env   # Create a virtualenv
source .env/bin/activate   # Activate virtualenv
cd forecast-admin/forecast && pip install -r requirements.txt   # Install dependencies
./manage migrate
./manage runserver
```

To load existing offices and opportunities from a CSV, run:

```
./manage.py load_opportunities -f [path/to/csv]
```