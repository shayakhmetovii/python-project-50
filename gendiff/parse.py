import json

import yaml


def parse(data, format):
    if format == 'yaml':
        return yaml.safe_load(data)
    if format == 'json':
        return json.loads(data)
