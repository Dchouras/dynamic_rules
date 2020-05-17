from dynamic_rules.rule_processing import load_rules
import pytest


@pytest.fixture(scope="module")
def load_test_rules():
    load_rules("../dynamic_rules/tests/test_rules.json")
