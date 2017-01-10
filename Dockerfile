FROM python:2.7-onbuild
MAINTAINER Areth <al.reshetnikov@gmail.com>

#CMD [ "python", "-m", "lserver" ]
# Use entrypoint instead of CMD to be able to pass parameters
ENTRYPOINT ["/usr/src/app/docker-start.sh"]