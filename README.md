# TwendeMars

A web application that uses NASA's Mars Rover Photos API to exhibit photos of Mars taken by the rover Curiosity.You can click on a photo afterwhich a modal will appear with details about the photo, and the rover Curiosity.Enjoy.

## Prerequisites(What you need to run this application)

* [Python3.6](https://www.python.org/) - Python is a programming language that lets you work quickly
and integrate systems more effectively
* [Django](https://www.djangoproject.com/) - Django is a high-level Python Web framework that encourages rapid    development and clean, pragmatic design
* [postgresql](https://www.postgresql.org/) - PostgreSQL is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.For [Installing postgresql on a mac](prerequisites.md)

## Getting Started and Installation

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

```
git clone https://github.com/kd-kinuthiadavid/TWMRS.git && cd TWMRS/

```
create and activate virtual environment

  ```
  python3.6 -m venv virtual && source virtual/bin/activate

  ```

install the dependencies

```
pip install -r requirements.txt

```

run the application

```
python3.6 manage.py runserver

```
See deployment for notes on how to deploy the project on a live system.

### User Stories/Journey

* [User Stories](specs.md)


## Deployment

For deploying this and other Django-apps:[Deploying Django Apps to Heroku](https://gist.github.com/Benard18/01e28cfbd911f87c7df8ee33cbdaa593)


## Versioning

version 1.0.0

## Bugs

Login may fail as i haven't implemented a user having their own profile, if it does, type the following in url section of your browser to get back to home:

```
http://127.0.0.1:8000

```

## Authors

* **KINUTHIA DAVID**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

## Acknowledgments

* Hat tip to Kiptoo, for issueing the challenge
* [Ben Karanja ](https://gist.github.com/Benard18/01e28cfbd911f87c7df8ee33cbdaa593) for Deployment