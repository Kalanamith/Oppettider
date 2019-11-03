def check_days(field, value, error):
    if type(value) is not list:
        error(field, "Must be a list.")

    if len(value) > 0:
        for item in value:
            if type(item) is not dict:
                error(item, "Must be a dictionary.")

            dict_keys = item.keys()

            results = all(elem in dict_keys for elem in ["type", "value"])

            if not results:
                error("Invalid entries.")

            if type(item["type"]) is not str:
                error("type must be string.")

            if item["type"] not in ["open", "close"]:
                error("type must be either open or close.")

            if type(item["value"]) is not int:
                error("value must be an integer.")

            if item["value"] <= 0:
                error("value must be greater than 0.")
