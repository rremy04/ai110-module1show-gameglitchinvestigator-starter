from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    # FIXME: This test returns a tuple so I need to unpack it into outcome and message
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    # FIXME: This test returns a tuple so I need to unpack it into outcome and message
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    # FIXME: This test returns a tuple so I need to unpack it into outcome and message
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_guess_above_secret_is_too_high():
    # The exact case from the bug: 60 vs 50 must be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_too_high_tells_player_to_go_lower():
    # The original bug: message said "HIGHER" when the guess was too high
    # FIXME: Ensures that the test returns what I expected for the output given the inputs.
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message


def test_guess_below_secret_is_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_too_low_tells_player_to_go_higher():
    # FIXME: Ensures that the test returns what I expected for the output given the inputs.
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message


def test_correct_guess_wins():
    # FIXME: Ensures that the test returns what I expected for the output given the inputs.
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_ints_compare_numerically_not_as_text():
    # FIXME: Ensures that the test returns what I expected for the output given the inputs.
    # Guards the string-secret bug: as text, "9" > "10" is True
    outcome, message = check_guess(9, 10)
    assert outcome == "Too Low"
