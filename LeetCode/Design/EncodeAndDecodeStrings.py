# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and 
# is decoded back to the original list of strings.

# Constraints:

    # 1 <= strs.length <= 200
    # 0 <= strs[i].length <= 200
    # strs[i] contains any possible characters out of 256 valid ASCII characters.


class Escaping:
    """
    This approach uses escaping technique.

    1. If we see //:, it means /: was part of a string, not a delimiter. The first slash is the escape character and what
       comes after it is the contents of the string.
    2. If we see /:, it must be a delimiter, because if it wasn't then it would have been escaped to //:.

    """
    def encode(self, strs):
        encoded_string = []

        for ss in strs:
            escaped_string = []
            for char in ss:
                escaped_string.append(char)
                if char == '/':
                    escaped_string.append('/')
            encoded_string.append(''.join(escaped_string)) 

        return '/:'.join(encoded_string)
    
    def decode(self, s):
        decoded_strings = []
        current_string = []
        i = 0

        while i <= len(s):
            if s[i:i+2] == '/:' or i == len(s):
                decoded_strings.append(''.join(current_string))
                current_string = []
                i += 2
            elif s[i:i+2] == '//':
                current_string.append('/')
                i += 2
            else:
                current_string.append(s[i])
                i += 1

        return decoded_strings 
    


class ChunkedTransferEncoding:
    """
    Chunked Transfer Encoding.

    Chunked transfer encoding is a method used in data communication protocols to send data in self-contained chunks,
    each of which is accompanied by its length or size.

    In our encoding process, instead of just joining all the strings together with a delimiter, we would precede each string 
    with its length, followed by a delimiter, and then the string itself. This way, even if our string contains the delimiter, 
    we can correctly identify the string boundaries.

    """
    def encode(self, strs):
        encoded_string = []

        for ss in strs:
            encoded_string.append(str(len(ss)) + '/:' + ss)
        
        return ''.join(encoded_string)
    
    def decode(self, s):
        decoded_strings = []
        i = 0

        while i < len(s):
            delimiter_pos = s.find('/:', i)
            length = int(s[i:delimiter_pos])
            decoded_strings.append(s[delimiter_pos+2 : delimiter_pos+2+length])
            i = delimiter_pos + 2 + length
            
        return decoded_strings
        

strs = ["Hello", "World/:", "How/are you?"]

encoder1 = Escaping()
encoder2 = ChunkedTransferEncoding()

encoded1 = encoder1.encode(strs)
encoded2 = encoder2.encode(strs)

print(encoded1)
print(encoded2)
print("--------------")
print(encoder1.decode(encoded1))
print(encoder2.decode(encoded2))