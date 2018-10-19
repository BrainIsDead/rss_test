# rss_test

rss_test this is rss parsing test app 

##Installation

Python 3.7
pipenv 

##Get Started

For getting started project install Python 3.7 and pipenv (using pip)

Clone the project. In the project directory(with Pipfile) run "pipenv install --dev" veinve will be created
and all needed packages('feedparser', 'django', 'python-dateutil') will be installed in venv.

Run venv shell "pipenv shell"

Run project /src/manage.py runserver
Add Django command /src/news/management/commands/get_news.py to the Scheduler (Cron) tasks and run in.
