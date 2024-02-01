import math


def read_data(filename):
    with open(filename, mode='r') as file:
        workflows = file.read().split('\n\n')[0]
        return workflows


def process_raw_workflows(workflows):
    workflow = {}

    for raw_workflow in workflows.splitlines():
        name, raw_rules = raw_workflow[:-1].split('{')
        rules = raw_rules.split(',')

        # a<2006:qkq -> ['a', '<', 2006, 'qkq']
        workflow[name] = [(*rule[:2], int(rule[2:].split(':')[0]), rule[2:].split(':')[1]) for rule in rules[:-1]]
        workflow[name] += [('-', '-', 0, rules[-1])]

    return workflow


def sort_parts(workflows):
    queue = [({'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}, 'in')]
    distinct_combinations_total = 0

    while queue:
        part_ranges, workflow_name = queue.pop()
        if workflow_name == 'A':
            distinct_combinations_total += math.prod(high - low + 1 for low, high in part_ranges.values())

        while workflow_name not in 'AR':
            rules = workflows[workflow_name]

            for rule in rules:
                category, operator, value, destination = rule
                low, high = part_ranges.get(category, (None, None))

                if operator == '<' and low < value:
                    # split the range of one category and add all of them to the queue with the new destination
                    queue.append((part_ranges | {category: (low, value - 1)}, destination))
                    # category ranges will be checked against the next rule and need to be updated to reflect the split
                    part_ranges[category] = (value, high)
                elif operator == '>' and high > value:
                    queue.append((part_ranges | {category: (value + 1, high)}, destination))
                    part_ranges[category] = (low, value)
                else:
                    queue.append((part_ranges, destination))
            break

    return distinct_combinations_total


if __name__ == '__main__':
    raw_workflows = read_data('../input/19.txt')
    # raw_workflows = read_data('../test_input/19.txt')  # 167409079868000

    processed_workflows = process_raw_workflows(raw_workflows)

    result = sort_parts(processed_workflows)
    print(result)
