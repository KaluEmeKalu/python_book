# Pens And Pencils both cost $2.
# You buy three pens and one pencil.
# What is your total?
pen = 2
pencil = 2
total = pen + pencil * 3
correct_order = pen + (pencil * 3)
incorrect_order = (pen + pencil) * 3
print("This is the default order of operations")
print(total)
print("This is the correct order of operations")
print(correct_order)
print("This is an  order of operations of the original question")
print(incorrect_order)