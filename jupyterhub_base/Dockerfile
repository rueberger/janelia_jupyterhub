FROM jupyterhub/jupyterhub:latest

WORKDIR /srv/jupyterhub

ADD . /srv/jupyterhub

RUN pip install -r requirements.txt
RUN  git clone https://github.com/jupyterhub/dockerspawner.git && \
     cd dockerspawner && \
     pip install -r requirements.txt && \
     python setup.py install && \
     cd ..

EXPOSE 8000
EXPOSE 389
