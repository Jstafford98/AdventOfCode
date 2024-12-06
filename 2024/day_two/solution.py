def is_safe(level : int, previous : int, direction : int | None = None) -> bool :

    step = level - previous
    step_abs = abs(step)

    if step_abs < 1 or step_abs > 3:
        ''' change too small or too large'''
        return False
    
    if direction is not None and direction != (-1 if step < 0 else 1 ):
        ''' change direction didn't match '''
        return False 
    
    return True

def validate_report(report : list[int]) -> bool :
    
    direction : int | None = None
    last_level, *report = report

    for level in report:

        safe = is_safe(level, last_level, direction)

        if not safe:
            return False

        if direction is None:
            direction =  -1 if (level - last_level) < 0 else 1 

        last_level = level

    return True


def combos(report : list[int]) -> list[list[int]] :
    return [report[:i] + report[i+1:] for i in range(len(report))]

def count_safe_reports(report_data : list[str]) -> int :
    return sum(
        validate_report([int(x) for x in report.strip().split()])
        for report in report_data
    )

def solution_dampened():
    with open("2024/day_two/input.txt", "r") as buff:
        total_safe_reports = 0
        for line in [[int(x) for x in report.strip().split()] for report in buff.readlines()]:
            if any(validate_report(c) for c in combos(line)):
                total_safe_reports+=1
        print(total_safe_reports)

def solution():
    with open("2024/day_two/input.txt", "r") as buff:
        total_safe_reports = count_safe_reports(buff.readlines())
        print(total_safe_reports)
                

if __name__ == '__main__' :
    # non dampened : 383
    # dampened : 436
    solution()
    solution_dampened()