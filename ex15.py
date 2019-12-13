from sys import argv

script, filename = argv

txt = open(filename)

print("Here's you file {}".format(filename))
print(txt.read())
txt.close()

prompt = "> "
print("Type the filename again:")
filename_again = input(prompt)

txt_again = open(filename_again)
print(txt_again.read())
txt_again.close()
