FROM rueberger/jupyterhub_base:latest

WORKDIR /srv/jupyterhub

# copy in jupyterhub_config.py
ADD . /srv/jupyterhub

CMD jupyterhub -f /srv/jupyterhub/jupyterhub_config.py