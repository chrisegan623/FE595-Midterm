from textblob import TextBlob

def NLP(blob, choice):

    # Text Sentiment Analysis
    if choice == '1':
        for sentence in blob.sentences:
            result = sentence.sentiment

    # Text Translation
    elif choice == '2':
        from_lang = input('Enter the language to be translated from: ')
        to_lang = input('Enter the language to be translated to: ')
        result = blob.translate(from_lang, to_lang)

    return (print(result))


if __name__ == '__main__':
    blob = TextBlob(input('Enter your text: '))
    print(' 1. Sentiment Analysis\n 2. Part of Speech Breakdown \n 3. Extract Noun Phrases \n 4. Translate')
    choice = input('Enter the number of your analysis choice ')

    NLP(blob,choice)
