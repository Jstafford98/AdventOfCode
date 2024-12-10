def expand_diskmap(diskmap : str) -> list[str] :
    
    expanded = []
    _id = 0
    for i,c in enumerate(diskmap):

        if i == 0 or i % 2 == 0:
            expanded.extend(_id for _ in range(int(c)))
            _id += 1
        else:
            expanded.extend('.' for _ in range(int(c)))

    return expanded

def compress_blocks(diskmap : list[str]) -> list[str] :
    i = 0
    last_idx = len(diskmap) - 1
    compressed = []
    while i <= last_idx:
        if (c := diskmap[i]) == '.':
            if diskmap[last_idx] != '.':
                compressed.append(diskmap[last_idx])
            else:
                i -= 1 # this will be undone, just want it to stay in place without rewriting the loop logic
            last_idx -= 1
        else:
            compressed.append(c)
        i += 1
    return compressed

def move_block(data : list[str], idxs : list[int], _to : tuple[int, int]):
    for old, new in zip(idxs, range(*_to)):
        data[new] = data[old]
        data[old] = '.'
    return data

def compress_blocks_v2(diskmap : list[str]) -> list[str] :

    compressed = [c for c in diskmap]

    blocks = dict()
    for i in range(len(diskmap)):

        if diskmap[i] == '.': continue
        
        if (d := diskmap[i]) in blocks:
            blocks[d].append(i)
        else:
            blocks[d] = [i,]

    freespace = []
    for i in range(len(diskmap)):
        if diskmap[i] == '.':
            j = i
            while diskmap[j] == '.':
                j+=1
            freespace.append(
                {"start" : i, "stop" : j,}
            )
            i = j

    for _, block in sorted(blocks.items(), key=lambda x : x[0], reverse=True):
        block_size = len(block)
        for free in freespace:

            fstart, fstop = free['start'], free['stop']
            free_size = fstop - fstart

            if free_size < block_size or block[0] < fstart:
                continue

            print([compressed[_i] for _i in block], '=>' ,[compressed[_i] for _i in range(fstart, fstop)],end=' ')
            compressed = move_block(compressed, block, (fstart, fstop))
            free['start'] += block_size
            print('=>' ,[compressed[_i] for _i in range(fstart, fstop)], end=' ')
            fstart = free['start']
            print('=>' ,[compressed[_i] for _i in range(fstart, fstop)])

            break
    return compressed
            
def calculate_checksum(diskmap : list[str]) -> int :
    total = 0
    for pos,val in enumerate(diskmap):
        if val == '.':
            continue
        total += (pos*int(val))
    return total

if __name__ == '__main__' :
    with open("2024/day_nine/sample_input.txt") as buff:
        diskmap = buff.read().strip()
        diskmap_expanded = expand_diskmap(diskmap)
        diskmap_compressed = compress_blocks(diskmap_expanded)
        diskmap_checksum = calculate_checksum(diskmap_compressed)
        print(diskmap_checksum)