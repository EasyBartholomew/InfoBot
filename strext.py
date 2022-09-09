import re


def is_none_or_empty(s: str) -> bool:
    return s is None or not s


def is_none_or_whitespace(s: str) -> bool:
    return s is None or re.match(r"^\s*$", s)
