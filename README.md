
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

## GTK aus Docker Container

~~~
$ docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v ~/code/sample-python:/sample-python \
  ubuntu:22.04
$ apt-get update && \
  apt-get install --yes python3 python3-pip python3-venv && /
  apt-get install --yes libgtk-3-bin libgtk-3-common libgtk-3-dev libgtk-3-doc && /
  apt-get install --yes libgtk-4-bin libgtk-4-common libgtk-4-dev libgtk-4-doc
$ adduser --uid 1000 --disabled-password --gecos "" --shell /bin/bash myuser
$ su myuser
$ cd sample-python
$ python3 sample-gtk3.py
$ python3 sample-gtk4.py
~~~
