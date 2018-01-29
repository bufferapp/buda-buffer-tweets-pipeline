IMAGE_NAME := bufferapp:twitter-crawler

.DEFAULT_GOAL := run

.PHONY: build
build:
	docker build -t $(IMAGE_NAME) .

.PHONY: run
run: build
	docker run -it --env-file .env -p 8888:8888 -v $(PWD):/work --rm $(IMAGE_NAME)
