class Solution:
    def maxPower(self, s: str) -> int:
        n = len(s)

        # Initiate the count and max count
        count = 1
        max_count_so_far = 1

        for i in range(n - 1):
            # If swe see a repeated character
            if s[i] == s[i + 1]:
                # Increment the count
                count += 1
                # And check if we've got a new max count
                # max_count_so_far = max(count, max_count_so_far)
                if max_count_so_far<count:
                    char = s[i]
                    max_count_so_far=count


            else:
                # Otherwise, reset the count
                count = 1
                char=None

        return max_count_so_far,char

str1 = 'aaabbbbbbccbbdddddddddeeeeeeeffttttttttttgg'
obj = Solution()
print(obj.maxPower(str1))