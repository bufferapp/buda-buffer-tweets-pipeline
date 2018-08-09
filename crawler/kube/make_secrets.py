#!/usr/bin/env python

import os
import base64
import yaml
import click


def load_template():
    return yaml.load(open('kube/crawler.secrets.yaml.template', 'r'))


def assign(template, name, env_name):
    value = os.environ[env_name]
    encoded_value = base64.b64encode(value.encode()).decode()
    template['data'][name] = encoded_value
    return template

def get_template_data_keys(template):
    return [(k, k.upper().replace('-', '_')) for k in template['data'].keys()]

@click.command()
def make_secrets():
    """Convert the crawler.secrets.yaml.template file to a real secrets file"""
    template = load_template()

    assign(template, 'consumer-key', 'CONSUMER_KEY')
    assign(template, 'consumer-secret', 'CONSUMER_SECRET')
    assign(template, 'access-token', 'ACCESS_TOKEN')
    assign(template, 'access-token-secret', 'ACCESS_TOKEN_SECRET')

    click.echo(yaml.dump(template, default_flow_style=False))


if __name__ == '__main__':
    make_secrets()
