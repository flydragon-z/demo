from django.test import TestCase

# Create your tests here.
# print(2**38)
# def isAnagram(s, t):
#     for i in s:
#         if i in t:
#             t = t.replace(i, '', 1)
#     if not t:
#         return True
#     else:
#         return False


# print(isAnagram('rat', 'cat'))
# print(isAnagram('anagram', 'nagaram'))


def isAnagram(s, t):
    if sorted(s) == sorted(t):
        return True
    else:
        return False

print(isAnagram('rat', 'cat'))