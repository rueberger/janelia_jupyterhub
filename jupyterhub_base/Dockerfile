FROM jupyterhub/jupyterhub:0.7.2

WORKDIR /srv/jupyterhub

ADD . /srv/jupyterhub

RUN pip install -r requirements.txt
RUN  git clone https://github.com/jupyterhub/dockerspawner.git && \
     cd dockerspawner && \
     pip install . && \
     cd ..

RUN wget https://get.docker.com -q -O /tmp/getdocker && \
    chmod +x /tmp/getdocker && \
    sh /tmp/getdocker

EXPOSE 8000
EXPOSE 389
