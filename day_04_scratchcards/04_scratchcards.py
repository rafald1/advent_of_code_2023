def read_data(filename):
    with open(filename, mode='r') as file:
        for line in file:
            yield line


def calculate_winning_points(scratchcard: str):
    winning_numbers = set(scratchcard.split(':')[1].split('|')[0].split())
    numbers_you_have = set(scratchcard.split(':')[1].split('|')[1].split())
    no_of_winning_numbers = len(winning_numbers & numbers_you_have)
    return 2 ** (no_of_winning_numbers - 1) if no_of_winning_numbers > 0 else 0


if __name__ == '__main__':
    data = read_data('../input/04.txt')
    # data = read_data('../test_input/04.txt')  # 13

    all_cards_points = 0

    while card := next(data, None):
        all_cards_points += calculate_winning_points(card)

    print(all_cards_points)
