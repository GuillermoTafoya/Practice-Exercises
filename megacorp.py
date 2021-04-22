"""This problem was asked by Atlassian.

MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written.
They would like to give the smallest positive amount to each worker consistent with the constraint
that if a developer has written more lines of code than their neighbor, they should receive more money.

Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.

For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1]."""

def reward(array):
    length = len(array)
    

    if length < 2:
        return [1 for x in range(length)]

    r = [0 for x in range(length)]

    r[0] = 2 if array[1] < array[0] else 1

    for idx in range(1,length-1):
        
            right = 2 if array[idx + 1] < array[idx] else -1

            left = r[idx-1]+1 if array[idx - 1] < array[idx] else -1

            r[idx] += max(left,right) if 0 < left or 0 < right else 1

    r[-1] += r[-2]+1 if array[-2] < array[-1] else 1

    return r


example = [10, 40, 200, 1000, 60, 30]

control =  [1, 2, 3, 4, 2, 1]

output = reward(example)

print(output)

print("Control == Output:",control==output)

test = [15, 20, 10, 20, 30, 30]

control =  [1, 2, 1, 2, 3, 1]

output = reward(test)

print(output)

print("Control == Output:",control==output)

print(reward([10,5]))

print(reward([4,7]))

print(reward([10,5,10]))

print(reward([1000]))