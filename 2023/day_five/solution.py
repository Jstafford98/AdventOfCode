import re
import itertools
from tqdm import tqdm
from pprint import pprint

if __name__ == '__main__' :
    #pt 1: 57075758 - correct,
    #pt 2: 
    with open("2023/day_five/input.txt") as buff:

        seeds, *maps = buff.read().split("\n\n")
        seeds = list(map(int, seeds.lstrip("seeds: ").strip().split(" ")))
        
        locs = []
        for seed in seeds:
            k = seed
            for _map in maps:
                for lookup in _map.split("\n")[1:]:
                    d_start, k_start, delta = map(int, lookup.split(" "))
                    if k_start <= k <= k_start + delta:
                        k = k - k_start + d_start
                        break
            locs.append(k)
        print(min(locs))

        # begin part two here chat gpt
        locs = []
        total_seeds = 0
        for i in range(1, len(seeds), 2):
            _, length = seeds[i-1:i+1]
            total_seeds += length
        
        with tqdm(total=total_seeds) as bar:
            for i in range(1, len(seeds), 2):
                start, length = seeds[i-1:i+1]
                for seed in range(start, start + length):
                    k = seed
                    for _map in maps:
                        for lookup in _map.split("\n")[1:]:
                            d_start, k_start, delta = map(int, lookup.split(" "))
                            if k_start <= k <= k_start + delta:
                                k = k - k_start + d_start
                                break
                    bar.update()
                    locs.append(k)
            print(min(locs))
        