FROM rueberger/jupyterhub_base:latest

WORKDIR /srv/jupyterhub

# copy in jupyterhub_config.py
ADD . /srv/jupyterhub

EXPOSE 8080

CMD jupyterhub -f /srv/jupyterhub/jupyterhub_config.py