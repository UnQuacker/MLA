import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords


class TextReader:
    lemmatizer = WordNetLemmatizer()

    def __readFileString(self, name):
        with open(name) as load_file:
            text = load_file.read()
            return text

    def getText(self, name):
        stop_words = set(stopwords.words('english'))
        stop_words.add("the")
        raw_text = self.__readFileString(name)
        processed_text = []
        raw_text = self.__lemmatize_sentence(raw_text)
        for raw_line in raw_text:
            line = re.sub("[^a-zA-Z]+", "", raw_line)
            line = line.lower()
            if line != '' and line not in stop_words:
                processed_text.append(line)

        return processed_text

    def __nltk_pos_tagger(self, nltk_tag):
        if nltk_tag.startswith('J'):
            return wordnet.ADJ
        elif nltk_tag.startswith('V'):
            return wordnet.VERB
        elif nltk_tag.startswith('N'):
            return wordnet.NOUN
        elif nltk_tag.startswith('R'):
            return wordnet.ADV
        else:
            return None

    def __lemmatize_sentence(self, text):
        nltk_tagged = nltk.pos_tag(nltk.word_tokenize(text))
        wordnet_tagged = map(lambda x: (x[0], self.__nltk_pos_tagger(x[1])), nltk_tagged)
        lemmatized_sentence = []

        for word, tag in wordnet_tagged:
            if tag is None:
                lemmatized_sentence.append(word)
            else:
                lemmatized_sentence.append(self.lemmatizer.lemmatize(word, tag))
        return lemmatized_sentence

