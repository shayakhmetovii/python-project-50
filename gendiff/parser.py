import json
import os

import yaml

from gendiff.parse import parse


def parser(file_path):
    _, ext = os.path.splitext(file_path)
    if ext in ('.yaml', '.yml'):
        format = 'yaml'
    elif ext == '.json':
        format = 'json'
    else:
        raise ValueError(f"Unsupported file extension: {ext}")
    try:
        with open(file_path) as file:
            data = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except IOError as e:
        raise IOError(f"Cannot read file {file_path}: {e}")
    try:
        parsed_data = parse(data, format)
    except (json.JSONDecodeError, yaml.YAMLError) as e:
        raise ValueError(f"Failed to parse {file_path} as {format}: {e}")
    return parsed_data
