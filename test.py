import re

def extract_last_set(input_string):
    # Regular expression to match sets in Python format
    pattern = re.compile(r'\{[^{}]*\}')
    
    # Find all matches of the pattern in the input string
    matches = pattern.findall(input_string)
    
    # If there are matches, return the last one; otherwise, return None
    return matches[-1] if matches else None

# Example usage
input_string = """To determine which pictures are visible when the book is closed, I need to analyze the arrangement of the objects inside and how they would appear based on the holes in the cover.\n\n1. The book cover has holes that correspond to specific items in the book.\n2. The objects I can see in the provided image are:\n   - Pear\n   - Ginger\n   - Apple\n   - Banana\n   - Watermelon\n\nWhen the book is closed, only the parts of the objects that align with the holes will be visible.\n\nBased on the sequence of the objects listed, the visible items through the holes when the book is closed will be:\n\n- The pear\n- The ginger\n- The apple\n- The banana\n- The watermelon\n\nUsing this information, the resulting set of words that represent the visible pictures when the book is closed would be:\n\n{pear, ginger, apple, banana, watermelon}\n\nThus, the answer is:\n\nANSWER: pear, ginger, apple, banana, watermelon"""

last_set = extract_last_set(input_string)
translation = str.maketrans('', '', '{}"\'[] ')
answer = last_set.translate(translation).strip().split(",")
print(set(answer))  # Output: {7, 8, 9}