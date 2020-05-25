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

    def less_than_or_equal(self):
        return self.less_than() or self.equals()

    def greater_than_or_equal(self):
        return self.greater_than() or self.equals()

    OPERATOR_MAP = {
        "lt": less_than,
        "gt": greater_than,
        "eq": equals,
        "lte": less_than_or_equal,
        "gte": greater_than_or_equal
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