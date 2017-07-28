FROM jupyterhub/jupyterhub:0.7.2

WORKDIR /srv/jupyterhub

ADD . /srv/jupyterhub

RUN pip install -r requirements.txt
RUN  git clone https://github.com/jupyterhub/dockerspawner.git && \
     cd dockerspawner && \
     pip install . && \
     cd ..

RUN apt-get -yqq update && apt-get -yqq install docker.io

EXPOSE 8000
EXPOSE 389
