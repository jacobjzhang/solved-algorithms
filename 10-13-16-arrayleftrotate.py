# https://www.hackerrank.com/challenges/ctci-array-left-rotation

# a = array
# n = number of integers
# k = number of rotations

def array_left_rotation(a, n, k):
    for integer in range(0, k):   
        temp = a[0]

        for i in range(0, n-1):
            a[i] = a[i+1]

        a[n-1] = temp
    
    print(' '.join(map(str,a)))


n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))