# import gensim
from gensim.models import word2vec
from .nlp import *
nlp=NLP()

class LC:
    def __init__(self):
        self.words_model=word2vec.Word2Vec.load("media/model/model.model")

    def letter_classification(text):
        word2vec_model = gensim.models.KeyedVectors.load_word2vec_format(
            'model/model.vec', binary=False)

        # sample = nlp.parsewithelimination(text)

        # for sentence in sample:

        #     for token in tokenizer.tokenize(sentence):
        #         noun = token.part_of_speech.split(',')[0]
        #         if noun in noun_list:
        #             for word in word_list:
        #                 if word in word_score:
        #                     word_score[word] += word2vec_model.similarity(
        #                         token.surface, word)
        #                 else:
        #                     word_score[word] = word2vec_model.similarity(
        #                         token.surface, word)

        # print("###一番高いトピック###")
        # print(max(word_score, key=word_score.get))

        # return max(word_score, key=word_score.get)
