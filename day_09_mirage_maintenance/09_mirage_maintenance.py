def read_data(filename):
    with open(filename, mode='r') as file:
        for line in file.read().split('\n'):
            yield [int(value) for value in line.split()]


def predict_next_value(values):
    sequences = [values]
    while sum(sequences[-1]) != 0:
        last_sequence_length = len(sequences[-1])
        sequences.append(
            [sequences[-1][i + 1] - sequences[-1][i] for i in range(last_sequence_length - 1)]
        )

    return sum(row[-1] for row in sequences)


if __name__ == '__main__':
    data = read_data('../input/09.txt')
    # data = read_data('../test_input/09.txt')  # 114

    predicted_values = []

    while report := next(data, None):
        predicted_value = predict_next_value(report)
        predicted_values.append(predicted_value)

    print(sum(predicted_values))
