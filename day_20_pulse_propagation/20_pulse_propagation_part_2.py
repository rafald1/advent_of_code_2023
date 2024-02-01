import math


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


def traceback_signal(modules, searched_module_name):
    source = [module_name for module_name, (_, destinations) in modules.items() if searched_module_name in destinations]
    return tuple([module_name for module_name, (_, destinations) in modules.items() if source[0] in destinations])


def send_pulse(modules):
    stop_modules = traceback_signal(modules, 'rx')
    cycle_counters = {module_name: 0 for module_name in stop_modules}

    for stop_module in stop_modules:
        flip_flops, conjunctions = prepare_modules(all_modules)
        is_cycle_length_found = False

        while not is_cycle_length_found:
            cycle_counters[stop_module] += 1
            pulse_type = False  # False is low, True is high
            pulse_queue = [('broadcaster', pulse_type, destination) for destination in modules['broadcaster'][1]]

            while pulse_queue:
                source_module_name, pulse_type, module_name = pulse_queue.pop(0)

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

                if module_name == stop_module and pulse_type:  # one of our stop modules sent high pulse
                    is_cycle_length_found = True

    return math.lcm(*cycle_counters.values())


if __name__ == '__main__':
    all_modules = read_data('../input/20.txt')

    result = send_pulse(all_modules)
    print(result)
