import sys, os
sys.path.insert(0, os.path.abspath("src"))
import text_utils

def test_clean_name_whitespace():
    assert text_utils.clean_name("  sara   ali  ") == "Sara Ali"

def test_clean_name_capitalisation():
    assert text_utils.clean_name("SARA ALI") == "Sara Ali"
    assert text_utils.clean_name("sara ali") == "Sara Ali"
