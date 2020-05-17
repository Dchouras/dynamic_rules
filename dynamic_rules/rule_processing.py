import json
import hashlib


RULE_SET = dict()


def load_rules(file_location):
    with open(file_location, 'r') as f:
        rules_dict = json.load(f)

    rules = rules_dict.get('rules', []) if rules_dict else []

    for rule in rules:
        name_list = []
        _get_attribute_list(rule.get("conditions", {}), name_list)
        names = ",".join(sorted(set(name_list)))
        rule_hash = _calculate_hash(names)
        if RULE_SET.get(rule_hash):
            RULE_SET[rule_hash].append(rule)
        else:
            RULE_SET[rule_hash] = [rule]


def applicable_rules(**kwargs):
    rule_hash = _calculate_hash(",".join(sorted(list(kwargs.keys()))))
    return RULE_SET.get(rule_hash)


def _calculate_hash(input_string):
    hash_object = hashlib.md5(input_string.encode())
    return hash_object.hexdigest()


def _get_attribute_list(rule_dict, name_list):
    if "operator" in rule_dict:
        name_list.append(rule_dict.get("label"))
    elif "all" in rule_dict or "any" in rule_dict:
        rule_value = list(rule_dict.values())[0] if rule_dict.values() else []
        for value in rule_value:
            _get_attribute_list(value, name_list)
