import string
def create_hashtag(input_string):
    words = ''.join(char for char in input_string if char not in string.punctuation).split()
    hashtag = '#' + ''.join(word.capitalize() for word in words)
    if len(hashtag) > 140:
        hashtag = hashtag[:140]
    return hashtag
user_input = input("Введіть рядок: ")
result = create_hashtag(user_input)
print(result)