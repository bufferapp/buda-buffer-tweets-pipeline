from __future__ import absolute_import

import argparse
import logging
import pkg_resources

import apache_beam as beam
from apache_beam.io import ReadFromPubSub
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.options.pipeline_options import StandardOptions
from pipeline.parse_bq_json_schema import get_schema
from apache_beam.io import BigQueryDisposition as bqd

PUBSUB_TOPIC = 'projects/buffer-data/topics/buffer-tweets'


def run(argv=None):
    parser = argparse.ArgumentParser()
    known_args, pipeline_args = parser.parse_known_args(argv)
    pipeline_options = PipelineOptions(pipeline_args)
    pipeline_options.view_as(SetupOptions).save_main_session = True
    pipeline_options.view_as(StandardOptions).streaming = True

    with pkg_resources.resource_stream(__name__, 'tweets_schema.json') as json:
        schema = get_schema(json)

    def parse_pubsub(line):
        import json
        return json.loads(line)

    with beam.Pipeline(argv=pipeline_args) as p:
        (p | 'Read from PubSub' >> ReadFromPubSub(topic=PUBSUB_TOPIC)
           | 'Parse Json' >> beam.Map(parse_pubsub)
           | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
                'buffer-data:buda.buffer_tweets',
                project='buffer-data',
                schema=schema,
                create_disposition=bqd.CREATE_IF_NEEDED,
                write_disposition=bqd.WRITE_APPEND
             )
         )


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()
