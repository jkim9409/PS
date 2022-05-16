class Solution:
    # def isValid_lecture(self, s:str) -> bool:
    #     pair = {'(':')',
    #             '[':']',
    #             '{':'}'
    #             }
    #     opener = '([{'
    #     stack = []
    #
    #     for char in s:
    #         if char in opener:
    #             stack.append(char)
    #         else:
    #             if not stack:
    #                 return False
    #             top = stack.pop()
    #             if pair[top] != char:
    #                 return False
    #     return not stack


    def valid(self, s:str) -> bool:
        pair = {
            '{':'}',
            '[':']',
            '(':')'
        }

        opener = '[({'
        stack = []
        for char in s:
            if char in opener:
                stack.append(char)

            else:
                if not stack:
                    return False
                if pair[stack.pop()] != char:
                    return False

        return not stack

ans1 = Solution().valid('[()][{}{}][]')
print(ans1)