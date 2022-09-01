#Write a program that will compute the area of a rectangle. Prompt the user to enter the width and height of the rectangle. Print a nice message with the answer.
width = input("what is the width of the rectangle?")
length = input("what is the length of the rectangle?")
width_int = int(width)
length_int = int(length)
area = width_int * length_int
print("Amazing! The area of the rectangle is", area)