# Configuration file for jupyterhub.

c.JupyterHub.log_level = 'DEBUG'
c.Spawner.debug = True

c.JupyterHub.extra_log_file = '/var/log/jupyterhub.log'


#c.DockerSpawner.extra_start_kwargs = { 'network_mode': network_name }
# User containers will access hub by container name on the Docker network
c.JupyterHub.hub_ip = ''
c.JupyterHub.hub_port = 8080



## The public facing ip of the whole application (the proxy)
c.JupyterHub.ip = ''

## The class to use for spawning single-user servers.
#
#  Should be a subclass of Spawner.
#c.JupyterHub.spawner_class = 'dockerspawner.'


#------------------------------------------------------------------------------
# Authenticator config
#------------------------------------------------------------------------------

# c.JupyterHub.authenticator_class = 'ldapauthenticator.ldapauthenticator.LDAPLocalAuthenticator'

# c.LDAPAuthenticator.server_address = 'ldap-vip1.int.janelia.org'

# c.LDAPAuthenticator.bind_dn_template = 'cn={username},ou=People,dc=hhmi,dc=org'

# c.LDAPAuthenticator.use_ssl = False
