def load_data(file : str) -> tuple[list[tuple[int, int]], list[int]] :
    with open(file) as buff:
        data = buff.readlines()
    rules = True
    print_jobs = []
    print_rules = []
    for line in data:
        if line == '\n':
            rules = False
            continue
        if rules:
            line = [*map(int, line.strip().split("|"))]
            print_rules.append(line)
        else:
            line = [*map(int, line.strip().split(","))]
            print_jobs.append(line)
    return print_rules, print_jobs

def solution(rules : list[tuple[int, int]], jobs : list[list[int]]) -> int :

    count_bad = 0
    count_good = 0

    rule_table = dict()
    for k,v in rules:
        if k in rule_table:
            rule_table[k].append(v)
        else:
            rule_table[k] = [v,]

    for job in jobs:
        job_table = {v:i for i,v in enumerate(job)}
        for page, page_pos in job_table.items():
            comes_before = rule_table.get(page, None)
            if comes_before is None: continue
            if not all(page_pos <= job_table.get(x, page_pos) for x in comes_before):
                break
        else:
            count_good += job[(len(job) // 2)]
            continue

        # sort the bad job using the rules
        job_copy = job.copy()
        job_table_copy = job_table.copy()

        violation = True
        while violation:
            violation = False
            for x_idx in range(len(job_copy)):

                x = job_copy[x_idx]

                rule_x = rule_table.get(x, None)
                if rule_x is None:
                    continue
                
                for y in rule_x:
                    y_idx = job_table_copy.get(y, None)

                    if y_idx is None:
                        continue

                    if x_idx > y_idx:
                        violation = True
                        job_copy.pop(y_idx)
                        job_copy.insert(x_idx, y)
                        job_table_copy = {v:i for i,v in enumerate(job_copy)}
        
        count_bad += job_copy[(len(job_copy) // 2)]
    return count_good, count_bad



if __name__ == '__main__' :

    actual_data = load_data("2024/day_five/input.txt")
    sample_data = load_data("2024/day_five/sample_input.txt")
    answer, answer_pt2 = solution(*actual_data)
    print(answer, answer_pt2)