# OSBU Forecast

[![Build Status](https://travis-ci.org/18F/osbu-forecast-api.svg?branch=master)](https://travis-ci.org/18F/osbu-forecast-api)[![Code Climate](https://codeclimate.com/github/18F/osbu-forecast-api/badges/gpa.svg)](https://codeclimate.com/github/18F/osbu-forecast-api)[![Coverage Status](https://coveralls.io/repos/18F/osbu-forecast-api/badge.svg?branch=master&service=github)](https://coveralls.io/github/18F/osbu-forecast-api?branch=master)

An API that provides an interface for the OSBU Forecast Tool, which is an MVP of a better version of http://www.gsa.gov/portal/content/101163. To learn more about the Office of Small Business Utilization at GSA, visit http://www.gsa.gov/portal/category/21015.

# Features
Support for storage via Elastic Search or Django Models.
Separation of API into a read and a write portion.

# Installation

The OSBU Forecast tool is a simple django application. To install, make sure python3 and [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/index.html) (or other preferred virtualenv framework). Then, installation is as easy as:

```
git clone https://github.com/18F/osbu-forecast-api.git && osbu-forecast-api   # Clone the repository
workon && mkvirtualenv forecast
cd forecast-admin/forecast && pip install -r requirements
./manage migrate
./manage runserver
```
