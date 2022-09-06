# Software Containers

Containers help to manage software installations and all their dependencies in a single large image.

Docker is an open-source platform for building, deploying, running, updating, and managing containers.

## Fantastic Containers and Where to Find Them

Docker containers are available in <https://hub.docker.com/>. This docker hub repository allows to share containers and use pre-existing docker images.

![!Containers docker hub website.](./images/containers_docker_hub_website.png)

## Using Containers on UAB RC Cloud (cloud.rc.uab.edu)

To access docker containers, install `Docker` in your system. To install docker desktop on your computer, follow this link: [Docker Desktop Page](https://www.docker.com/products/docker-desktop/).

### Docker Installation on UAB RC Cloud

Following are the installation instructions to install `Docker` on UAB RC Cloud with Ubuntu operating system. Tested the installation on Ubuntu 20.04. Setting up UAB RC Cloud account can be found in [UAB RC Cloud](../uab_cloud/introduction.md).

```bash
sudo apt-get update
sudo apt install docker.io
```

### Using a Docker Container from DockerHub

We can start pulling a container named `alpine` from the Docker hub. `alpine` is a general-purpose Linux distribution. Look for the container `alpine` in the docker hub, copy the pull command, and paste it into your terminal.

![!Containers pull docker from dockerhub.](./images/containers_pull_docker_from_dockerhub.png)

```bash
sudo docker pull alpine
```

![!Containers docker pull alpine.](./images/containers_docker_pull_alpine.png)

Once the image is pulled, you can verify if the image exists using the below command. Note that if you do not specify the tag/version of the container, the recent version is built, and the tag is listed as `latest`.

```bash
sudo docker images
```

![!Containers alpine image.](./images/containers_alpine_image.png)

If you prefer to pull a particular version of the `alpine` container, you need to mention the tag details in your pull command. You can see the available tags/versions of `alpine` from the Docker hub.

![!Containers dockerfile links alpine.](./images/containers_dockerfile_links_alpine.png)

To pull particular version of `alpine` container, use the below syntax.

```bash
sudo docker pull container_name:tag
```

Here the container_name is `alpine`, and the tag is `3.14`.

```bash
sudo docker pull alpine:3.14
```

The existing image looks like,

![!Containers docker alpine tag image.](./images/containers_docker_alpine_tag_image.png)

## Create Your Own Docker Container

You can create your own Docker container, build it, and upload/share them in the Docker hub or UAB GitLab container registry.

Let us take a synthetic python code and formulate the packages/dependencies required to build your software container. Below is a python script that requires packages, namely, numpy, scipy, and matplotlib. Next, the steps to create a `Dockerfile` is illustrated. Let us name this script `python_test.py`.

```bash
import numpy as np
import matplotlib
import pylab
import matplotlib.pylab as plt
import scipy.integrate as integrate

a = np.array([0, 10, 20, 30, 40])
print(a)

b = np.arange(-5, 5, 0.5)
print(b)

t = np.arange(0,20.5,0.5)
print(t)

result = integrate.quad(np.sin, 0, np.pi)
print(result)

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()
plt.savefig('testing.png')
```

### Create a Dockerfile that Has Miniconda Installed

We require numpy, scipy, and matplotlib libraries to execute the above Python script. Following are the steps to create a specification file and build a container image.

1. Create an empty directory `miniconda`.
2. Create a `Dockerfile` within the `miniconda` directory with the following contents. The file name `Dockerfile` is case-sensitive.

    ```bash
    # You may start with a base image
    # Always use a specific tag like "4.10.3", never "latest"!
    # The version referenced by "latest" can change, so the build will be 
    # more stable when building from a specific version tag. 
    FROM continuumio/miniconda3:4.12.0

    #Use RUN to execute commands inside the miniconda image
    RUN conda install -y numpy

    #RUN multiple commands together
    #Last two lines are cleaning out the local repository and removing the state information for installed package
    RUN apt-get update \
    && conda install -y scipy \
    && conda install -y matplotlib \
    && apt-get --yes clean \
    && rm -rf /var/lib/apt/lists/*
    ```

    This is the specification file. It provides Docker with the software information it needs to build our new container. See the Docker Container documentation for more information <https://docs.docker.com/engine/reference/builder/>.

!!! note "Containers and Reproducibiliy"
    Always include version numbers for Anaconda, package managers, software you are installing, and the dependencies for those software. Containers are not by nature scientifically reproducible, but if you include versions for as much software in the container as possible, they can be reproducible years later.

1. We start with an existing container `continuumio/miniconda3:4.12.0`. This container is obtained from Dockerhub; here, `continuumio` is the producer, and the repo name is `continuumio/miniconda3`. You may specify the required version from the `Tag` list. Here the tag/version is `4.12.0`.

    ![!Containers dockerhub miniconda.](./images/containers_dockerhub_miniconda.png)

2. To build your container, change the directory to `miniconda` and use the below syntax to build the `Dockerfile`. Here we use `.` to say "current directory." This will only work if you are in the directory with the `Dockerfile`.

    ```bash
    sudo docker build -t repository_name:tag .
    ```

3. Here the repository_name is `py3-miniconda` and the tag is `2022-08`.

    ```bash
    cd miniconda
    sudo docker build -t py3-miniconda:2022-08 .
    ```

!!! note
    The `.` at the end of the command! This indicates that we're using the current directory as our build environment, including the Dockerfile inside. Also, you may rename the `repository_name` and `tag` as you prefer.

```bash
sudo docker images
```

![!Containers miniconda docker image.](./images/containers_miniconda_docker_image.png)

### Running the Built Docker Container Interactively

To run docker interactively and execute commands inside the container, use the below syntax. Here `run` executes the command in a new container, and `-it` starts an interactive shell inside the container. After executing this command, the command prompt will change and move into the bash shell.

```bash
sudo docker run -it repository_name:tag /bin/bash
```

To execute your container `py3-miniconda` interactively, run this command with the tag `2022-08'.

```bash
sudo docker run -it py3-miniconda:2022-08 /bin/bash
cd /opt/conda/bin/
```

The `python` executables to execute our synthetic python script are within the directory structure `/opt/conda/bin`.

![!Docker interactive.](./images/containers_docker_interactive.png)

![!Python executable.](./images/containers_python_executable.png)

Remember you initially created the python script `python_test.py` when creating your own container. Move `python_test.py` within `miniconda` directory. Now you have your `miniconda/python_test.py` outside the container. To access the files outside the container you should mount the file path along with the `docker run` command.

### Mounting Data Onto a Container

To mount a host directory into your docker container, use the `-v` flag.

```bash
sudo docker run -v /host/directory/:/container/directory  -other-options
```

So the command for our example will be,

```bash
sudo docker run -v /home/ubuntu/:/home  -it py3-miniconda:2022-08 /bin/sh
```

Here we are mounting the $HOME directory `/home/ubuntu` from a host into containers' $HOME directory. Note that you may mount a particular directory according to your preference. The following shows the list of files in containers' $HOME directory with and without mounting.

Before mounting, there are no files found within the $HOME directory.

![!Containers before mounting.](./images/containers_before_mounting.png)

After mounting using `-v` flag, files show up within the $HOME directory. The highlighted `miniconda` is our working directory with python script.

![!Containers after mounting.](./images/containers_after_mounting.png)

We can now execute the script, python_test.py using this command.

```bash
python python_test.py
```

![!Containers python script execution.](./images/containers_python_script_execution.png)

More lessons on Docker can be found in this link: [Introduction to Docker](https://christinalk.github.io/docker-introduction/) and [Docker Documentation](https://docs.docker.com/engine/reference/builder/).

## Sharing Containers Using UAB GitLab Container Registry

If you prefer to share your container with a particular team/group, then the UAB GitLab container registry is the best and most secure option.

The following steps help you to create a container registry in UAB GitLab:

1. Create a UAB Gitlab account following the guidelines from the [UAB Gitlab page](../../docs/account_management/gitlab_account.md).
2. Create a `new_project` on UAB GitLab and click `Package and Registries`, and then go to Container Registry. Initially, the container registry looks empty because there are no container images in the registry.  

    ![!Containers registry.](./images/containers_registry.png)

    !!! note
        Copy these CLI commands for future reference. It contains commands (1) to login to your project UAB GitLab container registry (2) Add an image to the registry using the push/build command. We will use the `push` command as we already have the existing container in our system.  

3. Push Alpine Container from Ubuntu system to UAB GitLab container registry.

???+ example "Pushing an `alpine` image to the UAB GitLab container registry from an Ubuntu Linux computer"

- List the docker images on your local computer using the `docker images` command. An `alpine` image exists already on this computer. Your container will likely have a different name.
  
```bash
sudo docker images
```

![!Containers docker image.](./images/containers_docker_image.png)

- Tag `alpine` to push in UAB GitLab registry. We need to have the UAB GitLab registry name to push. It will show the default command on the container registry page. Copy these commands for future reference. The tag is `test` here.

```bash
$sudo docker tag alpine:latest gitlab.rc.uab.edu:4567/rc-data-science/build-and-push-container/alpinegitlab:test
```

You can see the tag `test` associated with the `alpine` image.  

```bash
sudo docker images
```

![!Containers docker test image.](./images/containers_docker_test_image.png)

## Login to UAB GitLab Registry

Use your `registry_name:ID` to log in to the UAB GitLab registry.

```bash
sudo docker login gitlab.rc.uab.edu:4567
```

Note: For securing concerns, use an access token to log in. Create an access token in UAB GitLab to push/pull the docker container in the container registry (Secure token and guidelines to follow are shown next).

```bash
sudo docker login gitlab.rc.uab.edu:4567 -u username –p access_token 
```

### Create an Access Token

From the UAB GitLab page, you can create an access token instead of using a password to log in to the UAB GitLab registry. Goto Edit profile -> Click `Access Tokens`. Then enter:

   1. **Token name.** Suggestion: "container"_"repository-name"
   2. **Expiry date.** Suggestion: 3 months from the date you are making it.
   3. Under select scopes, check read and write registry  (to push images to the registry) -> Then click `create personal access token`.

Once you create the token, copy the new personal access token since it’s a one-time step and hard to retrieve after a refresh. Use the personal access token for login.

![!Containers create access token.](./images/containers_create_access_token.png)

![!Containers personal access token.](./images/containers_personal_access_token.png)

![!Containers gitlab login success.](./images/containers_gitlab_login_success.png)

#### To Push Docker Container into UAB GitLab Registry

The below first command is the command to push the Docker image to the UAB GitLab container registry. The second command is an example of pushing a Docker image to the UAB GitLab container registry.

```bash
sudo docker push gitlab_registry_name:ID/gitlab_group_name/project_name:tag

sudo docker push gitlab.rc.uab.edu:4567/rc-data-science/build-and-push-container/alpinegitlab:test
```

![!Containers docker push gitlab.](./images/containers_docker_push_gitlab.png)

![!Containers alpine gitlab.](./images/containers_alpine_gitlab.png)

Remove the previous image from the system, which already has a `test` tag, to avoid discrepancies.

```bash
sudo docker rmi -f 5274064a8e18
```

![!Containers docker rmi.](./images/containers_docker_rmi.png)

![!Containers test gitlab registry.](./images/containers_test_gitlab_registry.png)

 Copy the pull command from the `test` container registry, and use it to pull the docker container to your system. You can see the image is reflected in the image list.

```bash
sudo docker pull gitlab.rc.uab.edu:4567/rc-data-science/build-and-push-container/alpinegitlab:test 
```

![!Containers gitlab pull.](./images/containers_gitlab_pull.png)
