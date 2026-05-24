from gendiff.formatters import json, plain, stylish


def formatting(ast, format_name='stylish'):
    formats = {
        'stylish': stylish,
        'plain': plain,
        'json': json,
    }
    return formats[format_name](ast)
