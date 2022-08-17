
# sample-python

Virtual Environment:

~~~
$ python3 -m venv ~/code/sample-python/.venv
$ source ~/code/sample-python/.venv/bin/activate
$ echo $VIRTUAL_ENV
...
$ deactivate
~~~

Dependencies:

~~~
$ python3 -m pip install psycopg2-binary
~~~

Ausführen:

~~~
$ python3 sample-hello.py
$ python3 sample-postgres.py
~~~
