import sys
import json
from apache_beam.io.gcp.internal.clients import bigquery

def _get_field_schema(**kwargs):
    field_schema = bigquery.TableFieldSchema()
    field_schema.name = kwargs['name']
    field_schema.type = kwargs.get('type', 'STRING')
    field_schema.mode = kwargs.get('mode', 'NULLABLE')
    fields = kwargs.get('fields')
    if fields:
        for field in fields:
            field_schema.fields.append(_get_field_schema(**field))
    return field_schema


def _inject_fields(fields, table_schema):
    for field in fields:
        table_schema.fields.append(_get_field_schema(**field))


def _parse_bq_json_schema(schema):
    table_schema = bigquery.TableSchema()
    _inject_fields(schema, table_schema)
    return table_schema

def get_schema(json_data):
    json_schema = json.load(json_data)
    return _parse_bq_json_schema(json_schema)
