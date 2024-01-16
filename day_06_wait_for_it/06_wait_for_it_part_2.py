import math


def read_data(filename):
    with open(filename, mode='r') as file:
        race_time = file.readline().split(':')[1].replace(' ', '')
        race_distance = file.readline().split(':')[1].replace(' ', '')
    return int(race_time), int(race_distance)


def calculate_ways_to_beat_record(time, distance):
    # (preparation_time * 1) * (time - preparation_time) > distance
    preparation_time1 = (time - math.sqrt(available_time ** 2 - 4 * distance)) / 2
    preparation_time2 = (time + math.sqrt(available_time ** 2 - 4 * distance)) / 2

    # you have to spend more time preparing than preparation_time1 and less than preparation_time2 to win
    # you should round up preparation_time1 and round down preparation_time2, but
    # we are interested in difference so there is no need to round up
    return int(preparation_time2) - int(preparation_time1)


if __name__ == '__main__':
    available_time, recorded_distance = read_data('../input/06.txt')
    # available_time, recorded_distance = read_data('../test_input/06.txt')  # 71503

    result = calculate_ways_to_beat_record(available_time, recorded_distance)
    print(result)
