# Configuration file for jupyterhub.

c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'

c.JupyterHub.log_level = 'DEBUG'
c.Spawner.debug = True

c.JupyterHub.extra_log_file = '/var/log/jupyterhub.log'


# Connect containers to this Docker network
network_name = 'juypterhub_jupyterhub-network'
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network_name
# Pass the network name as argument to spawned containers
c.DockerSpawner.extra_host_config = { 'network_mode': network_name }
#c.DockerSpawner.extra_start_kwargs = { 'network_mode': network_name }
# User containers will access hub by container name on the Docker network
c.JupyterHub.hub_ip = ''
c.JupyterHub.hub_port = 8080

c.DockerSpawner.container_ip = '0.0.0.0'
c.DockerSpawner.hub_ip_connect = 'jupyterhub'


## The public facing ip of the whole application (the proxy)
c.JupyterHub.ip = ''

## The class to use for spawning single-user servers.
#
#  Should be a subclass of Spawner.
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'


#------------------------------------------------------------------------------
# LDAP config
#------------------------------------------------------------------------------

c.LDAPAuthenticator.server_address = 'ldap-vip1.int.janelia.org'

c.LDAPAuthenticator.bind_dn_template = 'cn={username},ou=People,dc=hhmi,dc=org'

c.LDAPAuthenticator.use_ssl = False
