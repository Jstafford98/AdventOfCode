from __future__ import annotations
from solution import expand_diskmap, calculate_checksum

class Block:

    def __init__(self, start : int, stop : int, id : int | None = None,) -> None :
        self.id = id
        self.start = start
        self.stop = stop
    
    def __str__(self) -> str :
        return f'Block(id={self.id}, start={self.start}, stop={self.stop})'
    
    def __repr__(self):
        return str(self)
    
    def __iter__(self) -> list[int] :
        return (x for x in range(self.start, self.stop + 1))
    
    def __len__(self) -> int :
        return len(range(self.start, self.stop + 1))

    def fill(self, block : Block) -> None :
        for _ in block:
            self.start += 1

    def can_fit(self, block : Block) -> bool :
        return len(self) >= len(block)
    
    @property
    def slice(self) -> slice :
        return slice(self.start, self.stop + 1)

def create_free_blocks(diskmap : list[str]) -> list[Block] :
    freespace = []
    i = 0
    while i < len(diskmap):

        if diskmap[i] == '.':
            j = i
            while diskmap[j] == '.':
                j+=1
            freespace.append(
                {"start" : i, "stop" : j -1,}
            )
            i = j
        else:
            i += 1

    return [Block(x['start'], x['stop']) for x in freespace]

def create_used_blocks(diskmap : list[str]) -> list[Block] :
    
    blocks = dict()
    for i in range(len(diskmap)):

        if diskmap[i] == '.': continue
        
        if (d := diskmap[i]) in blocks:
            blocks[d].append(i)
        else:
            blocks[d] = [i,]

    return [Block(idxs[0], idxs[-1], id) for id, idxs in blocks.items()]

def compress_diskmap(diskmap : list[str]) -> list[str] :
    
    compressed = [x for x in diskmap] # copy for mutations
    
    blocks = sorted(create_used_blocks(diskmap), key=lambda b : b.id, reverse=True)
    free_blocks = create_free_blocks(diskmap)
    for block in blocks:
        for free in free_blocks:

            if free.start > block.start:
                continue
            if free.can_fit(block):
                print("Moving", block, "to", free)
                for _to, _from in zip(free, block):
                    compressed[_to] = compressed[_from]
                    compressed[_from] = '.'
                free.fill(block)
                break
    return compressed


if __name__ == '__main__' :

    with open("2024/day_nine/input.txt") as buff:
        diskmap = buff.read().strip()

    diskmap_expanded = expand_diskmap(diskmap)
    diskmap_compressed = compress_diskmap(diskmap_expanded)
    diskmap_checksum = calculate_checksum(diskmap_compressed)
    print(diskmap_checksum)