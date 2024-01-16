def read_data(filename):
    with open(filename, mode='r') as file:
        return [steps for steps in file.readline().split(',')]


def run_hash_algorithm(steps):
    current_value = 0

    for char in steps:
        current_value = (current_value + ord(char)) * 17 % 256

    return current_value


def run_hashmap_algorithm(sequence):
    boxes = [[] for _ in range(256)]
    for step in sequence:
        if '=' in step:
            label, lens_focal_length = step.split('=')
            box_no = run_hash_algorithm(label)

            if label in map(lambda x: x[0], boxes[box_no]):
                boxes[box_no] = [(label, int(lens_focal_length)) if label in lens else lens for lens in boxes[box_no]]
            else:
                boxes[box_no] += [(label, int(lens_focal_length))]

        if '-' in step:
            label = step.split('-')[0]
            box_no = run_hash_algorithm(label)
            boxes[box_no] = [lens for lens in boxes[box_no] if label not in lens]

    return boxes


def calculate_focusing_power(boxes):
    return sum([
        box_no * lens_slot * focal_length
        for box_no, box in enumerate(boxes, start=1)
        for lens_slot, (_, focal_length) in enumerate(box, start=1)
    ])


if __name__ == '__main__':
    initialization_sequence = read_data('../input/15.txt')
    # initialization_sequence = read_data('../test_input/15.txt')  # 145

    boxes_with_lenses = run_hashmap_algorithm(initialization_sequence)
    result = calculate_focusing_power(boxes_with_lenses)

    print(result)
