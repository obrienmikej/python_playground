import re
import unittest

def roman_to_int(s: str) -> int:
    
    # Define roman numeral values in dictionary
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    # Validate input; empty or not a string
    if not isinstance(s, str) or not s:
        return 0
    
    # Validate input; is a roman numeral value
    if not re.fullmatch(r'^[IVXLCDM]+$', s):
        return None
    
    # Validate input; invalid roman numeral pattern
    invalid_patterns = re.compile(r'(IIII|VV|XXXX|LL|CCCC|DD|MMMM|IL|IC|ID|IM|VX|XD|XM|LC|LD|LM|DM)')
    if invalid_patterns.search(s):
        return None

    # Initialize variables
    result = 0
    prev_value = 0

    # Convert a Roman numeral string (s) into an integer value (result).
    for char in s:
        value = roman_dict[char]
        if value > prev_value:
            result += value - 2 * prev_value  # Adjust the previously added value
        else:
            result += value
        prev_value = value

    return result

class TestRomanToInt(unittest.TestCase):
    def test_valid_roman_numerals(self):
        self.assertEqual(roman_to_int("I"), 1)
        self.assertEqual(roman_to_int("V"), 5)
        self.assertEqual(roman_to_int("X"), 10)
        self.assertEqual(roman_to_int("VI"), 6)
        self.assertEqual(roman_to_int("IV"), 4)
        self.assertEqual(roman_to_int("IX"), 9)
        self.assertEqual(roman_to_int("MMXXIII"), 2023)
        self.assertEqual(roman_to_int("CMXCIX"), 999)
        self.assertEqual(roman_to_int("MCMXCIV"), 1994)
        self.assertEqual(roman_to_int("LXXXIV"), 84)
        self.assertEqual(roman_to_int("CCXLVI"), 246)
        self.assertEqual(roman_to_int("MMMCMXCIX"), 3999)
    
    def test_invalid_roman_numerals(self):
        self.assertIsNone(roman_to_int("A"))
        self.assertIsNone(roman_to_int("IIII"))
        self.assertIsNone(roman_to_int("VV"))
        self.assertIsNone(roman_to_int("IC"))
        self.assertIsNone(roman_to_int("IL"))
        self.assertIsNone(roman_to_int("VX"))
        self.assertIsNone(roman_to_int("CCCC"))
        self.assertIsNone(roman_to_int("XD"))
        self.assertIsNone(roman_to_int("IIIIX"))
        self.assertIsNone(roman_to_int("LC"))
        self.assertIsNone(roman_to_int("DM"))        

    def test_edge_cases(self):
        self.assertEqual(roman_to_int(""), 0)
        self.assertIsNone(roman_to_int(" "))  # Invalid due to space
        self.assertIsNone(roman_to_int("IIIIIIII"))  # Long invalid sequence
        self.assertIsNone(roman_to_int("VVVV"))  # Repeated invalid numeral        

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)