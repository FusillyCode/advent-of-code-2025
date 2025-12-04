import os
import importlib.util


def _load_module():
    """Load the `2-2.py` module by file path (filename isn't a valid import name)."""
    path = os.path.join(os.path.dirname(__file__), "2-2.py")
    spec = importlib.util.spec_from_file_location("mod_2_2", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_repeats_true_basic():
    mod = _load_module()
    assert mod.repeats(1212) is True


def test_repeats_true_various():
    mod = _load_module()
    assert mod.repeats(123123) is True
    assert mod.repeats(121212) is True
    assert mod.repeats(1111) is True


def test_repeats_false_cases():
    mod = _load_module()
    # odd length should be False
    assert mod.repeats(123) is False
    # not a repeating pattern
    assert mod.repeats(123124) is False
    # two different digits -> not repeating substring
    assert mod.repeats(10) is False


def test___repeats_direct():
    mod = _load_module()
    func = getattr(mod, "repeats_n_numbers")
    # simple repeated substring
    assert func("1212", 2) is True
    # length not divisible by n -> False
    assert func("1234", 3) is False
    # n == 0 -> False
    assert func("1234", 0) is False
    # single-character repeating
    assert func("1111", 1) is True
