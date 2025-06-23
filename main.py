import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import countwords

from stats import countcharacters

from stats import sort_characters

text = get_book_text(sys.argv[1])

wordcount = countwords(text)

charactercount = countcharacters(text)

sorted_characters = sort_characters(charactercount)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("------------ Word Count ----------")
print(f"Found {wordcount} total words")
print("--------- Character Count -------")
for i in range(31):
    print(f"{sorted_characters[i]["char"]}: {sorted_characters[i]["num"]}")
print("============= END ===============")