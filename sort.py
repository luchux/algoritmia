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



def main():
    alist = [4, 6, 1, 2, 5, 3]
    merge_sort(alist)
    print alist

if __name__ == '__main__':
    main()
