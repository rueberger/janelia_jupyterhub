FROM jupyterhub/jupyterhub:0.7.2

WORKDIR /srv/jupyterhub

# copy in jupyterhub_config.py
ADD . /srv/jupyterhub

RUN  git clone https://github.com/jupyterhub/dockerspawner.git && \
     cd dockerspawner && \
     pip install . && \
     cd ..

RUN  git clone git@github.com:gkdb/ldapauthenticator.git && \
     cd ldapauthenticator && \
     pip install . && \
     cd ..


EXPOSE 8080
EXPOSE 8000
EXPOSE 389

CMD jupyterhub -f /srv/jupyterhub/jupyterhub_config.py