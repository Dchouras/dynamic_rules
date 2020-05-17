class NumericType:
    def __init__(self, input_val, rule_val):
        self.input_val = input_val
        self.rule_val = rule_val

    def less_than(self):
        return self.input_val < self.rule_val

    def greater_than(self):
        return self.input_val > self.rule_val

    def equals(self):
        return self.input_val == self.rule_val

    OPERATOR_MAP = {
        "lt": less_than,
        "gt": greater_than,
        "eq": equals
    }


class StringType:
    def __init__(self, input_val, rule_val):
        self.input_val = input_val
        self.rule_val = rule_val

    def equals(self):
        return self.input_val == self.rule_val

    OPERATOR_MAP = {
        "eq": equals
    }