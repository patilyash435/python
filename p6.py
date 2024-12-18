percentage = float(input("Enter your percentage: "))

if percentage >= 75:
    grade = 'O grade'
elif percentage >= 60:
    grade = 'A grade'
elif percentage >= 50:
    grade = 'B grade'
elif percentage >= 40:
    grade = 'C grade'
else:
    grade = 'Failed'

print(f"Your grade is: {grade}")
