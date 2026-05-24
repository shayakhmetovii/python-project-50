import pytest

from gendiff import generate_diff


def load_expected_result(path):
    with open(path) as file:
        return file.read().strip()


@pytest.mark.parametrize(
    "first_file, second_file, expected",
    [
        ("tests/fixtures/file1.json", "tests/fixtures/file2.json",
         load_expected_result("tests/fixtures/simple_result.txt")),
        ("tests/fixtures/file1.yml", "tests/fixtures/file2.yml",
         load_expected_result("tests/fixtures/simple_result.txt")),
        ("tests/fixtures/recursive1.json", "tests/fixtures/recursive2.json",
         load_expected_result("tests/fixtures/stylish_result.txt")),
        ("tests/fixtures/recursive1.yml", "tests/fixtures/recursive2.yml",
         load_expected_result("tests/fixtures/stylish_result.txt")),
    ]
)
def test_generate_diff_stylish(first_file, second_file, expected):
    assert generate_diff(first_file, second_file, "stylish") == expected


@pytest.mark.parametrize(
    "first_file, second_file, expected",
    [
        ("tests/fixtures/recursive1.json", "tests/fixtures/recursive2.json",
         load_expected_result("tests/fixtures/plain_result.txt")),
        ("tests/fixtures/recursive1.yml", "tests/fixtures/recursive2.yml",
         load_expected_result("tests/fixtures/plain_result.txt")),
    ]
)
def test_generate_diff_plain(first_file, second_file, expected):
    assert generate_diff(first_file, second_file, "plain") == expected


@pytest.mark.parametrize(
    "first_file, second_file, expected",
    [
        ("tests/fixtures/recursive1.json", "tests/fixtures/recursive2.json",
         load_expected_result("tests/fixtures/json_result.txt")),
        ("tests/fixtures/recursive1.yml", "tests/fixtures/recursive2.yml",
         load_expected_result("tests/fixtures/json_result.txt")),
    ]
)
def test_generate_diff_json(first_file, second_file, expected):
    assert generate_diff(first_file, second_file, "json") == expected
