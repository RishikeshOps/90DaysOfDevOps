Docker Cheetsheet 💥
==

```bash=
docker pull nginx #Pull Nginx
docker run --name docker-nginx -p 80:80 nginx #Expose Nginx 80 Port
docker run --name docker-nginx -p 8080:80 -d nginx #Expose 8080
docker run -P nginx
docker run -d -P nginx
```

```bash=
docker build -t imagename .              # Create image using this directory's Dockerfile
docker run -p 4000:80 imagename          # Run "friendlyname" mapping port 4000 to 80
docker run -d -p 4000:80 imagename       # Same thing, but in detached mode
docker run --name test-ubuntu -it ubuntu:16.04 ./bin/bash 
docker exec -it [container-id] bash         # Enter a running container
docker ps                                   # See a list of all running containers
docker stop <hash>                          # Gracefully stop the specified container
docker ps -a                                # See a list of all containers, even the ones not running
docker kill <hash>                          # Force shutdown of the specified container
docker rm <hash>                            # Remove the specified container from this machine
docker rm $(docker ps -a -q)                # Remove all containers from this machine
docker images -a                            # Show all images on this machine
docker rmi <imagename>                      # Remove the specified image from this machine
docker rmi $(docker images -q)              # Remove all images from this machine
docker logs <container-id> -f               # Live tail a container's logs
docker login                                # Log in this CLI session using your Docker credentials
docker tag <image> username/repository:tag  # Tag <image> for upload to registry
docker push username/repository:tag         # Upload tagged image to registry
docker run username/repository:tag          # Run image from a registry
docker system prune                         # Remove all unused containers, networks, images (both dangling and unreferenced), and optionally, volumes. (Docker 17.06.1-ce and superior)
docker system prune -a                      # Remove all unused containers, networks, images not just dangling ones (Docker 17.06.1-ce and superior)
docker volume prune                         # Remove all unused local volumes
docker network prune                        # Remove all unused networks

cd usr/share/nginx/html/

docker volume create my_vol                 # Create a volume
docker volume ls
docker volume inspect my_vol                # troulbeshooting
docker volume rm my_vol



##Setup Docker in EC2
Allows access to port 80 (HTTP) from anywhere
HTTP  TCP  80 Anywhere

   Amezon linux                                           ubuntu
sudo yum update -y                                  sudo apt-get update
sudo yum install -y docker                          sudo apt-get install docker.io -y
sudo service docker start                           sudo service docker start
sudo usermod -aG docker ec2-user                    sudo usermod -aG docker $USER
```

```bash=
**Delete all Exited Containers**

docker rm $(docker ps -q -f status=exited)

**Delete all Stopped Containers**

docker rm $(docker ps -a -q)

**Delete All Running and Stopped Containers**

docker stop $(docker ps -a -q)

docker rm $(docker ps -a -q)

**Remove all containers, without any criteria**

docker container rm $(docker container ps -aq)
```

```bash=
Docker Compose Commands

- Use Docker Compose to Build Containers
Run from directory of your docker-compose.ymI file.
docker-compose build

- Use Docker Compose to Start a Group of Containers
Use this command from directory of your docker-compose.ymi file,

docker-compose up -d

This will tell Docker to fetch the latest version of the container from the
repo, and not use the local cache.

docker-compose up -d --force-recreate

This can be problematic if you're doing CI builds with Jenkins and pushing
Docker images to another host, or using for CI testing. I was deploying a
Spring Boot Web Application from Jekins, and found the docker container
was not getting refreshed with the latest Spring Boot artifact.

#stop docker containers, and rebuild
docker-compose stop -t 1
docker-compose rm -f
docker-compose pull
docker-compose build
docker-compose up -d

- Follow the Logs of Running Docker Containers With Docker Compose
docker-compose logs -f

- Save a Running Docker Container as an Image
docker commit <image name> <name for image>

- Follow the logs of one container running under Docker Compose
docker-compose logs pump <name>

```


# Docker Swarm Commands

- Is Docker Swarm automatically enabled?

No, by default, Docker Swarm is not available

- Types of Nodes in a Docker Swarm

Manager and worker

- Enable the First Node of a Docker Swarm

`docker swarm init`

- List Running Services

`docker service ls`

- Add a Node to a Swarm Cluster

`docker swarm join --token <token> --listen-addr <ip:port>`

- Can manager nodes run containers?

Yes, manager nodes normally run containers

- Retrieve the Join Token

`docker swarm join-token`

- List Nodes in a Cluster

`docker node ls`

- Can you run a ‘docker node Is' from a worker node?
No. Docker Swarm commands can only be from manager nodes

- List Services in a Docker Swarm

`docker service Is`

- List Containers in a Service

`docker service ps <service name>`

- Remove a Service

`docker service rm <service name>`

- Remove a Node from a Swarm Cluster

`docker node rm <node name>`

- Promote a Node from Worker to Manager

`docker node promote <node name>`

- Change a Node from a Manager to 2 Worker

`docker node demote <node name>`

```
