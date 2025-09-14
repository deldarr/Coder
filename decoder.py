from math import sqrt


def Decoder(code):
    code = float(code)
    number = decoder_number(code)
    number = int(number)

    # split ascii codes with 256
    number = str(number)
    ascii_list = list(number.split('256'))

    # convert ascii to chr
    ascii_list = map(int, ascii_list)
    chr_list = map(chr,ascii_list)

    # convert chr to string and join characters
    output = map(str, chr_list)
    output = ''.join(output)

    return output


def decoder_number(number):
    output = number
    output = output * 31
    output = output / 2
    output = output + 1532
    output = output * 332
    output = output * 300
    output = output / 6
    output = output - 6
    output = output + 3
    output = output / 3
    output = output + 34
    output = output / 7
    output = sqrt(output)
    return output