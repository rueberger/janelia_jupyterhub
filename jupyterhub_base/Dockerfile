FROM jupyterhub/jupyterhub:latest

WORKDIR /srv/jupyterhub

ADD . /srv/jupyterhub

RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 389
