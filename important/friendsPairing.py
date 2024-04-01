def friendsPairing(n):
    if n == 1 or n == 2:
        return n
    # single
    # fnm1 = friendsPairing(n-1)
    # pair
    # fnm2 = friendsPairing(n-2)
    # pairWays = (n-1) * fnm2
    # totalWays = fnm1 + pairWays
    return friendsPairing(n-1) + (n-1) * friendsPairing(n-2)


print(friendsPairing(4))
