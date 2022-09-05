import config
import re


def is_none_or_whitespace(s: str) -> bool:
    return s is None or re.match(r"^\s*$", s)


def get_args_separators() -> str:
    return config.ARGS_SEPARATORS


def get_args_separators_string() -> str:
    result = ''
    separators = get_args_separators()

    for s in separators:
        result += s + ' |'

    return result.removesuffix(' |')


def get_text_args(text: str) -> list:
    return [arg.strip() for arg in
            filter(lambda s: not is_none_or_whitespace(s), re.split(get_args_separators_string(), text))]
