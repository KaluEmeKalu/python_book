exam_grades = [80, 93, 85, 94]
students = ['Eke', 'Jordan', 'Uche', 'Nnenna']
gpas = [3.8, 3.6, 3.33, 4.0]

text1 = "\n\nHi "
text2 = ". This is Professor Obama. Congratulations on finishing your Constitutional Law exam. "
text3 = "Your final grade was a "
text4 = ". Now your gpa is a "

eke_story = text1 + students[0] + text2 + text3
eke_story += str(exam_grades[0]) + text4 + str(gpas[0])

jordan_story = text1 + students[1] + text2 + text3
jordan_story += str(exam_grades[1]) + text4 + str(gpas[1])

uche_story = text1 + students[2] + text2 + text3
uche_story += str(exam_grades[2]) + text4 + str(gpas[2])

nnenna_story = text1 + students[3] + text2 + text3
nnenna_story += str(exam_grades[3]) + text4 + str(gpas[3])


print(eke_story)
print(jordan_story)
print(uche_story)
print(nnenna_story)