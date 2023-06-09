# docker-practice
practicing containerization of python applications uisng docker

## WITH OUT DOCKER-COMPOSE
1. writing in Dockerfile
2. To build the Docker Image `docker build -t docker-practice .`
3. To run the image `docker run --name docker-practice-container -p 80:80 docker-practice`
4. `docker run --name docker-practice-container -p 80:80 -d docker-practice`
5. `docker run --name docker-practice-container -p 80:80 -d -v $(pwd):/code docker-practice` code changes to effect inside container use volume tage `-v`
6. `-d` tag for running in detached mode
7. `docker ps -a` for listing the running containers
8. `docker rm <container_id>` to remove a container
9.  `docker rmi <image_id>` to remove an image

## DOCKER COMPOSE
1. `docker-compose up`
2. `docker-compose up -d` for detached mode
3. `docker-compose up --build` to rebuild the app service
4. in the app service user this after --ports for enabling ipdb debugging tool
    * ` stdin_open: true`
    * `tty: true`
    * and then in a new terminal window `docker attach <container_name or container_id>` for interacting with ipdb debugging tool