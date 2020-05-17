
from dynamic_rules.rule_engine import evaluate_rules
import pytest


class TestHappyFLow:

    def test_matching_rule(self, load_test_rules):
        assert evaluate_rules(
            num_of_cart_items=7,
            cpc_ad_budget=400,
            business_category="PLAH"
        )

    def test_no_matching_rule_found(self, load_test_rules):
        assert evaluate_rules(
            num_of_cart_items=7,
            cpc_ad_budget=400,
            business_category="PL",
            random_condition=141
        ) is None

    def test_missing_operator_support(self, load_test_rules):
        with pytest.raises(Exception):
            evaluate_rules(
                num_of_cart_items=7,
                cpc_ad_budget=400,
                select_condition=[121]
            )
