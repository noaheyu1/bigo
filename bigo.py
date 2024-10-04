"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Samuel Suh and Noah Yu, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: sjs5658
UT EID 2: ny3259
"""


def length_of_longest_substring_n3(s):
    """
    Finds the length of the longest substring without repeating characters
    using a brute force approach (O(N^3)).

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """

    maxlen = 0
    for start in range(len(s)):
        for current in range(start + 1, len(s) + 1):
            poss_str = s[start:current]  # generate a substring for any possibility
            repeat = False
            for p in range(len(poss_str) - 1):
                if poss_str[p] in poss_str[p + 1 :]:
                    repeat = True
                    break
            if not repeat and len(poss_str) > maxlen:
                maxlen = len(poss_str)
    return maxlen


def length_of_longest_substring_n2(s):
    """
    Finds the length of the longest substring without repeating characters
    using a frequency list approach (O(N^2)), converting each character to
    their corresponding numeric representation in ASCII as the index into the
    frequency list.

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """
    maxlen = 0
    len_s = len(s)
    for start in range(len_s):
        freqlst = [0] * 256  # create list of 256 zeros
        for current in range(start, len_s):
            char = ord(s[current])

            if freqlst[char] >= 1:  # check to see if it's in the list ~ test
                break

            freqlst[char] += 1

            if maxlen < (
                current + 1 - start
            ):  # determine the max length if test passes
                maxlen = current + 1 - start
    return maxlen


# TODO: implement this function. You may delete this comment when you are done.
def length_of_longest_substring_n(s):
    """
    Finds the length of the longest substring without repeating characters
    using a frequency list approach (O(N)), converting each character to
    their corresponding numeric representation in ASCII as the index into the
    frequency list. However, this approach stops early, breaking out of the inner
    loop when a repeating character is found. You may also choose to challenge
    yourself by implementing a sliding window approach.

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """
    maxlen = 0
    len_s = len(s)
    left = 0
    freqlst = [0] * 256  # create list of 256 zeros
    for right in range(len_s):
        char = ord(s[right])
        if freqlst[char] >= 1:  # check to see if it's in the list ~ test
            if maxlen < right - left:
                maxlen = right - left
            while s[left] != s[right]:  # catch up left index to move past right index
                freqlst[ord(s[left])] -= 1
                left += 1
            left += 1
        else:
            freqlst[char] += 1
    if maxlen < len_s - left:
        maxlen = len_s - left
    return maxlen
