# rules to build the images

build_jhub_base:
						cd jupyterhub_base; \
	       		docker build -t rueberger/jupyterhub_base .

push_jhub_base: build_jhub_base
				 		docker push rueberger/jupyterhub_base

build_jhub: push_jhub_base
						cd janelia_jupyterhub; \
						docker build -t rueberger/jupyterhub_janelia .

push_jhub: build_jhub
						docker push rueberger/jupyterhub_janelia
