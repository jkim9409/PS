# Example 1: input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
#                     banned = ["hit"]
#             output: ["ball"]
#
# Example 2: input: paragraph = "a"
#                     banned = []
#             output:"a"
#
# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
#
# The words| in paragraph are case-insensitive and the answer should be returned in lowercase.


def  mostCommonWord(paragraph:str, banned:[str]) -> str:
    import re
    import collections
    words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]

input1 = "Bob hit a ball, the hit BALL flew far after it was hit."
banned1 = ["hit"]

input2 = "a"
banned2 = []

print(mostCommonWord(input1,banned1))
print(mostCommonWord(input2,banned2))

#comment: need to review General Expression, and the "collections" lib