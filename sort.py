# n-1 passing. O(n^2)
def bubble_sort(alist):
    for passing in range(len(alist)-1, 0, -1):
        for i in range(passing):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

def main():
    alist = [4, 6, 1, 2, 5, 3]
    bubble_sort(alist)
    print alist

if __name__ == '__main__':
    main()
