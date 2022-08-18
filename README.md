
# sample-python

Virtual Environment:

~~~
$ python3 -m venv myvenv
$ source myvenv/bin/activate
$ echo $VIRTUAL_ENV
...
$ deactivate
~~~

Dependencies mit `pip` (z.B. in Virtual Environment):

~~~
$ python3 -m pip install psycopg2-binary
~~~

~~~
$ python3 -m pip install plotly==5.10.0
$ python3 -m pip install pandas
$ python3 -m pip install kaleido
~~~

Dependencies mit `conda`

~~~
$ conda create -n mycondaenv
$ conda activate mycondaenv
$ conda install -c plotly plotly
$ conda install -c conda-forge pandas
$ conda install -c conda-forge python-kaleido
$ conda deactivate
~~~

Ausführen:

~~~
$ python3 sample-hello.py
$ python3 sample-postgres.py
$ python3 sample-plotly.py
~~~
