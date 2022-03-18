# User function Template for python3

class Solution:
    # Complete this function

    # Function to find equilibrium point in the array.
    def equilibriumPoint(self, A, N):
        if N == 1:
            return 1
        if N == 2:
            return -1
        left_sum = 0
        # Your code here
        for i in range(1, N-1):
            left_sum += A[i - 1]
            right_sum = 0
            for j in range(i + 1, N):
                right_sum += A[j]
            if left_sum == right_sum:
                return i + 1
        return -1


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob = Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends