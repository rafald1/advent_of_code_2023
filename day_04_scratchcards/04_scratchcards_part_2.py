def read_data(filename):
    with open(filename, mode='r') as file:
        return [line for line in file]


def calculate_total_of_scratchcards(scratchcards):
    no_of_each_card_you_have = [1 for _ in range(len(scratchcards))]

    for card_index, card in enumerate(scratchcards):
        winning_numbers = set(card.split(':')[1].split('|')[0].split())
        numbers_you_have = set(card.split(':')[1].split('|')[1].split())
        no_of_cards_you_won = len(winning_numbers & numbers_you_have)
        for i in range(1, no_of_cards_you_won + 1):
            no_of_each_card_you_have[card_index + i] += no_of_each_card_you_have[card_index]

    return sum(no_of_each_card_you_have)


if __name__ == '__main__':
    test_data = read_data('../test_input/04.txt')
    assert calculate_total_of_scratchcards(test_data) == 30

    data = read_data('../input/04.txt')
    result = calculate_total_of_scratchcards(data)
    print(result)
