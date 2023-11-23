def trim_by_polyA(sequence, min_length=20, windowsize=5, cutoff=4):
    if not "AAA" in sequence[-6:]:
        return sequence
    l=len(sequence)
    countA={'A':0,'C':0,'G':0,'T':0,'N':0}
    for i in range(l-windowsize,l):countA[sequence[i]]+=1
    if countA['A']<cutoff:
        return sequence
    pos=0
    j=l-1
    while True:
        if j>=min_length:
            countA[sequence[j]]-=1
            countA[sequence[j-windowsize]]+=1
            if countA['A']<cutoff:
                pos=j-2
                break
        else:
            pos=0
            break
        j-=1
    return sequence[:pos]