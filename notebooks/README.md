# Notebooks

This folder contains Notebooks related with the pipeline that act as small tutorials.

## Requisistes

- [Docker](https://www.docker.com/) installed and running
- A set of [Twitter App Credentials](https://apps.twitter.com/)
- Acccess to your [AWS IAM User Account](https://aws.amazon.com/iam/)

## Quick Start

Before running the notebooks you'll need to create a `.env` file in this folder with the following environment variables:

- `ACCESS_TOKEN` from your Twitter App
- `ACCESS_TOKEN_SECRET` from your Twitter App
- `CONSUMER_KEY` from your Twitter App
- `CONSUMER_SECRET` from your Twitter App
- `AWS_DEFAULT_REGION` of your AWS Account
- `AWS_ACCESS_KEY_ID` of your IAM Account
- `AWS_SECRET_ACCESS_KEY` of your IAM Account

The easiest way to play with the Notebooks is running `make`.
This will spawn a Jupyter Server locally at [`http://0.0.0.0:8888/`](http://0.0.0.0:8888/). Enjoy!