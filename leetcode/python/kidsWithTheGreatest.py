
def kidsWithCandies(candies, extraCandies):
    max_value = max(candies)
    print(max_value)
    result = []
    for i in candies:
        if i + extraCandies >= max_value:
            result.append('true')
        else:
            result.append('false')
    return result


print(kidsWithCandies([2, 3, 5, 1, 3], 3))
