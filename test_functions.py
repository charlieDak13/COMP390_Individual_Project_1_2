import util_functions
import pytest
import io


def test_check_lower_year(monkeypatch, capfd):
    # test that the prompt was properly printed to terminal
    out, err = capfd.readouterr()
    assert out == ''
    # test a valid string
    input_string = '2020'
    simulate_user_input = io.StringIO(input_string)
    monkeypatch.setattr("sys.stdin", simulate_user_input)
    assert util_functions.check_lower_year() == "2020"

    input_string = 'Q'
    simulate_user_input = io.StringIO(input_string)
    monkeypatch.setattr("sys.stdin", simulate_user_input)
    assert util_functions.check_lower_year() == "break"


def test_check_for_break():
    assert util_functions.check_for_break("<q") == True
    assert util_functions.check_for_break("<Q") == True
    assert util_functions.check_for_break("file") == False
    assert util_functions.check_for_break(None) == False
    assert util_functions.check_for_break(13) == False


def test_print_file_name():
    assert util_functions.print_file_name("file") is None
    assert util_functions.print_file_name(None) is None
    assert util_functions.print_file_name(13) is None

