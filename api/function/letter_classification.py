import gensim

def letter_classification(text):
    word2vec_model = gensim.models.KeyedVectors.load_word2vec_format(
        'model/model.vec', binary=False)

    sample = [text]
    noun_list = ["動詞", "形容詞", "名詞"]
    word_list = ["良い", "悪い", "仕事", "恋愛", "夢", "愚痴", "未来", "過去", "願望"]

    tokenizer = Tokenizer()
    word_score = {}

    for sentence in sample:

        for token in tokenizer.tokenize(sentence):
            noun = token.part_of_speech.split(',')[0]
            if noun in noun_list:
                for word in word_list:
                    if word in word_score:
                        word_score[word] += word2vec_model.similarity(
                            token.surface, word)
                    else:
                        word_score[word] = word2vec_model.similarity(
                            token.surface, word)

    # print(word_score)
    print("###一番高いトピック###")
    print(max(word_score, key=word_score.get))

    return max(word_score, key=word_score.get)
