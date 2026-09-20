import sys, os
sys.path.insert(0, os.path.abspath("src"))
import grade_utils

def test_letter_grade():
    assert grade_utils.letter_grade(5.00) == "A"
    assert grade_utils.letter_grade(3.90) == "B"
    assert grade_utils.letter_grade(0.00) == "F"

def test_dean_list():
    assert grade_utils.is_dean_list(4.50) is True
    assert grade_utils.is_dean_list(4.49) is False
