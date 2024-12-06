from collections import Counter

def solution():
    
    '''
        sample:
            1   2\n
            3   4\n
            5   6\n

        needs to be loaded as list_one, list_two = [1,3,5], [2,4,6]
    '''
    with open('2024/day_one/input.txt', 'r') as buff:
        data = list(map(str.split, buff.readlines()))

    '''
        Sort both lists and make sure they're ints
    '''
    list_one, list_two = [map(int, x) for x in zip(*data)]
    list_one, list_two = map(sorted, (list_one, list_two))

    '''
        Sum the difference between the two lists, sorted in asc order
    '''
    total_difference = 0
    for a,b in zip(list_one, list_two):
        total_difference += abs(a-b)
    print(total_difference)

    '''
        Sum how many times a value in list_one occurs in list_two times 
        the value in list_one

        i.e if 3 occurs 3 times in list_two, total_similarity += (3*3)
    '''
    count = Counter(list_two)
    total_similarity = 0
    for value in list_one:
        total_similarity += (value*count.get(value, 0))
    print(total_similarity)

if __name__ == '__main__' :
    solution()