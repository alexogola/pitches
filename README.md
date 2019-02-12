# Pitches

Web application that allows users to submit quick pitches that will thereafter be voted on by other users who also have the ability to give feedback about the pitches.


## Author name

Alex Ogola

## Technology used

Python 3.6
HTML
Bootstrap 4
JavaScript
Heroku
Postgresql

## Project setup installation

## Prerequisites
- Python 3.6
- Ubuntu software

## Create a Virtual Environment

## Install dependancies

Install dependancies that will create an environment for the app to run

pip3 install -r requirements

Install Postgres

## Prepare environment variables

export DATABASE_URL='postgresql+psycopg2://username:password@localhost/pitches'

export SECRET_KEY='Your secret key'


## Run Database Migrations

python manage.py db init

python manage.py db migrate -m "initial migration"

python manage.py db upgrade

## Running the app in development

In the same terminal type: python3 manage.py server

Open the browser on http://localhost:5000/

## Behaviour driven development
| Behaviour   |      Input     |  Output |
|----------|:-------------:|------:|
| Sign up | Enter email and password |   Sign in successful |
| Log in | Enter email and password |   Login successful |
| Pitch | Enter pitch and click submit button |  Pitch published successful |


## License
MIT licence

Copyright <YEAR> <COPYRIGHT HOLDER>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
