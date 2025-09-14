def Coder(text):

    # convert characters to ascii code
    ascii_list = list(map(ord, text))

    #convert int list to string list
    ascii_list = map(str, ascii_list)

    # join list item with 256 to each other and make a number
    code = '256'.join(ascii_list)
    number = int(code)

    output = coder_number(number)
    return output



def coder_number(number):
    output = number
    output = output * output
    output = output *  7
    output = output - 34
    output = output * 3
    output = output - 3
    output = output + 6
    output = output  * 6
    output = output  / 300
    output = output  / 332
    output = output  - 1532
    output = output * 2
    output = output / 31
    return output