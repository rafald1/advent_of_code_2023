import re


def find_valid_games(input_string, red=12, green=13, blue=14):
    game = re.search(r'Game (\d+):', input_string)
    max_red_value = max(int(match) for match in re.findall(pattern=r'(\d+) red', string=input_string))
    max_green_value = max(int(match) for match in re.findall(pattern=r'(\d+) green', string=input_string))
    max_blue_value = max(int(match) for match in re.findall(pattern=r'(\d+) blue', string=input_string))

    if max_red_value <= red and max_green_value <= green and max_blue_value <= blue:
        return int(game.group(1))
    else:
        return 0


def process_data(filename):
    with open(filename, mode='r') as file:
        return sum(find_valid_games(line) for line in file)


if __name__ == '__main__':
    assert process_data('../test_input/02.txt') == 8

    result = process_data('../input/02.txt')
    print(result)
