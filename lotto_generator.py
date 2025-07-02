import random

def draw_numbers():
    return random.sample(range(1, 50), 6)

def generate_sequences(count: int, retries: int = 1):
    """
    Generates a list of lotto sequences.
    Each sequence is drawn 'retries' times, last attempt is returned.
    """
    if count < 1:
        raise ValueError("Count must be a positive integer greater than 0!")

    if retries < 1:
        raise ValueError("Retries must be a positive integer greater than 0!")

    results = []
    for seq in range(count):
        for retr in range(retries):
            numbers = draw_numbers()
        results.append(numbers)
    return results

def save_to_file(results, filename="lotto_results.txt"):
    with open(filename, "w") as f:
        for idx, sequence in enumerate(results, start=1):
            f.write(f"Sequence {idx}: {sequence}\n")
    print(f"Saved to {filename}")

def show_histogram(results):
    """
    Very simple text histogram of all drawn numbers
    """
    from collections import Counter
    import matplotlib.pyplot as plt

    # Put numbers from all sequences into one list
    flat = [n for seq in results for n in seq]
    counts = Counter(flat)

    # Plot with matplotlib
    plt.bar(counts.keys(), counts.values())
    plt.xlabel("Number")
    plt.ylabel("Frequency")
    plt.title("Histogram of drawn numbers")
    plt.show()

def cli():
    """
    Command-line interface for the Lotto generator.
    
    Example usage:
        python lotto_generator.py --count 5 --retries 10 --save --histogram

    Available options:
        --count      how many sequences to generate
        --retries    how many times to retry each sequence before accepting
        --save       save results to results.txt
        --histogram  show a frequency histogram
    """
    import argparse
    parser = argparse.ArgumentParser(description="Lotto number generator")
    parser.add_argument("--count", type=int, default=1,
                        help="how many sequences you want to generate")
    parser.add_argument("--retries", type=int, default=1,
                        help="how many times to retry each sequence before accepting last draw")
    parser.add_argument("--save", action="store_true",
                        help="save results to file")
    parser.add_argument("--histogram", action="store_true",
                        help="show frequency histogram")

    args = parser.parse_args()

    results = generate_sequences(args.count, args.retries)

    for idx, numbers in enumerate(results, start=1):
        print(f"Sequence {idx}: {numbers}")

    if args.save:
        save_to_file(results)

    if args.histogram:
        show_histogram(results)


if __name__ == "__main__":
    cli()
