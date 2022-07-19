# select the text from Project Gutenberg https://gutenberg.org/ to analyze
# use count() to find how many times a word appears in a string
# write a program that reads the file and counts how many times the word 'the' appears in the file
# this is an approximate count as it will also count 'then' and 'there'
# then try counting 'the' with a space in the string and see how much lower your count is

# open the file, use UTF, it is used when your system's default encouding does not match the file's encoding
with open('the_untamed_by_george_pattullo.txt', encoding='utf-8') as f:
    try:
        content = f.read()
    except FileNotFoundError:
        print("Sorry, the file cannot be opened.")
    else:
        words_v1 = content.lower().count('the')
        print(f"The approximate 'the' word count in The Untamed by George Pattulo is {words_v1}.")

        words_v2 = content.lower().count('the ')
        print(f"The approximate 'the ' word count with a space in 'the' in The Untamed by George Pattulo is {words_v2}.")
        
        difference = words_v1 - words_v2
        print(f"The difference between the word count of 'the' without a space and 'the ' with the space is: {difference} words.")
    
