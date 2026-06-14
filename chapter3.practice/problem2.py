# fill in a letter template in given below 

letter = '''Dear <|Name|>,
            You are selected!
            <|Date|>'''

print(letter.replace("<|Name|>","Aakriti").replace("<|Date|>","30 august 2007")) #using replace() method to replace the placeholders with actual values. 