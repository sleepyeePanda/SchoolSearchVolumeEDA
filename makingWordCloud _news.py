from konlpy.tag import Twitter
from collections import Counter
import pytagcloud
import os
import glob

# 현재 디렉터리
CURRENT_DIRECTORY = os.path.join(os.getcwd(),'news')

def make_wordcloud(news_file):
    nouns_tagger = Twitter()
    with open(news_file,'r', encoding='utf-8') as filereader:
        text = filereader.read()
        nouns = nouns_tagger.nouns(text)
        count = Counter(nouns)
        ranked_tags = count.most_common(40)
        taglist = pytagcloud.make_tags(ranked_tags, maxsize=80)
        pytagcloud.create_tag_image(taglist, 'wordcloud_news.jpg', size=(900, 600), fontname='NanumBarunGothic', rectangular=False)
# INPUT_FILE = 'news_cleaned.txt'
# filereader = open(INPUT_FILE, 'r', newline='')
# word_corpus = str(filereader.readlines())
# filereader.close()

# nouns_tagger = Twitter()
# nouns = nouns_tagger.nouns(word_corpus)
# count = Counter(nouns)
# ranked_tags = count.most_common(40)
# taglist = pytagcloud.make_tags(ranked_tags, maxsize=80)
# pytagcloud.create_tag_image(taglist, 'wordcloud.jpg', size=(900, 600), fontname='NanumBarunGothic', rectangular=False)

def main():
    for news_file in glob.glob(os.path.join(CURRENT_DIRECTORY,'*')):
        with open(news_file, 'r',encoding='utf-8') as filereader:
            text = filereader.read()
        with open('all.txt','a',encoding='utf-8') as filewriter:
            filewriter.write(text)
    make_wordcloud('all.txt')

if __name__=='__main__':
    main()