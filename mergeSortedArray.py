class Solution:
    def merge(num1, m, num2, n):
        
        while(n >= 0):
            if num1[m] < num2[n]:
                num1[m+n+1] = num2[n]
                n = n-1
                print(num2)
            else:
                print("else")
                num1[m], num2[n] = num2[n], num1[m]
                

        return num1


if __name__ == '__main__':
    a = Solution
    print(a.merge(num1=[1], m=1, num2=[], n=0))
