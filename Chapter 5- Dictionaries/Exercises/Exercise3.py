#add five more Python terms and their meanings in the glossary.
glossary = {
    'string': 'A sequence of characters.',
    'comment': 'Simple sentences that we use to make the code easier to understand which the Python interpreter ignores.',
    'list': 'A collection of items in a particular order and is changeable.',
    'control flow': 'The order in which individual statements, instructions, or function calls are executed or evaluated.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'loop': 'Work through a collection of items, one at a time.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    'variable': 'value that may vary.',
    }

#Print each word and its meaning.
for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")