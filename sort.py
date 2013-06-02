# n-1 passing. O(n^2)
def bubble_sort(alist):
    for index in range(len(alist)-1, 0, -1):
        for i in range(index):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

def insertion_sort(alist):
    for index in range(1,len(alist)):

        actual = alist[index]
        position = index

        while position > 0 and actual < alist[position-1]:
            alist[position] = alist[position-1]
            position -= 1

        alist[position] = actual

def merge_sort(alist):

    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]

        #recursive call to break in half lists until atomic
        merge_sort(left)
        merge_sort(right)

        #merging left, right into alist in a sorted way.
        ileft, iright, imerg = 0, 0, 0
        while ileft < len(left) and iright < len(right):
            if left[ileft] < right[iright]:
                alist[imerg] = left[ileft]
                ileft += 1
            else:
                alist[imerg] = right[iright]
                iright += 1

            imerg += 1

        while ileft < len(left):
            alist[imerg] = left[ileft]
            ileft += 1
            imerg += 1

        while iright < len(right):
            alist[imerg] = right[iright]
            iright += 1
            imerg += 1

#partition function to find the pivot in QuickSort
def partition(alist, first, last):
    pivotval = alist[first]

    leftpter = first+1
    rightpter = last

    done = False
    while not done:
        while leftpter <= rightpter and alist[leftpter] <= pivotval:
            leftpter += 1

        while leftpter <= rightpter and alist[rightpter] >= pivotval:
            rightpter -= 1

        if rightpter < leftpter:
            done = True

        else:
            alist[leftpter], alist[rightpter] =  alist[rightpter], alist[leftpter]

    alist[first], alist[rightpter] = alist[rightpter], alist[first]
    return rightpter


#it does the actual work, of call partition, and then the recursive calls.
def quick_sort_helper(alist, first, last):
    if first < last:

        pivot = partition(alist, first, last)

        quick_sort_helper(alist, first, pivot-1)
        quick_sort_helper(alist, pivot+1, last)

#wrapper
def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist)-1)


def main():
    alist = [4, 6, 1, 2, 5, 3]
    quick_sort(alist)
    print alist

if __name__ == '__main__':
    main()
