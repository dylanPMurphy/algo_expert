def numberOfWaysToMakeChange(n, denoms):
    waysToMakeChange = [0 for i in range(n+1)]
    waysToMakeChange[0] = 1
    for d in range(0, len(denoms)):
	    for i in range(denoms[d],n+1):
		    waysToMakeChange[i] += waysToMakeChange[i-denoms[d]]
    return waysToMakeChange[n]
