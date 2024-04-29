def apply_operations(input_string, operation):
    result = ""
    for char in input_string:
        if operation == "AND":
            result += chr(ord(char) & 127)
        elif operation == "XOR":
            result += chr(ord(char) ^ 127)
    return result

def main():
    input_string = "\\Hello World"
    print("Original string:", input_string)
    
    and_result = apply_operations(input_string, "AND")
    xor_result = apply_operations(input_string, "XOR")
    
    print("After AND operation with 127:", and_result)
    print("After XOR operation with 127:", xor_result)

if __name__ == "__main__":
    main()
