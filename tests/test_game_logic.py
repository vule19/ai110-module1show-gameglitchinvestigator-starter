from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score


# --- check_guess tests ---

def test_winning_guess():
    # check_guess returns (outcome, message); outcome should be "Win"
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_check_guess_returns_tuple():
    result = check_guess(50, 50)
    assert isinstance(result, tuple)
    assert len(result) == 2

def test_check_guess_boundary_one_above():
    outcome, _ = check_guess(51, 50)
    assert outcome == "Too High"

def test_check_guess_boundary_one_below():
    outcome, _ = check_guess(49, 50)
    assert outcome == "Too Low"


# --- parse_guess tests ---

def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_valid_float_truncates():
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7
    assert err is None

def test_parse_guess_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_none():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err is not None


# --- get_range_for_difficulty tests ---

def test_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_range_hard():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 1000

def test_range_unknown_defaults():
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100


# --- update_score tests ---

def test_update_score_win_early():
    # attempt 1: points = 100 - 10*(1+1) = 80
    new_score = update_score(0, "Win", 1)
    assert new_score == 80

def test_update_score_win_minimum_points():
    # attempt 10: 100 - 10*11 = -10, clamped to 10
    new_score = update_score(0, "Win", 10)
    assert new_score == 10

def test_update_score_too_high_even_attempt():
    # even attempt => +5
    new_score = update_score(50, "Too High", 2)
    assert new_score == 55

def test_update_score_too_high_odd_attempt():
    # odd attempt => -5
    new_score = update_score(50, "Too High", 3)
    assert new_score == 45

def test_update_score_too_low():
    new_score = update_score(50, "Too Low", 1)
    assert new_score == 45

def test_update_score_unknown_outcome():
    new_score = update_score(50, "Unknown", 1)
    assert new_score == 50
