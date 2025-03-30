#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 

with open("words.txt", "r") as file:
    words = file.read().splitlines()

palindromes = [word for word in words if word == word[::-1]]

palindrome_count = len(palindromes)

print(f"There are {palindrome_count} palindromes.")
