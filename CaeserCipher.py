import argparse

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
            result += chr(shifted)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            shifted = (ord(char) - ord('A') - shift) % 26 + ord('A')
            result += chr(shifted)
        else:
            result += char
    return result

def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher Program")
    parser.add_argument('shift', type=int, help='The shift for the Caesar cipher')
    parser.add_argument('--encrypt', '-e', action='store_true', help='Encrypt the file')
    parser.add_argument('--decrypt', '-d', action='store_true', help='Decrypt the file')
    parser.add_argument('filename', type=str, help='The name of the file to encrypt or decrypt')

    args = parser.parse_args()

    try:
        with open(args.filename, 'r') as file:
            content = file.read()

        if args.encrypt:
            result = caesar_encrypt(content, args.shift)
            output_filename = args.filename.replace('.txt', '_encrypted.txt')
        elif args.decrypt:
            result = caesar_decrypt(content, args.shift)
            output_filename = args.filename.replace('.txt', '_decrypted.txt')
        else:
            print("Please specify --encrypt or --decrypt.")
            return

        with open(output_filename, 'w') as file:
            file.write(result)

        print(f"Operation successful! Output saved to {output_filename}")

    except FileNotFoundError:
        print(f"Error: File '{args.filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
