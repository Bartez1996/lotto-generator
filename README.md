# Lotto Generator
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Simple command-line Lotto number generator written in Python.

## Features

- Generates random Lotto number sequences
- Optionally repeats draws (to simulate more randomness)
- Saves results to a file
- Displays a histogram of drawn numbers using matplotlib
- Includes simple unit tests (pytest)

## Usage

```bash
python lotto_generator.py --count 5 --retries 10 --save --histogram
```

Options:

--count — how many sequences you want to generate (default 1)

--retries — how many times to retry drawing a sequence before accepting it (default 1)

--save — save results to results.txt

--histogram — show histogram of drawn numbers

## Testing

To run tests with pytest:

```bash
pytest test_lotto_generator.py
```

## Requirements

Python 3.8+

matplotlib

## Author

Bartłomiej Ostrowski (Bartez1996)
