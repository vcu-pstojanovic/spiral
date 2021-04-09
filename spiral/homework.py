def spiralize(number):
    # ulam spiral https://www.educative.io/edpresso/how-to-solve-the-number-spiral-diagonals-problem
    n = (number - 1) / 2
    return (3 + 2 * n * (8 * n * n + 15 * n + 13)) / 3
