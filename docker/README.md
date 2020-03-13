### Docker support

Users that do not want to change the configuration or packages installed on their host machine can build and run a docker container using the scripts available in this folder.

Scripts provided
----------------
- Build the image using the `build-docker-image.sh` script
- Run the container using `run-docker-container.sh` available in the root of the project folder (one folder above this one)
- Version control the image via the `version.txt` file (available one folder above this one)
- Push image to docker hub using `push-docker-image-to-hub.sh`

The docker image contains Jupyter lab, the necessary lab extensions, bamboolib and it's dependencies.

Building the docker image
-------------------------
The below command builds the docker image with the necessary dependencies to run bamboolib inside Jupyter lab:

```
$ ./build-docker-image.sh
```

Running the docker container
----------------------------
Works out-of-the-box with the below command, once the image has been built with the above step.

```
$ ./run-docker-container.sh
```

A `notebooks` is created and mounted into the container in order to create your notebooks in there and make it access inside the container while having it saved on the host machine.


[back to main README.md](../README.md)