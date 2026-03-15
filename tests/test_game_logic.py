from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "CORRECT" in message.upper()

def test_guess_too_high():
    # FIX: Updated with Copilot help to validate tuple output + correct directional hint.
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()

def test_guess_too_low():
    # FIX: Updated with Copilot help to validate tuple output + correct directional hint.
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()


def test_high_guess_hint_points_lower_regression():
    # FIX: Added with Copilot as a regression test so reversed hints are caught quickly.
    # Regression: when guess is above secret, message should tell player to go lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()
