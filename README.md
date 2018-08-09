# Buffer Tweets Data Pipeline

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains code and resources for the Buffer Tweets Data Pipeline.
The Pipeline grabs tweets in real time and publishes them to PubSub.
Then, the tweets are processed using Google Cloud Dataflow and saved BigQuery.

![Buffer Tweets Pipeline](https://user-images.githubusercontent.com/1682202/43895537-fb295570-9bd5-11e8-91e3-cf8a6b62392d.png)

## Usage

The project consists of two parts, the crawler and the pipeline.

The crawler is a standalone application that uses the Twitter streaming API to pull data from Twitter and publishes it PubSub.
The crawler lives in the `crawler` directory.

Read more about the `crawler` [here](https://github.com/bufferapp/buda-buffer-tweets-pipeline/blob/master/crawler/README):

The pipeline is a Cloud Dataflow job that's designed to run on GCP. Right now it just parses the raw Tweets json and writes it to BigQuery.

The pipeline lives in the `pipeline` directory.

Read more about the `pipeline` [here](https://github.com/bufferapp/buda-buffer-tweets-pipeline/blob/master/pipeline/README):
