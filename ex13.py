def CalculateSum(list_data):
    if list_data.__len__() == 0:
        return 0
    else:
        total = 0
        for i in list_data:
            total = total + i

        return total


def CalculateProduct(list_data):
    if list_data.__len__() == 0:
        return 0
    else:
        total = 1
        for i in list_data:
            total = total * i
        return total


def average(list_data):
    if list_data.__len__() == 0:
        return 0
    else:
        list_count = list_data.__len__()
        list_sum = 0
        for i in list_data:
            list_sum = list_sum + i
            avr = list_sum / list_count
        return avr


def median(numbers):
    if len(numbers) == 0:
        return None

    numbers.sort()

    middleIndex = len(numbers)//2

    if len(numbers)%2 == 0:
        return (numbers[middleIndex]+numbers[middleIndex- 1])/2
    else:
        return numbers[middleIndex]



if __name__ == '__main__':
    print('find sum')
    print(CalculateSum([]) == 0)
    print(CalculateSum([1,3,5,7,9]) == 25)
    print('find product')
    print(CalculateProduct([]) == 0)
    print(CalculateProduct([2,4,6,8,10]) == 3840)
    print('find average')
    print(average([1,2,3]) == 2)
    print(average([1,2,3,1,2,3,1,2,3]) == 2)
    print(average([12,20,37]) == 23)
    print(average([0,0,0,0,0]) == 0)
    print('find median')
    print(median([]) == None)
    print(median([1,2,3]) == 2)
    print(median([3,7,10,4,1,9,6,5,2,8]) == 5.5)
    print(median([3,7,10,4,1,9,6,2,8]) == 6)
