import functools


def read_data(filename):
    with open(filename, mode='r') as file:
        return [(line.split()[0], int(line.split()[1])) for line in file]


def process_hand(received_hand: str):
    processed_hand = {}
    for card in received_hand:
        if card not in processed_hand:
            processed_hand[card] = 1
        else:
            processed_hand[card] += 1
    return dict(sorted(processed_hand.items(), key=lambda x: x[1], reverse=True))


def calculate_hand_value(processed_hand):
    match list(processed_hand.values()):
        case [5]:
            return 6
        case [4, 1]:
            return 5
        case [3, 2]:
            return 4
        case [3, 1, 1]:
            return 3
        case [2, 2, 1]:
            return 2
        case [2, 1, 1, 1]:
            return 1
        case _:
            return 0


def compare_hands(hand_1, hand_2):
    cards_order = '23456789TJQKA'
    hand_1 = hand_1[0]
    hand_2 = hand_2[0]
    hand_1_value = calculate_hand_value(process_hand(hand_1))
    hand_2_value = calculate_hand_value(process_hand(hand_2))

    if hand_1_value > hand_2_value:
        return 1
    if hand_1_value < hand_2_value:
        return -1

    for card_hand_1, card_hand_2 in zip(hand_1, hand_2):
        if card_hand_1 == card_hand_2:
            continue
        return 1 if cards_order.index(card_hand_1) > cards_order.index(card_hand_2) else -1

    return 0


def calculate_total_winnings(sorted_data):
    return sum((index + 1) * bid for index, (_, bid) in enumerate(sorted_data))


if __name__ == '__main__':
    data = read_data('../input/07.txt')
    # data = read_data('../test_input/07.txt')  # 6440

    data.sort(key=functools.cmp_to_key(compare_hands))
    total_winnings = calculate_total_winnings(data)
    print(total_winnings)
