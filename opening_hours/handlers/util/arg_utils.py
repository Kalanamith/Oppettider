__doc__ = """ Utility functions to use in views """

import re
from typing import Dict, Union


def convert(param: str) -> str:
    """
    Reference :- https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case

    Converts camel / pascal case to snake case
    :param param:
    :return:
        - snake_case str
    """
    s1: str = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", param)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def prepare_data(args: Dict) -> Dict[str, Union[bool, int, str]]:
    """
    Construct a dictionary with snake_case keys from args
    :param args:
    :return: Dict[str, Union[bool, int, str]]
    """
    if type(args) is not dict:
        return {}

    params: Dict[str, Union[bool, int, str]] = {convert(key): value for key, value in args.items()}

    return params
