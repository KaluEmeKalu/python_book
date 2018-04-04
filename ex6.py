string1 = 'How are you doing'

string2 = "You can create a string this way as well."
string3 = "Strings can also have numbers, like 23 414, and some symbols, like #$*&#"
intro1 = "Strings are used to display text that is meant for human eyes."
print("\n\nHere is the first intro 1")
print(intro1)
intro2 = " You can add one string to another string. "

# You can use intro1 in the assignment even though you are overriding it
intro1 = intro1 + intro2
# IT's very comment to see the same variable name on both sides
# of the equals sign like above. It's okay
# as long as that variable has already been created before

print("\n\nHere is string 1")
print(string1)
print("\n\n Here is string 2")
print(string2)
print("\n\n Here is string 3")
print(string3)
print("\n\n Here is the second intro 1")
print(intro1)
print("\n\n Here is intro2")
print(intro2)
