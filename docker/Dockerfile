FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install --yes python3 python3-pip python3-venv && \
    apt-get install --yes libgtk-3-bin libgtk-3-common libgtk-3-dev libgtk-3-doc && \
    apt-get install --yes libgtk-4-bin libgtk-4-common libgtk-4-dev libgtk-4-doc && \
    apt-get install libgirepository1.0-dev && \
    adduser --uid 1000 --disabled-password --gecos "" --shell /bin/bash philip

USER 1000:1000
WORKDIR /home/philip

RUN echo 'PATH="$HOME/.local/bin:$PATH"' >> .bashrc
