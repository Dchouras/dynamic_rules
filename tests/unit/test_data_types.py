from dynamic_rules.data_types import NumericType
import pytest


class TestNumericType:

    @pytest.mark.parametrize(
        "operator,val1,val2",
        [
            ("lt", 2, 3),
            ("lte", 2, 3),
            ("gt", 3, 2),
            ("gte", 3, 2),
            ("eq", 2, 2),
            ("lte", 2, 2),
            ("gte", 2, 2)
        ]
    )
    def test_numeric_type_happy_flow(self, operator, val1, val2):
        obj = NumericType(val1, val2)
        assert obj.OPERATOR_MAP[operator](obj)
