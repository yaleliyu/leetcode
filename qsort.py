
def switch(input:list, a, b):
    if a == b:
        return

    tmp = input[a]
    input[a] = input[b]
    input[b] = tmp

def qsort_impl(input:list, start, end):
    if start>= end:
        return

    cursor = start
    left = start+1
    right = end

    while left <= right:
        need_exchange = False
        while left <= right:
            if input[right] < input[cursor]:
                need_exchange = True
                break
            right -= 1

        if need_exchange:
            switch(input, right, cursor)
            cursor = right
            right -= 1

        need_exchange = False
        while left <= right:
            if input[left] > input[cursor]:
                need_exchange = True
                break
            left += 1

        if need_exchange:
            switch(input, cursor, left)
            cursor = left
            left += 1

    if start < cursor:
        qsort_impl(input, start, cursor-1)

    if end > cursor:
        qsort_impl(input, cursor+1, end)


def qsort(input:list):
    qsort_impl(input, 0, len(input)-1)


input = [5,-3,7,2,8,-2,0,2,5,-3,8,7,9,-4,6,7,-1,3,9,2,4,6,3,8,2,9,-6,5,4,0,1,5,7,5,-7,5,7,5,1,3,5,9]

print(input)
qsort(input)
print(input)