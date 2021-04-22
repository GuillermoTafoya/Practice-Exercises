def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if fastest:
        redShirtSpeeds = list(reversed(redShirtSpeeds))

    total = 0

    if fastest:
        for x in range(len(redShirtSpeeds)):
            total += max(redShirtSpeeds[x],blueShirtSpeeds[x])
    else:
        for x in range(len(redShirtSpeeds)):
            total += min(redShirtSpeeds[x],blueShirtSpeeds[x])


    return total


redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]
fastest = True
expected = 32
actual = tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)

print(actual)