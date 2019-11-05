from textblob import TextBlob

if __name__ == '__main__':

    blob = TextBlob(input('Enter your text: '))

    #Analysis Choice
    print (' 1. Sentiment Analysis\n 2. Part of Speech Breakdown \n 3. Extract Noun Phrases \n 4. Translate')
    choice =  input('Enter the number of your analysis choice ')

    #Text Sentiment Analysis
    if choice == '1':
        for sentence in blob.sentences:
            print(sentence.sentiment)

    #Part of Speech Breakdown
    elif choice == '2':
        print(blob.tags)

    # Extract Noun Phrases
    elif choice == '3':
        for np in blob.noun_phrases:
            print('Noun phrase:', np)

    # Text Translation
    elif choice == '4':
        from_lang = input('Enter the language to be translated from: ')
        to_lang = input('Enter the language to be translated to: ')
        print(blob.translate(from_lang, to_lang))
