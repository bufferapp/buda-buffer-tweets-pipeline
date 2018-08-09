.DEFAULT_GOAL := help

PIP := $(shell command -v pip 2> /dev/null)
PIPENV := $(shell command -v pipenv 2> /dev/null)
GCLOUD := $(shell command -v gcloud 2> /dev/null)

.PHONY: help
help:
	@echo -e "Usage: \tmake [TARGET]\n"
	@echo -e "Targets:"
	@echo -e "  deps            Installs and checks for dependencies (Pipenv, gcloud)"
	@echo -e "  setup           Initialize the dev enviroment, make sure to run this before using make run"
	@echo -e "  run             Execute the pipeline locally"
	@echo -e "  console         Open a IPython console for testing and development"
	@echo -e "  deploy          Deploy the pipline to GCP"

.PHONY: deps
deps:
	@echo "Checking dependencies"
ifndef PIP
    $(error "pip is not available please install it!")
endif
ifndef PIPENV
    $(error "pipenv is not available please install it!")
endif
ifndef GCLOUD
    $(error "The gcloud cli is not available please install it!")
endif
	@echo "All dependencies installed"

.PHONY: setup
setup: deps
	@pipenv install --dev

.PHONY: run
run:
	@pipenv run pipeline --streaming

.PHONY: console
console:
	@pipenv run ipython

.PHONY: deploy
deploy: #this doesn't work yet
	pipenv run pipeline --streaming \
		--job_name buda-buffer-tweets-pipeline \
		--project buffer-data \
		--runner DataflowRunner \
	    --staging_location gs://buffer-data/staging/ \
		--update \
		--temp_location gs://buffer-data/tmp/


