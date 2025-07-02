import pytest
from lotto_generator import generate_sequences

def test_generate_sequences_valid():
    """
    Test that generate_sequences returns the correct number of sequences
    with exactly 6 unique numbers in each sequence.
    """
    results = generate_sequences(5, retries=2)
    assert len(results) == 5
    for seq in results:
        assert len(seq) == 6
        assert len(set(seq)) == 6  # no duplicates

def test_generate_sequences_invalid_count():
    """
    Test that generate_sequences raises ValueError if count is 0 or negative.
    """
    with pytest.raises(ValueError):
        generate_sequences(0, retries=2)
    with pytest.raises(ValueError):
        generate_sequences(-5, retries=2)

def test_generate_sequences_invalid_retries():
    """
    Test that generate_sequences raises ValueError if retries is 0 or negative.
    """
    with pytest.raises(ValueError):
        generate_sequences(5, retries=0)
    with pytest.raises(ValueError):
        generate_sequences(5, retries=-3)
