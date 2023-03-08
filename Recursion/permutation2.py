

def permutation(proc,unproc,ans):
    if len(unproc) == 0:
        ans.append(proc)
        
    
    else:
        for i in range(len(unproc)):
            n_proc = proc + unproc[i]
            n_unproc = unproc[0:i]+unproc[i+1:]
            permutation(n_proc,n_unproc,ans)
        return ans

print(permutation("","ABC",[]))