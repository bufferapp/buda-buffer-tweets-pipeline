.DEFAULT_GOAL := help

IMAGE_NAME := buda-buffer-tweets-pipeline-crawler
GCP_PROJECT=buffer-data
GKE_CLUSTER=apollo
COMPUTE_ZONE=us-central1-a

PIP := $(shell command -v pip 2> /dev/null)
PIPENV := $(shell command -v pipenv 2> /dev/null)
DOCKER := $(shell command -v docker 2> /dev/null)
GCLOUD := $(shell command -v gcloud 2> /dev/null)

.PHONY: help
help:
	@echo -e "Usage: \tmake [TARGET]\n"
	@echo -e "Targets:"
	@echo -e "  deps            Installs and checks for dependencies (Pipenv)"
	@echo -e "  setup           Initialize the dev enviroment, make sure to run this before using make run"
	@echo -e "  run             Execute the crawler locally"
	@echo -e "  console         Open a IPython console for testing and development"
	@echo -e "  patch           Bump the VERSION file to a new patch version"
	@echo -e "  minor           Bump the VERSION file to a new minor version"
	@echo -e "  major           Bump the VERSION file to a new major version"
	@echo -e "  image           Build crawler Docker images"
	@echo -e "  rund            Execute the crawler in a Docker container"
	@echo -e "  push            Push crawler Docker image to the registry"
	@echo -e "  deploy          Deploy the crawler to Kubernetes"
	@echo -e "  logs            Display the logs of the running Kubernetes application"


.PHONY: deps
deps:
	@echo "Checking dependencies"
ifndef PIP
    $(error "pip is not available please install it!")
endif
ifndef PIPENV
    $(error "pipenv is not available please install it!")
endif
ifndef DOCKER
    $(error "Docker is not available please install it!")
endif
ifndef GCLOUD
    $(error "The gcloud cli is not available please install it!")
endif
	@echo "All dependencies installed"

.PHONY: setup
setup: deps
	@pipenv install --dev
	@gcloud auth configure-docker

.PHONY: run
run:
	@pipenv run crawler

.PHONY: console
console:
	@pipenv run ipython

.PHONY: image
image:
	@docker build -t $(IMAGE_NAME):latest .

.PHONY: patch
patch:
	@docker run --rm -v "$(PWD)":/app treeder/bump patch
	@version=`cat VERSION`

.PHONY: run-image
run-image: image
	docker run --env-file .env -v ~/.config/gcloud:/root/.config/gcloud --rm $(IMAGE_NAME)


.PHONY: secrets
secrets:
	@pipenv run ./kube/make_secrets.py | kubectl apply -f -

.PHONY: deploy
deploy:
	@gcloud builds submit --config cloudbuild.yaml . \
		--substitutions=_IMAGE_NAME=$(IMAGE_NAME),_VERSION=$(shell cat VERSION),_CLUSTER=$(GKE_CLUSTER),_COMPUTE_ZONE=$(COMPUTE_ZONE)

.PHONY: logs
logs:
	@echo TODO
