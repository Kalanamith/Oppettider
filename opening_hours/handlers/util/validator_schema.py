from typing import Dict, Union


class BaseSchema:
    """
    Base schema for validation schema.
    """
    __slots__ = ()

    @classmethod
    def get_schema(cls, schema_name: str):
        return getattr(cls, schema_name)


class ValidationSchema(BaseSchema):
    """
    Stores validators to validate request args in POST, PUT, GET, DELETE requests
    """
    @classmethod
    def cashier_put_schema(cls) -> Dict[str, Dict[str, Union[str, bool]]]:
        """
        Schema declaration to validate a PUT cashier request
        :return:
        """
        pass
