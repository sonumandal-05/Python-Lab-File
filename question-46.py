# 2.Once, Ram was playing a game with his brother. He asked him to extract all vowels present in a given sentence and 
# store in a list. Can you help his brother to do it by a Python program? 



sentence = input("Enter a sentence: ")
vowels = [char for char in sentence if char.lower() in 'aeiou']
print("Vowels in the sentence:", vowels)
