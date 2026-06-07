import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)
    assert get_range_for_difficulty("Unknown") == (1, 100)


def test_hints_not_reversed():
    # Regression: hints were previously swapped (Too High returned when guess was low, etc.)
    outcome_high, _ = check_guess(60, 50)  # guess > secret → must be "Too High"
    assert outcome_high == "Too High", f"Expected 'Too High' but got '{outcome_high}' — hint may be reversed"

    outcome_low, _ = check_guess(40, 50)  # guess < secret → must be "Too Low"
    assert outcome_low == "Too Low", f"Expected 'Too Low' but got '{outcome_low}' — hint may be reversed"
