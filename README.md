
# sample-python

Ausführen:

~~~
$ python3 sample-hello.py
$ python3 sample-postgres.py
$ python3 sample-plotly.py
~~~

Dependencies installieren mit `pip`:

~~~
$ python3 -m venv myvenv
$ source myvenv/bin/activate
$ python3 -m pip install psycopg2-binary
$ python3 -m pip install plotly==5.10.0
$ python3 -m pip install pandas
$ python3 -m pip install kaleido
$ python3 -m pip install flask
$ deactivate
~~~

Dependencies installieren mit `conda`:

~~~
$ conda create -n mycondaenv
$ conda activate mycondaenv
$ conda install -c plotly plotly
$ conda install -c conda-forge pandas
$ conda install -c conda-forge python-kaleido
$ conda deactivate
~~~

## GTK aus Docker Container

~~~
$ docker build -t gtk-dev docker

$ docker run -it --rm \
  -e TERM \
  -e DISPLAY=$DISPLAY \
  -v /usr/local:/usr/local \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v ~/code:/home/philip/code \
  -v ~/code-dl:/home/philip/code-dl \
  gtk-dev

$ cd code/sample-python
$ python3 sample-gtk3.py
$ python3 sample-gtk3-glade.py
$ python3 sample-gtk4.py
~~~

## PyInstaller

Es wird der Docker Container benötigt (siehe oben).

~~~
$ python3 -m pip install -U pyinstaller
~~~

~~~
$ rm -rf build dist
$ pyinstaller sample-gtk3.py
$ pyinstaller sample-gtk3-glade.py
$ pyinstaller sample-gtk4.py
$ ./dist/sample-gtk3/sample-gtk3
$ ./dist/sample-gtk3-glade/sample-gtk3-glade
$ ./dist/sample-gtk4/sample-gtk4
~~~
