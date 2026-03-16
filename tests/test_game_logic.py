from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50)
    assert result == "Too Low"


# Bug 1: hint messages were swapped
def test_too_high_message_says_go_lower():
    outcome, message = check_guess(80, 30)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_message_says_go_higher():
    outcome, message = check_guess(10, 70)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# Bug 4: string comparison breaks numeric ordering (e.g. "9" > "10" is True)
def test_check_guess_uses_numeric_comparison():
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"
