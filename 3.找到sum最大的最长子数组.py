class solution:

    def maxSubArray(self,a):
        """just the sum"""
        max_so_far = a[0]
        max_ending_here = a[0]

        for i in range(1,len(a)):
            if max_ending_here < 0:
                max_ending_here =0
                max_ending_here = max_ending_here +a[i]
                if max_ending_here > max_so_far:
                    max_so_far = max_ending_here

        return max_so_far
    def max_subarray(self,a):
        """the sum and the sunarray index"""

        max_so_far = a[0]
        max_ending_here = a[0]
        s= 0
        e = 0

        for i in range(1,len(a)):
            if max_ending_here <0:
                max_ending_here = 0
                s = i
                print("s=",i)

            max_ending_here = max_ending_here +a[i]
            if max_ending_here >max_so_far:
                max_so_far = max_ending_here
                e =i
                print("e=",e)

        return max_so_far,s,e

data = [-2,1,-3,4,-1,2,1,-5,4]
print(solution().max_subarray(data))
