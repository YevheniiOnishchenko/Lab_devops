## Lab_4
link to repo: `https://hub.docker.com/r/yevheniionishchenko/lab_4/`
link to image django: `https://hub.docker.com/layers/131090302/yevheniionishchenko/lab_4/django/images/sha256-b90b43a57aae6e29188321325271cb2565513ce4a28fd81c7d9136e692cc1ee7?context=explore`
link to image monitoring: `https://hub.docker.com/layers/131094305/yevheniionishchenko/lab_4/monitoring/images/sha256-9012a45401d3f121341d3a5fd41dde8da3af12973656d42aae8fb8f8c6817082?context=explore`
1. Using commands `docker -v`, `docker -h`, `docker run docker/whalesay cowsay Docker is fun`
2. Using commands `docker pull python:3.8-slim`, `docker images`, `docker inspect python:3.8-slim`
3. Using commands `sudo docker build -t yevheniionishchenko/lab_4:django .`, `sudo docker build --file Dockerfile.momitoring -t yevheniionishchenko/lab_4:monitoring .`
4. Using command `docker run -it --name=django --rm -p 8000:8000 yevheniionishchenko/lab_4:django`
5. Using command `udo docker run -it --name=monitoring --rm -v $(pwd)/server.log:/app/server.log yevheniionishchenko/lab_4:monitoring`
6. Using command `udo docker run -it --net=host --name=monitoring --rm -v $(pwd)/server.log:/app/server.log yevheniionishchenko/lab_4:monitoring` because of problem with connection
