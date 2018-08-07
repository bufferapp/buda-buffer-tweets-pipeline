# buda-buffer-tweets-pipeline

Data pipeline that grabs tweets in real time, publishes them to PubSub, processes the data using Dataflow and saves them to BigQuery.


## Usage

The project consists of two parts, the crawler and the pipeline.

The crawler is a standalone application that uses the Twitter streaming API to pull data from Twitter and publishes it PubSub.
The crawler lives in the `crawler` directory.

Read more about the `crawler` [here](https://github.com/bufferapp/buda-buffer-tweets-pipeline/blob/master/crawler/README):

The pipeline is a Cloud Dataflow job that's designed to run on GCP. Right now it just parses the raw Tweets json and writes it to BigQuery.

The pipeline lives in the `pipeline` directory.

Read more about the `pipeline` [here](https://github.com/bufferapp/buda-buffer-tweets-pipeline/blob/master/pipeline/README):
