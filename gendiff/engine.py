from gendiff.ast import build_ast
from gendiff.formatter import formatting
from gendiff.parser import parser


def generate_diff(file_path1, file_path2, format_name='stylish') -> str:
    if format_name not in ('stylish', 'plain', 'json'):
        raise ValueError(f"Unsupported format: {format_name}")
    try:
        file1 = parser(file_path1)
        file2 = parser(file_path2)
    except (FileNotFoundError, IOError, ValueError) as e:
        raise e
    ast = build_ast(file1, file2)
    rendered = formatting(ast, format_name)
    return rendered
