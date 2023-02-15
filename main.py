# To improve this, I could:
# put a Try Except block before the return_binary function so that the input prompt recognises when the user 
# inputs hexadecimal characters.
# create a new function which converts hexadecimal into binary and denary. 


def match_binary_with_hex(half_byte):
    binary_set = ("0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011",
                  "1100", "1101", "1110", "1111")
    hexadecimal_set = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F")

    for sequence in binary_set:
        if half_byte == sequence:
            discovered_index = binary_set.index(sequence)
            return hexadecimal_set[discovered_index]


def return_hexadecimal(byte):
    return match_binary_with_hex(byte[:4]) + match_binary_with_hex(byte[4:])


def return_binary(integer):
    # returns a binary sequence when fed an integer under 256
    determine_binary = ["0", "0", "0", "0", "0", "0", "0", "0"]
    most_significant_bit = 128
    count = 0

    while integer >= 1:
        if integer >= most_significant_bit:
            determine_binary[count] = "1"
            integer -= most_significant_bit

        count += 1
        most_significant_bit //= 2

    return ''.join(determine_binary)


while True:
    user_input = (input("Enter a positive integer below 256 to convert to it to hexadecimal >"))
    print(f"Denary = {user_input}")
    print(f"Binary = {return_binary(int(user_input))}")
    print(f"Hexadecimal = {return_hexadecimal(return_binary(int(user_input)))}")
