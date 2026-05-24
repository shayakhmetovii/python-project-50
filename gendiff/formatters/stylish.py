def make_indent(depth: int) -> str:
    return ' ' * (depth * 4 - 2)


def make_string(value, depth: int) -> str:
    match value:
        case bool():
            return 'true' if value else 'false'
        case None:
            return 'null'
        case dict():
            indent = make_indent(depth)
            current_indent = indent + (' ' * 6)
            lines = [
                (f'{current_indent}{k}: '
                 f'{make_string(v, depth + 1)}') for k, v in value.items()
                     ]
            result = '\n'.join(lines)
            return f'{{\n{result}\n  {indent}}}'
        case _:
            return str(value)


def rendering_node(node: dict, depth=0) -> str:
    children = node.get('children')
    indent = make_indent(depth)
    key = node.get('key')
    rendered_value = make_string(node.get('value'), depth)
    rendered_value_old = make_string(node.get('old_value'), depth)
    rendered_value_new = make_string(node.get('new_value'), depth)

    match node['type']:
        case 'root':
            lines = [rendering_node(child, depth + 1) for child in children]
            result = '\n'.join(lines)
            return f'{{\n{result}\n}}'
        case 'nested':
            lines = [rendering_node(child, depth + 1) for child in children]
            result = '\n'.join(lines)
            return f"{indent}  {key}: {{\n{result}\n  {indent}}}"
        case 'changed':
            line1 = f"{indent}- {key}: {rendered_value_old}\n"
            line2 = f"{indent}+ {key}: {rendered_value_new}"
            return line1 + line2
        case 'unchanged':
            return f"{indent}  {key}: {rendered_value}"
        case 'removed':
            return f"{indent}- {key}: {rendered_value}"
        case 'added':
            return f"{indent}+ {key}: {rendered_value}"
        case _:
            return ''


def rendering(node: dict):
    return rendering_node(node)
