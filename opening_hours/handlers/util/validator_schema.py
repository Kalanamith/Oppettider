from typing import Dict, Union


class BaseSchema:
    __slots__ = ()

    @classmethod
    def get_schema(cls, schema_name: str):
        return getattr(cls, schema_name)


class ValidationSchema(BaseSchema):
    @classmethod
    def cashier_put_schema(cls) -> Dict[str, Dict[str, Union[str, bool]]]:
        """
        Schema declaration to validate a PUT cashier request
        :return:
        """
        pass
