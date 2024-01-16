import re
from functools import cache


def read_data(filename):
    with open(filename, mode='r') as file:
        for line in file:
            reports = line.rstrip('\n').split()
            yield '?'.join([reports[0]] * 5), tuple(int(number) for number in reports[1].split(',')) * 5


def simplify_field_record(field_record):
    return re.sub(r'[.]+', '.', field_record.strip('.'))


@cache
def check_if_valid_solution(field_record, validators):
    if not field_record:  # end of a field record was reached, valid solution found if there is no more validators
        return 0 if validators else 1
    if not validators:  # all validators have been used, valid solution if there is no more springs on the field record
        return 0 if '#' in field_record else 1

    first_value, rest_of_record = field_record[0], field_record[1:]

    if first_value == '.':  # carry on with the rest_of_record
        return check_if_valid_solution(rest_of_record, validators)

    if first_value == '?':  # pursue two possibilities
        return (check_if_valid_solution('#' + rest_of_record, validators) +
                check_if_valid_solution(rest_of_record, validators))  # no need to add '.', see previous if

    if first_value == '#':
        first_validator = validators[0]
        segment = field_record.split('.')[0]  # split the field_record if possible

        # if length of segment matches length indicated by validator
        # as well if it is greater than length indicated by validator and at the same time there is no '#' after it,
        # you carry on omitting the number of values indicated by validator and omitting first_validator from validators
        if len(segment) == first_validator or len(segment) > first_validator and field_record[first_validator] != '#':
            return check_if_valid_solution(field_record[first_validator + 1:], validators[1:])

        # valid solution can't be found because length of segment was too short or
        # length of segment was longer than indicated by validator, but there was a damaged spring directly after,
        # making the sequence of broken springs longer than indicated by validator
        return 0


if __name__ == '__main__':
    data_generator = read_data('../input/12.txt')
    # data_generator = read_data('../test_input/12.txt')  # 525152

    result = 0
    while record_set := next(data_generator, None):
        result += check_if_valid_solution(record_set[0], record_set[1])
    print(result)
