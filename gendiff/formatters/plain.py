def make_string(value):
    match value:
        case dict():
            return '[complex value]'
        case bool():
            return "true" if value else "false"
        case None:
            return 'null'
        case int() | float():
            return str(value)
        case _:
            return f"'{value}'"


def rendering_node(node: dict, path='') -> str:
    children = node.get('children')
    key = node.get('key')
    current_path = f"{path}{key}"

    match node['type']:
        case 'root':
            lines = [rendering_node(child, path) for child in children]
            result = "\n".join(filter(bool, lines))
            return result
        case 'nested':
            lines = [
                rendering_node(child, f"{current_path}.") for child in children
            ]
            result = "\n".join(filter(bool, lines))
            return result
        case 'changed':
            rendered_old = make_string(node.get('old_value'))
            rendered_new = make_string(node.get('new_value'))
            return (f"Property '{current_path}' was updated. "
                    f"From {rendered_old} to {rendered_new}")
        case 'removed':
            return f"Property '{current_path}' was removed"
        case 'added':
            rendered = make_string(node.get('value'))
            return f"Property '{current_path}' was added with value: {rendered}"
        case _:
            return ''


def rendering(node: dict):
    return rendering_node(node)
