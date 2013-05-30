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

def main():
    alist = [4, 6, 1, 2, 5, 3]
    insertion_sort(alist)
    print alist

if __name__ == '__main__':
    main()
