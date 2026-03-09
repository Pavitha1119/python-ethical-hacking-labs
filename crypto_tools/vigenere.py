def vigenere(text, keyword, mode):
    result = ""
    keyword = keyword.lower()
    key_index = 0  # Tracks position in the keyword — only advances for alpha characters

    for char in text:
        if char.isalpha():

            # Determine the shift from the current keyword character
            shift = ord(keyword[key_index % len(keyword)]) - ord('a')

            # Preserve the original case of the character
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            # Apply shift for encode, reverse shift for decode
            if mode == "encode":
                new_char = chr((ord(char) - base + shift) % 26 + base)
            elif mode == "decode":
                new_char = chr((ord(char) - base - shift) % 26 + base)

            # Append result
            result += new_char

            # Advance key_index only here
            key_index += 1

        else:
            result += char  # Non-alpha characters are passed through unchanged

    return result


mode = input("Mode (encode/decode): ").strip().lower()
message = input("Enter message : ")
keyword = input("Enter keyword : ").strip()

if mode == "encode":
    print(f"\nEncoded: {vigenere(message, keyword, 'encode')}")
elif mode == "decode":
    print(f"\nDecoded: {vigenere(message, keyword, 'decode')}")
else:
    print("[!] Invalid mode.")