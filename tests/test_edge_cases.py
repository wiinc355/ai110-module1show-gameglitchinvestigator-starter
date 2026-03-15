from logic_utils import parse_guess


def test_parse_negative_number_input():
    ok, guess_value, error_message = parse_guess("-7")
    assert ok is True
    assert guess_value == -7
    assert error_message is None


def test_parse_decimal_input_truncates_gracefully():
    ok, guess_value, error_message = parse_guess("42.9")
    assert ok is True
    assert guess_value == 42
    assert error_message is None


def test_parse_extremely_large_integer_input():
    ok, guess_value, error_message = parse_guess("999999999999999999999999999999")
    assert ok is True
    assert guess_value == 999999999999999999999999999999
    assert error_message is None


def test_parse_non_numeric_input_returns_user_friendly_error():
    ok, guess_value, error_message = parse_guess("not-a-number")
    assert ok is False
    assert guess_value is None
    assert error_message == "That is not a number."
