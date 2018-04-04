quote = "Practice makes perfect"

substring1 = quote[0:8]
substring2 = quote[-7:]
substring3 = quote[9:14]
substring4 = substring2 + " " + substring1 + " " + substring3
substring5 = substring3 + " " + substring2 + " " + substring1
substring6 = substring1 + " " + substring3 + " " + substring2
substring7 = substring3 + " " + substring1 + " " + substring2

story = "I once heard that "
story += substring4 + " "
story += " the saying " + substring6 + " true. "
story += "So we must " + substring1 + " " + substring2
story += " to be " + substring2
story += "."

print(substring1) 
print(substring2)
print(substring3)
print(substring4)
print(substring5)
print(substring6)
print(substring7)
print(story)