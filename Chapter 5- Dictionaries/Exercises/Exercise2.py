#Use programming words as the keys in your glossary, and store their meanings as values.
glossary = {
    'string': 'A sequence of characters.',
    'comment': 'Simple sentences that we use to make the code easier to understand which the Python interpreter ignores.',
    'list': 'A collection of items in a particular order and is changeable.',
    'control flow': 'The order in which individual statements, instructions, or function calls are executed or evaluated.',
    'dictionary': "A collection of key-value pairs.",
    }

#Print each word and its meaning.
word = 'string'
print(f"\n{word.title()}: {glossary[word]}")

word = 'comment'
print(f"\n{word.title()}: {glossary[word]}")

word = 'list'
print(f"\n{word.title()}: {glossary[word]}")

word = 'control flow'
print(f"\n{word.title()}: {glossary[word]}")

word = 'dictionary'
print(f"\n{word.title()}: {glossary[word]}")
