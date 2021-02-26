FROM python:3.8

ARG KEYBASE_VERSION=5.6.1-20210125164223.f3b21527b9

ENV KEYBASE_PAPERKEY='' \
    KEYBASE_USERNAME='' \
    SONGLINK_KEY=''

RUN groupadd -g 999 -r keybase && useradd -r --uid 999 -m -g keybase keybase

ADD https://s3.amazonaws.com/prerelease.keybase.io/linux_binaries/deb/keybase_${KEYBASE_VERSION}_amd64.deb /tmp/keybase_amd64.deb

# Prevent modifying apt packages list
RUN apt-get update && \
    touch /etc/default/keybase && \
    apt install -y /tmp/keybase_amd64.deb

WORKDIR /workdir
COPY requirements.txt /workdir/
RUN pip install -r requirements.txt

COPY chrisbot /workdir/chrisbot
COPY setup.py README.md /workdir/
RUN ls /workdir/
RUN pip install -e .

USER keybase

ENTRYPOINT python chrisbot/main.py
