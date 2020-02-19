import nltk
from flask import Flask, request, render_template, jsonify
from textblob import TextBlob, Word
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('brown')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import brown

app = Flask(__name__)


@app.route('/nlp', methods=['GET'])
def nlp_guidance():
    try:
        return render_template('guidance.html')
    except Exception as e:
        return str(e)


@app.route('/nlp/<int:service>', methods=['GET', 'POST'])
def nlp_service(service):
    try:
        if request.method == 'POST':
            json_temp = {'input': request.json['input']}
            json_input_blob = json_temp['input']
            blob = TextBlob(json_input_blob)
            if service == 1:
                try:
                    class Sentiment:
                        def __init__(self,sentence):
                            self.sentence = sentence
                            self.sentence_list = []
                            self.sentiment_list = []
                            self.final_sentiment_list = []
                        def sentiment_add(self):
                            for self.sentence in blob.sentences:
                                self.sentence_list.append(self.sentence)
                                sentiment = self.sentence.sentiment
                                self.sentiment_list.append(sentiment)
                            for i in range(len(self.sentence_list)):
                                self.final_sentiment_list.append('Word or Sentence {}'.format(i + 1)
                                                                 + ' ({})'.format(self.sentence_list[i])
                                                                 + ': {}.'.format(self.sentiment_list[i]))
                            return jsonify({'Sentiment Analysis of ({})'.format(blob): 
                                            str(self.final_sentiment_list).strip('[]')})
                    final_sentiment = Sentiment(blob)
                    return final_sentiment.sentiment_add()
                except Exception as e:
                    return str(e)
            elif service == 2:
                try:                    
                    SpeechBreakdown = blob.tags
                    return jsonify({"The Parts of Speech breakdown is as shown for ({})".format(blob): str(SpeechBreakdown)})    
                except Exception as e:
                    return str(e)
            elif service == 3:
                try:
                     NP_Extract = blob.noun_phrases
                     return jsonify({'Noun-Phrase Extraction Results ({})'.format(blob):str(NP_Extract)})
                except Exception as e:
                    return str(e)
            elif service == 4:
                try:
                    from_lang = blob.detect_language()
                    to_lang_temp = {'to_lang': request.json['to_lang']}
                    to_lang = to_lang_temp['to_lang']
                    translation = blob.translate(str(from_lang),str(to_lang))
                    return jsonify ({'Translation of ({})'.format(blob) + ', from {}'.format(str(from_lang))
                             + ' to {}'.format(str(to_lang)): str(translation)})
                except Exception as e:
                    return str(e)
            elif service == 5:
                try:
                    correction = blob.correct()
                    return jsonify({'Spelling Correction of ({})'.format(blob): str(correction)})
                except Exception as e:
                    return str(e)
            elif service == 6:
                try:
                    lemmatization = blob.words.lemmatize()
                    return jsonify({'Lemmatization of ({})'.format(blob): str(lemmatization)})
                except Exception as e:
                    return str(e)
            else:
                return render_template('service_error.html')
        else:
            if service == 1:
                return render_template('service_1.html')
            elif service == 2:
                return render_template('service_2.html')
            elif service == 3:
                return render_template('service_3.html')
            elif service == 4:
                return render_template('service_4.html')
            elif service == 5:
                return render_template('service_5.html')
            elif service == 6:
                return render_template('service_6.html')
            else:
                return render_template('service_error.html')
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
