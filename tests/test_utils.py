# Distributed under the terms of the MIT License.
from HaikuPorter.Utils import cmp, naturalCompare, prefixLines
from pytest import mark


@mark.parametrize(
    "input_str, prefix, expected_output",
    [
        ["first\nsecond", "pre", "prefirst\npresecond"],
        ["first\nsecond", "", "first\nsecond"],
    ],
)
def test_prefixlines(input_str, prefix, expected_output):
    """Tests prefixLines()."""
    assert prefixLines(prefix=prefix, string=input_str) == expected_output


@mark.parametrize(
    "test_data, expected_output", [[[0, 1], -1], [[1, 1], 0], [[1, 0], 1]]
)
def test_cmp(test_data, expected_output):
    """Tests cmp()."""
    assert cmp(*test_data) == expected_output


@mark.parametrize(
    "test_data, expected_output",
    [
        [["0", "1"], -1],
        [[0, "1"], -1],
        [["0", 1], -1],
        [[0, 1], -1],
        [["a", "b"], -1],
    ],
)
def test_naturalcompare(test_data, expected_output):
    """Tests naturalCompare()."""
    assert naturalCompare(*test_data) == expected_output
