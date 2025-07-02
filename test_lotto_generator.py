import pytest
from lotto_generator import generate_sequences

def test_generate_sequences_valid():
    # sprawdzamy normalne działanie
    results = generate_sequences(5, retries=2)
    assert len(results) == 5
    for seq in results:
        assert len(seq) == 6
        assert len(set(seq)) == 6  # brak duplikatów

def test_generate_sequences_invalid_count():
    # sprawdzamy count <= 0
    with pytest.raises(ValueError):
        generate_sequences(0, retries=2)
    with pytest.raises(ValueError):
        generate_sequences(-5, retries=2)

def test_generate_sequences_invalid_retries():
    # sprawdzamy retries <= 0
    with pytest.raises(ValueError):
        generate_sequences(5, retries=0)
    with pytest.raises(ValueError):
        generate_sequences(5, retries=-3)
