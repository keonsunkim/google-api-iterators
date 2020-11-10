# youtube_api.validator_functions.py

"""
Validator functions kept here. I aim to keep all validating functions here so its
easier to manage validators for different use cases.
"""

def validate_youtube_api_parameters(cls, params):
    """
    Parameter validator for a search functions.
    We assume that the Youtube API Class's required/filter/optional parameter rules
    follow the following structure.

    { 'parameter name' : {'required_type' : type, 'values' : [some list of values]} }

    If there are no set of list required for values, then just ommit the value
    key value pair like the following.

    { 'parameter name' : {'required_type' : type } }

    The parameter_values_type_validator function will automatically pass
    value subset checks if there is no given value!

    Also, we assume that parameters passed to the search function, and finally to
    this validator will look like below. The params argument only accept the following
    form.

    { 'parameter name' : [values] }

    """
    required_params_num = len(cls.required_parameters)
    #Exactly one filter parameter is allowed!
    allowed_filter_params_num = 1

    for key, value in params.items():
        if key in cls.required_parameters:
            parameter_values_type_validator(
                                    cls.required_parameters.get(
                                        key
                                    ).get('required_type'),
                                    params_dict = {key : value}
                                    )
            parameter_values_subset_validator(
                                    key,
                                    value,
                                    cls.required_parameters.get(
                                        key
                                    ).get('values', list())
            )
            required_params_num -= 1
        elif key in cls.filter_parameters:
            if allowed_filter_params_num < 1:
                raise ValueError(f"Only one filter parameter is allowed.")
            parameter_values_type_validator(
                                      cls.filter_parameters.get(
                                            key
                                      ).get('required_type'),
                                      params_dict = {key : value}
            )
            parameter_values_subset_validator(
                                      key,
                                      value,
                                      cls.filter_parameters.get(
                                            key
                                      ).get('values', list())
            )
            allowed_filter_params_num -= 1
        elif key in cls.optional_parameters:
            parameter_values_type_validator(
                                    cls.optional_parameters.get(
                                        key
                                    ).get('required_type'),
                                    params_dict = {key : value}
                                    )
            parameter_values_subset_validator(
                                    key,
                                    value,
                                    cls.optional_parameters.get(
                                        key
                                    ).get('values', list())
            )
        else:
            raise ValueError(f"{key} in your parameter is not allowed.")

def parameter_values_type_validator(expected_type, params_dict):
    for key, values in params_dict.items():
        for value in values:
            if value is None:
                pass
            elif isinstance(value, expected_type):
                pass
            else:
                raise ValueError(f"You put {value} in your parameter "\
                                 f"values. However, only values of type "\
                                 f"{expected_type} is legitimate for {key}")

def parameter_values_subset_validator(params_name, target_set, mother_set):
    # First check if there is a mother subset to check for! Pass if empty
    if not mother_set:
        pass
    # Then check if target set is subset
    elif set(target_set).issubset(set(mother_set)):
        pass
    else:
        raise ValueError(f"You put {target_set} as parameter values "\
                         f"for your parameter {params_name}. "\
                         f"Correct values are {mother_set}. ")
