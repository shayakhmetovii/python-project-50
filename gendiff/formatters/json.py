import json


def rendering(ast: list) -> json:
    return json.dumps(ast, indent=4)
