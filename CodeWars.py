# Bit Counting
# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
def count_bits(number):
    result = ''
    while int(number) > 0:
        divided = int(number) % 2
        result += str(divided)
        number = number / 2
    lst = list(result)
    return(lst.count('1'))



# Create Phone Number
# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
def create_phone_number(n):
    return f'({str(n[0])+str(n[1])+str(n[2])}) {str(n[3])+str(n[4])+str(n[5])}-{str(n[6])+str(n[7])+str(n[8])+str(n[9])}'



# Vowel Count
# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
def get_count(sentence):
    count = 0
    vowels  = 'aeiou'
    for i in sentence:
        if i in vowels:
            count += 1
    return(count)



# Find The Parity Outlier
# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
def find_outlier(integers):
    even = 0
    odd = 0
    for i in integers:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    for i in integers:
        if odd > even:
            if i % 2 == 0:
                return i
        else:
            if i % 2 != 0:
                return i
            


# Sum of two lowest positive integers
# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]



# Your order, please
# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
def order(sentence):
    sentence_splt = sentence.split()
    result_str = ''
    count = 1
    while count <= len(sentence_splt):
        for i in sentence_splt:
            if str(count) in i:
                count += 1
                result_str += i+' '
    return(result_str[:-1])


# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
                

# Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# Given a roman numeral, convert it to an integer.
class Solution(object):
    def romanToInt(self, num):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        final_num = 0
        prev_value = 0
        
        for char in reversed(num):
            value = roman_dict[char]
            if value < prev_value:
                final_num -= value
            else:
                final_num += value
            prev_value = value
        return final_num
    

# Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.
def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
        
        
# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
def longestCommonPrefix(self, strs):
        first_word = strs[0]
        for i in range(len(first_word)):
            for j in strs[1:]:
                if (i == len(j)) or j[i] != first_word[i]:
                    return first_word[0:i]
        return first_word


# Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
def isValid(self, s):
    l = []
    for i in s:
        if i in ['(','[','{']:
            l.append(i)
        else:
            length = len(l)
            if length>0:
                if i==')' and l.pop()=='(' or i==']' and l.pop()=='[' or i=='}' and l.pop()=='{':
                    pass
                else:
                    return False
            else: 
                return False
    if l==[]:
        return True
    else:
        return False
    

# Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
def lengthOfLastWord(self, s):
        return len(s.split()[-1])


# Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
def strStr(self, haystack, needle):
        x = haystack.find(needle)
        return x