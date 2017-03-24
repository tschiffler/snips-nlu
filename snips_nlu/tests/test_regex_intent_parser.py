import unittest

from snips_nlu.intent_parser.regex_intent_parser import RegexIntentParser
from snips_nlu.result import IntentClassificationResult, ParsedSlot
from snips_nlu.tests.utils import SAMPLE_DATASET


class TestRegexIntentParser(unittest.TestCase):
    def test_should_get_intent(self):
        # Given
        dataset = SAMPLE_DATASET
        parser = RegexIntentParser().fit(dataset)
        text = "this is a dummy_a query with another dummy_c"

        # When
        intent = parser.get_intent(text)

        # Then
        probability = 1.0
        expected_intent = IntentClassificationResult(
            intent_name="dummy_intent_1", probability=probability)

        self.assertEqual(intent, expected_intent)

    def test_should_get_slots(self):
        # Given
        dataset = SAMPLE_DATASET
        parser = RegexIntentParser().fit(dataset)
        text = "this is a dummy_a query with another dummy_c"

        # When
        slots = parser.get_slots(text, intent="dummy_intent_1")

        # Then
        expected_slots = [
            ParsedSlot(match_range=(10, 17), value="dummy_a",
                       entity="dummy_entity_1", slot_name="dummy_slot_name"),
            ParsedSlot(match_range=(37, 44), value="dummy_c",
                       entity="dummy_entity_2", slot_name="dummy_slot_name2")
        ]
        self.assertItemsEqual(expected_slots, slots)


if __name__ == '__main__':
    unittest.main()