import pytest
from text_processor import TextProcessor


def test_capitalize_text_equal():
    """1. Assert equal - egyenlőség ellenőrzés"""
    processor = TextProcessor()
    result = processor.capitalize_text("unga bunga")
    assert result == "UNGA BUNGA"



def test_capitalize_text_not_equal():
    """2. Assert not equal - nem egyenlő"""
    processor = TextProcessor()
    result = processor.capitalize_text("unga bunga")
    assert result != "unga bunga"
    assert result != "Unga Bunga"


def test_reverse_text_in():
    """3. Assert in - benne van"""
    processor = TextProcessor()
    result = processor.reverse_text("unga")
    assert "u" in result
    assert "g" in result
    assert "n" in result



def test_reverse_text_not_in():
    """4. Assert not in - nincs benne"""
    processor = TextProcessor()
    result = processor.reverse_text("unga")
    assert "f" not in result
    assert "h" not in result


def test_count_words_isinstance():
    """5. Assert isinstance - típus ellenőrzés"""
    processor = TextProcessor()
    result = processor.count_words("unga bunga")
    assert isinstance(result, int)
    assert not isinstance(result, str)
    assert isinstance(result, int) and result == 2



def test_count_words_greater_less():
    """6. Assert >, <, >=, <= - összehasonlítás"""
    processor = TextProcessor()
    result1 = processor.count_words("unga")
    result2 = processor.count_words("unga bunga")
    result3 = processor.count_words("unga bunga hulla")

    assert result1 < result2    
    assert result2 < result3    
    assert result3 > result1    

def test_count_words_empty_string():
    """7. Üres sztring bemenet ellenőrzése"""
    processor = TextProcessor()
    result = processor.count_words("")
    assert result == 0
    assert result is not None


def test_is_palindrome_true_false():
    """8. Assert True/False - boolean ellenőrzés"""
    processor = TextProcessor()
    result_type = processor.is_palindrome("Anna")
    assert result_type is True
    assert processor.is_palindrome("unga bunga") is False


def test_remove_spaces_multiple_asserts():
    """9. Több assert egy tesztben"""
    processor = TextProcessor()
    result = processor.remove_spaces("unga bunga")
    result2 = processor.remove_spaces("unga bunga")
    assert result == "ungabunga"
    assert len(result2) == 9
    assert isinstance(result, str)