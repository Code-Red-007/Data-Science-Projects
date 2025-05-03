#*******************COMPLUSORY 2******************************
#Example 1:  This code prints out the poem.
poem = ("The!quick!brown!fox!jumps!over!the!lazy!dog!")
print(poem)
#*********END OF CODE*****************************************
#Example 2:  This code replaces "!" with blank spaces.
poem = ("The!quick!brown!fox!jumps!over!the!lazy!dog!")
new_poem = poem.replace ("!"," ")
print (new_poem)
#**************End of Code**********************************
#Example 3: This code converts the string to Upper Case
NEW_POEM = new_poem.upper()  
print(NEW_POEM) 
#****************End of Code*************************************
#Example 4:  This code reverses each letter in the sentence (using lower case)
reverse_new_poem = new_poem [::-1]
print (reverse_new_poem)
#*****************End of Code******************************************
#Example 5:  This code reverses each word in the sentence
reverse_sentence_new_poem = new_poem.split()
rev_sen_new_poem = reverse_sentence_new_poem [::-1]
revised_rev_sen_new_poem = rev_sen_new_poem = " ".join(rev_sen_new_poem)
print(revised_rev_sen_new_poem)
#****************End of the Code************************************************