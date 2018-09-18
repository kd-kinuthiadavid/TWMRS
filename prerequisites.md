## setting up postgress on a MAC:

* Homebrew makes it really easy to install Postgres. Just run:

```
$ brew install postgres

```


* After it finishes installing, you'll need to configure your computer a bit. First, you need to tell Postgres where to find the database cluster where your databases will be stored:

```	
$ echo "export PGDATA=/usr/local/var/postgres" >> ~/.bash_profile

```

* This command will help some programs find Postgres more easily:

```
$ echo "export PGHOST=/tmp" >> ~/.bash_profile

```

* To load these configuration changes, run:

```
$ source ~/.bash_profile

```

* To start the Postgres server, simply run:

```
$ postgres

```

* You'll have to leave that window open while you need the server. To stop the server, press Ctrl + C (_not_ Cmd + C). If you want Postgres to boot at startup and run in the background, run:

```
$ ln -sfv /usr/local/opt/postgresql/*.plist ~/Library/LaunchAgents

```

* And to start it now (since it won't boot automatically until you restart your computer), run:

```
$ pg_ctl start

```

* To prepare for the next lesson, create a default database with your computer's username:

```
$ createdb $USER

```

* And you're done.


## To create a database, in your terminal:

* We can access our database using the following command:

```
$ psql
james=#

```
* Let us create a new database:

```
james=#  CREATE DATABASE school;

```

* SQL commands are usually case insensitive but by convention we capitalize them. Every SQL command ends with a semicolon ;

```
james=# \c school

```

* We use the \c psql command to connect to the school database. We can view all the databases we have using the \l command.




## in the settings.py located in the TWENDEMARS directory:

* find the databases section:

```

DATABASES = {
'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'twendemars', #name of the database, you can replace with yours, or have it the same as mine
        'USER': 'midik', #replace with your name as the user, the name registerd as the user in postgress 
        'PASSWORD':'12345', #replace this with your password for your database
    }
}

```