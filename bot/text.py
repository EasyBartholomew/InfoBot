import config
import re
from py_linq import Enumerable


def is_none_or_whitespace(s: str) -> bool:
    return s is None or re.match(r"^\s*$", s)


def get_args_separators() -> str:
    return config.ARGS_SEPARATORS


def get_args_separators_string(*separators: str) -> str:
    result = ''

    if separators is None or not separators:
        separators = get_args_separators()

    for s in separators:
        result += s

    return result


def get_text_args(text: str, *separators: str) -> list:
    separators_string = get_args_separators_string(*separators)

    if Enumerable(text).all(lambda c: c not in separators_string):
        return [text]

    args = re.findall(fr'"".+?""|[^{separators_string}]+', text)

    return [re.sub(r'""(.+)""', r'\1', x).strip() for x in filter(lambda s: not is_none_or_whitespace(s), args)]
