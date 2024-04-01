global ways
ways = 0


def tiling(n):
    if n == 0 or n == 1:
        return 1
    # vertical choice
    fnm1 = tiling(n-1)
    # horizontal choice
    fnm2 = tiling(n-2)
    totWays = fnm1 + fnm2
    return totWays


print(tiling(5))
