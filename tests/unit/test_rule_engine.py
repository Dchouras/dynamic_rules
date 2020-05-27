from dynamic_rules.rule_engine import _determine_data_object
from dynamic_rules.errors import DataTypeMismatchError
import pytest


class TestDetermineDataObject:

    def test_data_type_mismatch(self):
        with pytest.raises(DataTypeMismatchError):
            _determine_data_object(123, "1232")
