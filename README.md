# dynamic_rules
This python based rule engine allows developers to define and evaluate rules dynamically.
Introducing new rules or conditions would not need any updates to the source code.

Performance

# Runbook

## 1. Define Rules

```json
{
      "conditions": {
        "any": [
          {
            "label": "num_of_cart_items",
            "operator": "lt",
            "value": 5
          },
          {
            "label": "business_category",
            "operator": "eq",
            "value": "PLAH"
          }
        ]
      },
      "tags": [],
      "outcome": {
        "data": {
          "products": [],
          "product_plans": []
        },
        "actions": [
          {
            "event_type": "AWS IoT",
            "event_data": {}
          }
        ]
      }
    }
``` 
There are 3 basic elements in the rule definition:
* __conditions__: This key consist of one or more JSON objects with fields -- `label, operator and value`, 
each evaluating to a boolean values. Multiple objects could be combined with `any (equivalent of OR)` or `all (equivalent of AND)` logical operators

* __outcome__: This key captures the data or any actions that needs to returned or triggered once a given rule evaluates to be `true`.
* __tags__: This key captures any additional attributes applicable to the rules, mostly relevant to filter applicable rules for a given evaluation request.

## 2. Evaluate Rules
```python
from dynamic_rules import load_rules, evaluate_rules
load_rules("your/rules/location")
evaluate_rules(param_1="foo", param_2=123)
```
Rule engine filters the applicable rules based on the request params, evaluates them serially and returns `outcome` object as soon as first rule match happens.


# License
[MIT License](https://choosealicense.com/licenses/mit/)



