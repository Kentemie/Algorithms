# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is 
# fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when 
# necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly
# between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# Note:

    # A word is defined as a character sequence consisting of non-space characters only.
    # Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    # The input array words contains at least one word.

def fullJustify(words, maxWidth):
    def get_words(i):
        curr_line = []
        curr_length = 0

        while i < len(words) and curr_length + len(words[i]) <= maxWidth:
            curr_line.append(words[i])
            curr_length += len(words[i]) + 1
            i += 1
        
        return curr_line

    def create_line(line, i):
        base_length = -1

        for word in line:
            base_length += len(word) + 1

        extra_spaces = maxWidth - base_length

        if len(line) == 1 or i == len(words):
            return " ".join(line) + " " * extra_spaces
        
        word_count = len(line) - 1
        spaces_per_word, needs_extra_space = divmod(extra_spaces, word_count)

        for j in range(needs_extra_space):
            line[j] += " "

        for j in range(word_count):
            line[j] += " " * spaces_per_word
        
        return " ".join(line)

    res = []
    i = 0

    while i < len(words):
        curr_line = get_words(i)
        i += len(curr_line)
        res.append(create_line(curr_line, i))
    
    return res

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

res = fullJustify(words, maxWidth)
print(res)