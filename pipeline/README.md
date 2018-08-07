# buda-buffer-tweets-pipeline pipeline

The pipeline is a streaming Cloud Dataflow job that reads messages from PubSub, processes them and writes the data to BigQuery.

## Setup

Since Cloud Dataflow only supports Python2 the pipeline is a Python 2 application. We use pipenv to manage dependencies.

To get started and run the pipeline locally:

```
make setup
```

## Usage

To run the pipeline locally:

```
make run
```
