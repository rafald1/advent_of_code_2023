def read_data(filename):
    with open(filename, mode='r') as file:
        modules = {}

        for line in file:
            module, raw_destinations = line.rstrip().split(' -> ')
            destinations = raw_destinations.split(', ')

            if module == 'broadcaster':
                module_type = None
                module_name = module
            else:
                module_type = module[0]
                module_name = module[1:]

            modules[module_name] = (module_type, destinations)

        return modules


def prepare_modules(modules):
    flip_flops = {}
    conjunctions = {}

    for module_name, (module_type, _) in modules.items():
        if module_type == '%':
            flip_flops[module_name] = False
        elif module_type == '&':
            conjunctions[module_name] = {}

    for conjunction_name in conjunctions.keys():
        for module_name, (_, destinations) in modules.items():
            if conjunction_name in destinations:
                conjunctions[conjunction_name][module_name] = False

    return flip_flops, conjunctions


def send_pulse(modules, flip_flops, conjunctions, no_of_pulses=1000):
    low_pulse_counter = 0
    high_pulse_counter = 0

    for _ in range(no_of_pulses):
        pulse_type = False  # False is low, True is high
        low_pulse_counter += 1
        pulse_queue = [('broadcaster', pulse_type, destination) for destination in modules['broadcaster'][1]]

        while pulse_queue:
            source_module_name, pulse_type, module_name = pulse_queue.pop(0)
            if pulse_type:
                high_pulse_counter += 1
            else:
                low_pulse_counter += 1

            if module_name in modules.keys():
                module_type, destinations = modules[module_name]

                if module_type == '%':
                    if pulse_type:
                        continue
                    flip_flops[module_name] = not flip_flops[module_name]
                    pulse_type = flip_flops[module_name]
                elif module_type == '&':
                    conjunctions[module_name][source_module_name] = pulse_type
                    pulse_type = not all(conjunctions[module_name].values())

                pulse_queue.extend([(module_name, pulse_type, destination) for destination in destinations])

    return low_pulse_counter * high_pulse_counter


if __name__ == '__main__':
    all_modules = read_data('../input/20.txt')
    # all_modules = read_data('../test_input/20_1_1.txt')  # 32000000
    # all_modules = read_data('../test_input/20_1_2.txt')  # 11687500

    all_flip_flops, all_conjunctions = prepare_modules(all_modules)

    result = send_pulse(all_modules, all_flip_flops, all_conjunctions)
    print(result)
