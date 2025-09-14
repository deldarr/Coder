def Coder(text):

    # convert characters to ascii code
    ascii_list = list(map(ord, text))

    #convert int list to string list
    ascii_list = map(str, ascii_list)

    # join list item with 98(_) to each other and make a number
    code = '98'.join(ascii_list)
    number = int(code)

    output = coder_number(number)
    return output



def coder_number(number):
    return number