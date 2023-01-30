1) What is the Difference between an Image, Container and Engine?
- An image is a snapshot of a Docker container. A container is a running instance of an image. An engine is the component of the Docker platform that builds and runs containers.
2) What is the Difference between the Docker command COPY vs ADD?
- COPY is a command used to copy files from the host file system into a Docker image, while ADD can perform the same function, but with the added ability to handle archive files (i.e. tar, gzip) and extract them into the image file system.
3) What is the Difference between the Docker command CMD vs RUN?
- CMD is used to set default commands in a Docker image, while RUN is used to execute a command during the image build process.
4) How Will you reduce the size of the Docker image?
- Reducing the size of a Docker image can be done through techniques such as using multi-stage builds, using Alpine Linux instead of larger base images, and removing unnecessary files and dependencies.
5) Why and when to use Docker?
- Docker is used for packaging, distributing, and running applications in containers. It provides a consistent environment for deployment and eliminates issues with dependencies and configurations.
6) Explain the Docker components and how they interact with each other.
- Docker components include the Docker daemon, the Docker CLI, and the Docker API. They interact by receiving commands from the CLI and API, performing actions on the host system, and communicating with the Docker registry to download and upload images.
7) Explain the terminology: Docker Compose, Docker File, Docker Image, Docker Container?
- Docker Compose is a tool for defining and running multi-container applications. A Docker file is a script used to build a Docker image. A Docker image is a snapshot of a container. A Docker container is a running instance of an image.
8) In what real scenarios have you used Docker?
- I am an AI language model and don't have personal experiences but some scenarios include microservices architecture, continuous integration and delivery, and development environments.
9) Docker vs Hypervisor?
- Docker uses OS-level virtualization, while a hypervisor provides full virtualization and runs multiple VMs on a host. Docker is lighter and faster than a hypervisor.
10) What are the advantages and disadvantages of using docker?
- Advantages of using Docker include consistency in deployment, efficient resource utilization, and faster setup times. Disadvantages include increased security risks and potential compatibility issues.
11) What is a Docker namespace?
- A Docker namespace is a mechanism for isolating the file system, network, and other resources of a container from the host system and other containers.
12) What is a Docker registry?
- A Docker registry is a centralized repository for storing and distributing Docker images.
13) What is an entry point?
- An entry point is the command that is automatically run when a Docker container is started.
14) How to implement CI/CD in Docker?
- CI/CD in Docker can be implemented by using tools like Jenkins, TravisCI, and GitLab to automate the build, test, and deployment processes.
15) Will data on the container be lost when the docker container exits?
- Data in a Docker container will be lost when the container stops or is deleted, unless it is stored in a data volume that is separate from the container file system.
16) What is a Docker swarm?
- A Docker swarm is a native Docker tool for orchestration and cluster management of Docker containers.
17) What are the docker commands for the following:
- view running containers       `docker ps`
- command to run the container under a specific name    `docker run --name [name] [image_name]`
- command to export a docker      `docker save [image_name] > [filename.tar]`
- command to import an already existing docker image        `docker load < [filename.tar]`
- commands to delete a container        `docker rm [container_id]`
- command to remove all stopped containers, unused networks, build caches, and dangling images?    `docker system prune`   
18) What are the common docker practices to reduce the size of Docker Image?
- Common practices to reduce the size of Docker images include using multi-stage builds, using Alpine Linux, removing unnecessary files and dependencies, and compressing files.
