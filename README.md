# docker-practice
practicing containerization of python applications uisng docker

1. writing in Dockerfile
2. To build the Docker Image `docker build -t docker-practice .`
3. To run the image `docker run --name docker-practice-container -p 80:80 docker-practice`
4. `-d` tag for running in detached mode
5. `docker ps -a` for listing the running containers
6. `docker rm <container_id>` to remove a container
7. `docker rmi <image_id>` to remove an image 