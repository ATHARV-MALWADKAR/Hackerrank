M = 1000000007

def main():
    n = int(input())
    d = list(map(int, input().split()))
    dist, coun, cdis, corn = 0, 1, 0, 0
    for a in d:
        c = coun
        ndist = (4 * dist + c * (16 * c * a + 12 * cdis) + 8 * cdis + 12 * c * a + a) % M
        ncdis = (4 * cdis + 8 * c * a + 3 * c * corn + 3 * a + 2 * corn) % M
        ncorn = (2 * corn + 3 * a) % M
        ncoun = (4 * c + 2) % M
        dist, cdis, corn, coun = ndist, ncdis, ncorn, ncoun
    print(dist)

main()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna