def read_data(filename):
    with open(filename, mode='r') as file:
        workflows, parts = file.read().split('\n\n')
        return workflows, parts


def process_raw_workflows(workflows):
    workflow = {}

    for raw_workflow in workflows.splitlines():
        name, raw_rules = raw_workflow[:-1].split('{')
        rules = raw_rules.split(',')

        # a<2006:qkq -> ['a', '<', 2006, 'qkq']
        workflow[name] = [(*rule[:2], int(rule[2:].split(':')[0]), rule[2:].split(':')[1]) for rule in rules[:-1]]
        workflow[name] += [('-', '-', 0, rules[-1])]

    return workflow


def process_raw_parts(parts):
    return [
        {element.split('=')[0]: int(element.split('=')[1]) for element in part[1:-1].split(',')}
        for part in parts.splitlines()
    ]


def sort_parts(parts, workflows):
    accepted_parts_sum = 0

    for part in parts:
        workflow_name = 'in'

        while workflow_name not in 'AR':
            rules = workflows[workflow_name]

            for rule in rules:
                category, operator, value, destination = rule

                if operator == '<' and part[category] < value:
                    workflow_name = destination
                    break
                elif operator == '>' and part[category] > value:
                    workflow_name = destination
                    break
                else:
                    workflow_name = destination

            if workflow_name == 'A':
                accepted_parts_sum += sum(part.values())

    return accepted_parts_sum


if __name__ == '__main__':
    raw_workflows, raw_parts = read_data('../input/19.txt')
    # raw_workflows, raw_parts = read_data('../test_input/19.txt')  # 19114

    processed_workflows = process_raw_workflows(raw_workflows)
    processed_parts = process_raw_parts(raw_parts)
    result = sort_parts(processed_parts, processed_workflows)
    print(result)
