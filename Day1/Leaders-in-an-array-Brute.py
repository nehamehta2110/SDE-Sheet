class Solution:
    # Back-end complete function Template for Python 3

    # Function to find the leaders in the array.
    def leaders(self, A, N):
        output = []
        for i in range(0, N):
            for j in range(i + 1, N):
                if A[i] <= A[j]:
                    break
            if j == N - 1:  # If loop didn't break
                output.append(A[i])
        return output


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        obj = Solution()

        A = obj.leaders(A, N)

        for i in A:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends