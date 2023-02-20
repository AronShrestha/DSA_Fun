def permutation(processed,unprocessed):
    if len(unprocessed) == 0:
        print(processed)
        return 
    else:
        ch = unprocessed[0]
        for i in range(len(processed)+1):
            f = processed[0:i]
            e = processed[i:len(processed)]
            permutation(f+ch+e,unprocessed[1:])


permutation("","abc")
