def read_data(filename):
    with open(filename, mode='r') as file:
        race_times = file.readline().split(':')[1].split()
        race_distances = file.readline().split(':')[1].split()
    return [int(race_time) for race_time in race_times], [int(race_distance) for race_distance in race_distances]


def starting_speed(preparation_time):
    return preparation_time * 1


def calculate_distance(speed, race_time):
    return race_time * speed


def calculate_possible_distances(avail_time):
    return [calculate_distance(starting_speed(prep_time), avail_time - prep_time) for prep_time in range(1, avail_time)]


def calculate_ways_to_beat_record(results, distance_to_beat):
    return len(list(filter(lambda x: distance_to_beat < x, results)))


if __name__ == '__main__':
    times, record_distances = read_data('../input/06.txt')
    # times, record_distances = read_data('../test_input/06.txt')  # 288

    total = 1

    for time, record_distance in zip(times, record_distances):
        possible_race_results = calculate_possible_distances(time)
        total *= calculate_ways_to_beat_record(possible_race_results, record_distance)

    print(total)
