'''
Ask the user to type in the first line of a nursery rhyme and
display the length of the string. Ask for a starting number and an
ending number and then display just that section of the text
(remember Python starts counting from 0 and not 1).
'''

#Solution

rhyme = input("Enter the first line of a nursery rhyme: ")

print(f"The length of the text is: {len(rhyme)}")

start = int(input("Enter a starting number: "))
end = int(input("Enter an ending number: "))

print("Selected text:")
print(rhyme[start:end])
