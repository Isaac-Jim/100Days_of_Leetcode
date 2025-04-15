'''
1. have a set that will contain all seen  numbers, list has o(n) lookup
but set has o(1) look up on average that is why i chose a set over list
2. have  an empty list that will contain all duplicates
3. check if the  element  has been seen
4. if yes add it to duplicates
5. if no add it to  the set seen
'''
def find_duplicates(nums):

    seen = set()
    duplicates = []

    for number in nums :
        if  number in seen :
            duplicates.append(number)
        else:
            seen.add(number)
    return duplicates

print(find_duplicates([1,2,3,2,2,5,6,9,3,1,4,11]))