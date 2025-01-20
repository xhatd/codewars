'''
Task

You get an array of numbers, return the sum of all of the positives ones.

Example

    [1, -4, 7, 12] => 1+7+12=20 1 + 7 + 12 = 20 1+7+12=20
'''

def positive_sum(arr):
    return 0 if not arr else sum(num for num in arr if num > 0)

array = [1, -4, 7, 12]
print(positive_sum(array))

'''
I could of got rid of the return 0 if not arr ...
because it would just print 0 if nothing exists
'''
