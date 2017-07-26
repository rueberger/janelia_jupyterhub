FROM jupyterhub/jupyterhub:latest

# add to requirements
#RUN pip install jupyterhub-ldapauthenticator

WORKDIR /srv/jupyterhub

ADD . /srv/jupyterhub

RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 389

CMD jupyterhub -f /srv/jupyterhub/jupyterhub_config.py