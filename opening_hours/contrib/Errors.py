__doc__ = """ Definition of Errors """

from enum import Enum
from typing import Dict


class Errors(Enum):
    """
    Generic errors to use in handlers and models
    """
    SAVE_ERROR = "SAVE_ERROR"
    UPDATE_ERROR = "UPDATE_ERROR"
    DELETE_ERROR = "DELETE_ERROR"
    ERROR = "ERROR"


DATA_ERRORS: Dict[str, Dict[str, str]] = {
    """
    Generic Error messages
    """
    "SAVE_ERROR": {"SAVE_ERROR": "Error in data"},
    "UPDATE_ERROR": {"UPDATE_ERROR": "Error in data"},
    "DELETE_ERROR": {"DELETE_ERROR": "Error in data"},
    "ERROR": {"ERROR": "Error"},
}
