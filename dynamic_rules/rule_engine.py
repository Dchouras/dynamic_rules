from dynamic_rules.data_types import NumericType, StringType
from dynamic_rules.rule_processing import applicable_rules
from dynamic_rules.errors import TypeNotSupportedError, DataTypeMismatchError


def evaluate_rules(**kwargs):
    rule_set = applicable_rules(**kwargs)
    if not rule_set:
        print("No matching rules for input eligibility criteria\n")
        return
    for rule in rule_set:
        print("Evaluating rule")
        conditions_obj = rule.get("conditions")
        if _eval_conditions(conditions_obj, **kwargs):
            return rule["outcome"]


def _eval_conditions(conditions_obj, **kwargs):
    if "operator" in conditions_obj:
        return _eval_leaf_condition(conditions_obj, **kwargs)
    elif "any" in conditions_obj:
        conditions = conditions_obj["any"]
        for condition in conditions:
            if _eval_conditions(condition, **kwargs):
                return True
        return False
    elif "all" in conditions_obj:
        conditions = conditions_obj["all"]
        for condition in conditions:
            if not _eval_conditions(condition, **kwargs):
                return False
        return True


def _eval_leaf_condition(conditions_obj, **kwargs):
    label, operator, value = conditions_obj["label"], conditions_obj["operator"], conditions_obj["value"]

    # from the name in rule and same variable passed in the input, compare and validate the data-types
    # translate operator to numeric or string operation
    data_object = _determine_data_object(kwargs[label], value)
    # do the operator comparison
    return data_object.OPERATOR_MAP[operator](data_object)


def _determine_data_object(input_val, rule_val):
    if type(input_val) != type(rule_val):
        raise DataTypeMismatchError(
            f"Data type mismatch, input type - {type(input_val)} vs rule type - {type(rule_val)}"
        )
    if isinstance(input_val, int):
        return NumericType(input_val, rule_val)
    elif isinstance(input_val, str):
        return StringType(input_val, rule_val)
    else:
        raise TypeNotSupportedError
