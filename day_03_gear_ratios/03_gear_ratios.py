def read_data(filename):
    with open(filename, mode='r') as file:
        return [line.rstrip('\n') for line in file]


def calculate_part_numbers_value(eng_schematic):
    stored_numbers = []
    current_number = ""
    for row_no in range(len(eng_schematic)):
        for column_no in range(len(eng_schematic[row_no])):
            if eng_schematic[row_no][column_no].isnumeric():
                current_number += eng_schematic[row_no][column_no]
                if column_no == len(eng_schematic[row_no]) - 1 or not eng_schematic[row_no][column_no + 1].isnumeric():
                    # the whole number has been found, and it is stored in current_number
                    # find adjacent_cells for the whole number
                    adjacent_cells = []
                    if row_no != 0:  # add cells directly above every digit if possible
                        adjacent_cells += [eng_schematic[row_no - 1][column_no - x] for x in range(len(current_number))]
                    if row_no != len(eng_schematic) - 1:  # add cells directly under every digit if possible
                        adjacent_cells += [eng_schematic[row_no + 1][column_no - x] for x in range(len(current_number))]
                    if column_no != 0:  # add top left, left and bottom left adjacent cell if possible
                        if row_no != 0:  # top left
                            adjacent_cells.append(eng_schematic[row_no - 1][column_no - len(current_number)])
                        adjacent_cells.append(eng_schematic[row_no][column_no - len(current_number)])  # left
                        if row_no != len(eng_schematic) - 1:  # bottom left
                            adjacent_cells.append(eng_schematic[row_no + 1][column_no - len(current_number)])
                    if column_no != len(eng_schematic[row_no]) - 1:  # add top right, right and bottom right cell
                        if row_no != 0:  # top right
                            adjacent_cells.append(eng_schematic[row_no - 1][column_no + 1])
                        adjacent_cells.append(eng_schematic[row_no][column_no + 1])  # right
                        if row_no != len(eng_schematic) - 1:  # bottom right
                            adjacent_cells.append(eng_schematic[row_no + 1][column_no + 1])

                    for value in adjacent_cells:  # check if number is a valid part number
                        if not value.isnumeric() and value != '.':
                            stored_numbers.append(int(current_number))
                            break

                    current_number = ""

    return sum(stored_numbers)


if __name__ == '__main__':
    test_data = read_data('../test_input/03.txt')
    assert calculate_part_numbers_value(test_data) == 4361

    data = read_data('../input/03.txt')
    result = calculate_part_numbers_value(data)
    print(result)
