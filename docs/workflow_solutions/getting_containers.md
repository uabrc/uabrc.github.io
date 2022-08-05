# Software Containers

Containers helps to manage software installations and all its dependencies in a single large image.

Docker is an open source plaform to build, deploy, run, update, and manage containers.

## Fantastic Containers and Where to Find Them

Docker containers are available in <https://hub.docker.com/>. This docker hub repository allows to share containers and use pre-existing docker images.

![!Docker hub webiste.](./images/docker_hub_website.png)

## Using Containers on UAB RC Cloud (cloud.rc)

To access docker containers, install `Docker` in your system. To install docker desktop on your computer follow this link: [Docker Desktop Page](https://www.docker.com/products/docker-desktop/).

### Installation

Following are the installation instructions to install `Docker` on UAB RC Coud with Ubuntu operating system. The installation was tested on Ubuntu 20.04.

```bash
sudo apt-get update
sudo apt install docker.io
```

### Use existing Docker

We can start with pulling an sample container named `Alpine`. Search for the docker container `Alpine` in docker hub, copy the pull command, and paste it in your terminal.

![!Pull docker from dockerhub.](./images/pull_docker_from_dockerhub.png)

```bash
sudo docker pull alpine
```

![!Docker pull alpine.](./images/docker_pull_alpine.png)

<!--  ## Create your own Docker container -->
<!--  ## Fetching particular version of docker container (testing) -->

<!-- Hyperlink [test](using_anaconda.md)-->

If there exist no direct pull command for a particular version of container, you may create your own `Dockerfile` and build it.

Here is an example to build `Alpine` or fetch the Dockerfile content from Dockerhub or any other repositories like Github, Gitlab, etc.

1. Create a directory `alpine`.

    ```bash
    mkdir alpine
    ```

2. Create a `Dockerfile` witin the `alpine` directory. The file name `Dockerfile` is case sensitive.

3. Fetch the Dockerfile content of a desired version of `Alpine`.

![!Dockerfile links alpine.](./images/dockerfile_links_alpine.png)

Clicking any one of the Dockerfile links redirects to the Dockerfile content page, and copy this content, and paste in  `alpine/Dockerfile`.

![!Alpine dockerfile.](./images/alpine_dockerfile.png)

To build Alpine docker container, use the below syntax.

```bash
$sudo docker build -t repository_name:tag .
```

Here the given repository_name is `alpine`, and the tag is `latest`.

```bash
$sudo docker build -t alpine:latest .
```

This may lead to an error `alpine-minirootfs-3.16.0-x86_64.tar.gz file not found`. You can download the repo within `alpine` directory from the github repo where you fetched the Dockerfile content, and build again.

![!Build alpine error.](./images/build_alpine_error.png)

![!Alpine dependnecy fix.](./images/alpine_dependency_fix.png)

![!Alpine directory.](./images/alpine_directory.png)

![!Alpine successful build.](./images/alpine_successful_build.png)

Once the built is successful. You can verify if the image exists.

![!Alpine image.](./images/alpine_image.png)

## Sharing containers using UAB GitLab Container Registry

To Create container registry in Gitlab, following are the requirements: <!-- cross reference for Gitlab account -->

<!-- (i) Create an Gitlab account with UAB email ID

(ii) Create a new_project in Gitlab

(iii) Create an access token in gitlab to push/pull the docker container in the container registry (Secure token, and guidelines to follow are below)  -->

### Create New Project

Create a new project in Gitlab. Once you create the `new_project` -> Click Package and Registries -> Click Container Registry.  

Initially the container registry looks empty.  

![!Container registry.](./images/container_registry.png)

Initially there exists no container images in the container registry. Note, copy this CLI commands for future reference. This contains commands (1) to login to your project gitlab container registry (2) Add an image to the registry using push/build command. We will use `push` command as we have the existing container in our system already.  

### Push Alpine Container from Ubuntu system to Gitlab container registry

Here is an example of pushing `alpine` image to container registry from your ubuntu system.  

List the docker images using the below command. Here `alpine` image exists already, and we will learn how to push this image to gitlab container registry. 

```bash
sudo docker images
```

![!Docker image.](./images/docker_image.png)

## Tag alpine to push in Gitlab registry

We need to have gitlab registry name to push. It will show the default command in the container registry page. Copy these commands for future reference. Tag is `test` here.

```bash
$sudo docker tag alpine:latest gitlab.rc.uab.edu:4567/rc-data-science/build-and-push-container/alpinegitlab:test
```

You can see the tag `test` associated with the `alpine` image,  

```bash
sudo docker images
```

![!Docker test image.](./images/docker_test_image.png)

## Login to gitlab registry

Use your registry name:ID to login to gitlab registry.

```bash
sudo docker login gitlab.rc.uab.edu:4567
```

Note: For securing concern use access token to login. Creating access token is shown below.

```bash
sudo docker login gitlab.rc.uab.edu:4567 -u username –p access_token 
```

### Create an Access token

From the gitlab page you can create an access token instead of using password to login to gitlab registry. Goto Edit profile -> Click `Access Tokens`. Then enter, 1.Token name 2. Expiry date 3. Under select scopes, check read and write registry  (to push images to registry) -> Then click `create personal access token`.

Once you create the token. Copy the new personal access token, since it’s a one-time step, and hard to retrieve after a refresh. Use the personal access token for login.

![!Create access token.](./images/create_access_token.png)

![!Personal access token.](./images/personal_access_token.png)

![!Gitlab login success.](./images/gitlab_login_success.png)

## To push docker container in gitlab registry

The below first command is the command to push docker image to gitlab container registry. The second command is an example of pushing docker image to gitlab container registry.

```bash
sudo docker push gitlab_registry_name:ID/gitlab_group_name/project_name:tag

sudo docker push gitlab.rc.uab.edu:4567/rc-data-science/build-and-push-container/alpinegitlab:test
```

![!Docker push gitlab.](./images/docker_push_gitlab.png)

![!Alpine gitlab.](./images/alpine_gitlab.png)

Removing the previous image from the system which has `test` tag already to avoid discrepancies.

```bash
sudo docker rmi -f 5274064a8e18
```

![!Docker rmi.](./images/docker_rmi.png)

![!Test gitlab registry.](./images/test_gitlab_registry.png)

 Copy the pull command from the `test` container registry, and use it to pull the docker container to your system. You can see the image is reflected in the image list.

```bash
sudo docker pull gitlab.rc.uab.edu:4567/rc-data-science/build-and-push-container/alpinegitlab:test 
```

![!Gitlab pull.](./images/gitlab_pull.png)

<!-- Sharing containers public<https://rc.uab.edu> -->