from opening_hours.handlers.util.custom_validators import check_days


class BaseSchema:
    """
    Base schema for validation schema.
    """
    __slots__ = ()

    @classmethod
    def get_schema(cls, schema_name: str):
        """
        Returns the schema function
        :param schema_name:
        :return: Schema function
        """
        return getattr(cls, schema_name)


class ValidationSchema(BaseSchema):
    """
    Stores validators to validate request args in POST, PUT, GET, DELETE requests
    """

    @classmethod
    def opening_hours_get_schema(cls):
        """
        Schema declaration to validate a PUT cashier request
        :return:
        """
        return {
            "monday": {"check_with": check_days},
            "tuesday": {"check_with": check_days},
            "wednesday": {"check_with": check_days},
            "thursday": {"check_with": check_days},
            "friday": {"check_with": check_days},
            "saturday": {"check_with": check_days},
            "sunday": {"check_with": check_days},
        }
