from coder import Coder

print('For coding, enter 1')
print('For decoding, enter 2')

user_input = input(': ')
if user_input != '1' and user_input != '2':
    print('Invalid input')
    exit()

if user_input == '1':
    text = input('Enter your text:')
    output = Coder(text)
    print(output)

elif user_input == '2':
    pass




