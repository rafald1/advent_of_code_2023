def read_data(filename):
    with open(filename, mode='r') as file:
        for line in file.read().split('\n'):
            yield [int(value) for value in line.split()]


def predict_previous_value(values):
    sequences = [values]
    while sum(sequences[-1]) != 0:
        last_sequence_length = len(sequences[-1])
        sequences.append(
            [sequences[-1][i + 1] - sequences[-1][i] for i in range(last_sequence_length - 1)]
        )

    # x = a - (b - (c - d)) -> x = a + (-b) + c + (-d)
    return sum(-row[0] if sequence_row_no % 2 != 0 else row[0] for sequence_row_no, row in enumerate(sequences))


if __name__ == '__main__':
    data = read_data('../input/09.txt')
    # data = read_data('../test_input/09.txt')  # 2

    predicted_values = []

    while report := next(data, None):
        predicted_value = predict_previous_value(report)
        predicted_values.append(predicted_value)

    print(sum(predicted_values))
