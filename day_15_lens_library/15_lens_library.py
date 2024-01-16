def read_data(filename):
    with open(filename, mode='r') as file:
        for steps in file.readline().split(','):
            yield steps


def run_hash_algorithm(steps):
    current_value = 0

    for char in steps:
        current_value = (current_value + ord(char)) * 17 % 256

    return current_value


if __name__ == '__main__':
    sequence_steps_generator = read_data('../input/15.txt')
    # sequence_steps_generator = read_data('../test_input/15.txt')  # 1320

    result = 0

    while sequence_steps := next(sequence_steps_generator, None):
        result += run_hash_algorithm(sequence_steps)

    print(result)
