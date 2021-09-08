# GPIO-FastAPI

## Introduction

While completing my Cloud Native Architecture nanodegree I learned about FastAPI and decided to build an application that uses FastAPI. Here I will show you how I did it and how you can try it yourself.

## Getting Started

### Hardware

* Raspberry Pi 3B+ (But any model will do)
* Three LEDs, three 220 ohm resistors and jumper wires
* 9g servo motor
* My Robot Torvalds (any robot can be used or you can omit this part)

### Software
* Raspberry Pi OS
* FastAPI (I have provided that in the requirements.txt file so all you need to do is run pip install requirements.txt)
* Python 3 


## The Code

* `fastapi_gpio`: The main code that runs the application. To run this you must run the `uvicorn fastapi_gpio:app --reload`
* `templates/gpio.html`: The main code that defines the design of the app
* `static/gpio.css`: The css of the app
* `static/gpio.js`: The jQuery that defines the logic of the application

## Packaging App in Docker

To package this as a docker container, I have provided a `Dockerfile` for use. To use this first install Docker on your machine. Follow [this](https://docs.docker.com/get-docker/) link to install. Set up a DockerHub account so you can implement this on your own. Once you do that run the following commands:

* `docker build -t gpio_fastapi .`: This builds the image
* `docker run -d -p 8000:8000 gpio_fastapi`: This runs docker image detached at port 8000
* `docker ps`: Checks the docker images that have run
* Check `locahost:8000` to see the app run.
* You can stop the image with `docker stop`
* To tag use `docker tag gpio_fastapi yourusername/gpio-fastapi:tag`
* Push with `docker push yourusername/gpio_fastapi:tag`

## Kubernetes Manifests

I have provided kubernetes manifests to run the service. I have provided a service, deployment and namespace. The namespace needs to run first since the deployment and service files require a namespace. Make sure if you are using your own docker image to change the image in the file. Install [k3s](https://k3s.io/) and then deploy with `kubectl apply -f filename.yaml`.

## ArgoCD Helm Charts

To deploy this on ArgoCD first install ArgoCD with [this](https://argoproj.github.io/argo-cd/getting_started/) link. Then follow the instructions to deploy ArgoCD on your own machine. Use the ArgoCD files I have provided to deploy the service. Make sure to use `kubectl apply -f` and then the file name to deploy the service. 
