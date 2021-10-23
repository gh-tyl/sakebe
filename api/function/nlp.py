import os
import re
import nltk
import MeCab
import pandas as pd
from sklearn.feature_extraction import text
from DictionaryServices import DCSGetTermRangeInString, DCSCopyTextDefinition

class Cleasing:
    def __init__(self):
        # stopwords english ver.
        self.stop_words_en = text.ENGLISH_STOP_WORDS
        self.stop_words_EN = [word.upper() for word in self.stop_words_en]
        self.stop_words_EN_Cap = [word.capitalize() for word in self.stop_words_en]
        self.stop_words_en_nltk = nltk.corpus.stopwords.words('english')
        self.stop_words_EN_nltk = [word.upper() for word in self.stop_words_en_nltk]
        self.stop_words_EN_Cap_nltk = [word.capitalize() for word in self.stop_words_en_nltk]
        addstopwords = ["BA", "English", "Hibernate", "STAY", "SURU"]
        self.stopwords = self.stopwordslist_creation(addstopwords)
        self.elim = ['数', '接尾', '非自立']
        self.part = ['名詞', '動詞', '形容詞']

    #形態素解析
    def parsewithelimination(self, sentense):
        mecab = MeCab.Tagger(os.environ['MECAB_PATH'])
        sentence = mecab.parse(sentense)
        sentence = sentence.split('\n')
        sentence = [s.split(',') for s in sentence]
        sentence = [s[0].split('\t') + s[1:] for s in sentence]
        # 単語の解析結果以外を消去
        sentence = [s for s in sentence if len(s) > 2]
        # 品詞指定
        sentence = [s for s in sentence if any([z == s[1] for z in self.part])]
        # 採用しない語を除去
        sentence = [s for s in sentence if not any([z == s[2] for z in self.elim])]
        # 実際に出現した単語を取得
        # orginal_word = [s[0] for s in sentence]
        # 単語の原型を取得
        origin_word = [s[7] for s in sentence] 
        # ストップワード除去
        result = [x for x in origin_word if not x in self.stopwords]  
        return result

    #ストップワードの作成
    def stopwordslist_creation(self, stopwordlist):
        stopwords=[]
        with open('./stopwords/stopwords.txt', 'r') as f:
            words = f.readlines()
            for line in words:
                line = line.replace('\n', '')
                if not line==u'':
                    stopwords.append(line)
        stopwords.extend(stopwordlist)
        stopwords.extend(self.stop_words_en)
        stopwords.extend(self.stop_words_EN)
        stopwords.extend(self.stop_words_EN_Cap)
        stopwords.extend(self.stop_words_en_nltk)
        stopwords.extend(self.stop_words_EN_nltk)
        stopwords.extend(self.stop_words_EN_Cap_nltk)        
        return stopwords

    def delete_brackets(self, s):
        # 括弧と括弧内文字列を削除
        # brackets to zenkaku
        table = {"(": "（", ")": "）", "<": "＜", ">": "＞", "{": "｛", "}": "｝", "[": "［", "]": "］"}
        for key in table.keys():
            s = s.replace(key, table[key])
        # delete zenkaku_brackets
        l = ['（[^（|^）]*）', '【[^【|^】]*】', '＜[^＜|^＞]*＞', '［[^［|^］]*］',
            '「[^「|^」]*」', '｛[^｛|^｝]*｝', '〔[^〔|^〕]*〕', '〈[^〈|^〉]*〉']
        for l_ in l:
            s = re.sub(l_, " ", s)
        # recursive processing
        return self.delete_brackets(s) if sum([1 if re.search(l_, s) else 0 for l_ in l]) > 0 else s