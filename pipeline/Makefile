.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo -e "Usage: \tmake [TARGET]\n"
	@echo -e "Targets:"
	@echo -e "  deps            Installs and checks for dependencies (Pipenv)"
	@echo -e "  init            Initialize the Python enviroment, make sure to run this before using make run"
	@echo -e "  run             Execute the pipeline locally"
	@echo -e "  console         Open a IPython console for testing and development"
	@echo -e "  deploy          Deploy the pipline to GCP"

.PHONY: deps
deps:
	@pip install pipenv
	@docker -v

.PHONY: init
init: deps
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


