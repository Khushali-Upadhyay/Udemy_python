Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # If-condition
>>> totalMarks = 95
>>> if totalMarks >= 90:
	print("Conratulations! You have secured an 'A' grade")

	
Conratulations! You have secured an 'A' grade
>>> totalMarks = 80
>>> if totalMarks >= 90:
	print("Conratulations! You have secured an 'A' grade")

	
>>> # If- else condition
>>> if totalMarks >= 90:
	print("Congratulations! You have secured an 'A' grade")
else:
	print("You have cleared the examination")

	
You have cleared the examination
>>> # If-elif condition
>>> totalMarks = 60
>>> if totalMarks >= 90:
	print("Congratulations! You have secured an 'A' grade")
elif totalMarks >= 40:
	print("You have cleared the examination")

else:
	print("You have failed the examination")

	
You have cleared the examination
>>> totalMarks = 100
# Nested if
>>> if totalMarks >= 90:
	print("Congratulations! You have secured an 'A' grade")
	if totalMarks ==100:
		print("You have also secured full marks")

		
Congratulations! You have secured an 'A' grade
You have also secured full marks
>>> 
