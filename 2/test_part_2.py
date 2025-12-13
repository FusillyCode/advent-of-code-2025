from part_2 import repeats, repeats_n_numbers

def test_repeats_true_basic():
    assert repeats(1212) is True


def test_repeats_true_various():
    assert repeats(123123) is True
    assert repeats(121212) is True
    assert repeats(1111) is True


def test_repeats_false_cases():
    # odd length should be False
    assert repeats(123) is False
    # not a repeating pattern
    assert repeats(123124) is False
    # two different digits -> not repeating substring
    assert repeats(10) is False


def test___repeats_direct():
    # simple repeated substring
    assert repeats_n_numbers("1212", 2) is True
    # length not divisible by n -> False
    assert repeats_n_numbers("1234", 3) is False
    # n == 0 -> False
    assert repeats_n_numbers("1234", 0) is False
    # single-character repeating
    assert repeats_n_numbers("1111", 1) is True
