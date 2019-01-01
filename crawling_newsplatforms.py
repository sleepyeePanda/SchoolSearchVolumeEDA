from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
from collections import Counter
import pandas as pd

BASE_URL='https://search.naver.com/search.naver?&where=news'
KEYWORD_URL = '&query='
REST_URL='&sm=tab_pge&sort=1&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&start=1&refresh_start=0'

# get 기사의 뉴스 플랫폼
def get_newsplatforms_from_news_title(page_start_num,page_end_num, URL):
    with open('data/2018/newsplatforms_2018.txt', 'w',encoding='utf8') as filewriter:
        newsplatform_list = []
        for i in range(page_start_num-1,page_end_num):
            # 페이지 번호 = 이전 페이지 수 * 페이지 당 기사수 + 1
            current_page_num = i*10+1
            URL_with_page_num = URL.replace('1',str(current_page_num))
            # urlopen() : 봇으로 인식하므로 header 추가
            request = urllib.request.Request(URL_with_page_num,headers={'User-Agent': 'Mozilla/5.0'})
            source_code_from_URL = urllib.request.urlopen(request).read()
            soup = BeautifulSoup(source_code_from_URL, 'html.parser',from_encoding='utf-8')
            # get 뉴스 플랫폼 태그 텍스트
            newsplatform_list.extend([newsplatform.get_text() for newsplatform in soup.find_all('span', '_sp_each_source')])
            print(i)
        filewriter.write(','.join(newsplatform_list))
            
# count 뉴스 플랫폼 수
def count_newsplatform():
    with open('data/2018/newsplatforms_2018.txt', 'r',encoding='utf8') as filereader:
        newsplatform_list=filereader.readline().split(',')
        sr = pd.Series(Counter(newsplatform_list))
        # 내림차순으로 정렬
        # inplace=True : same as sr = sr.sort_values(ascending=False)
        sr.sort_values(inplace=True, ascending=False)
        sr.to_csv('data/2018/newsplatforms_2018_count.csv')
 
def main():
    # 검색 단어
    keyword = '대덕소프트웨어마이스터고'
    # 검색 페이지
    page_start_num=1
    page_end_num =10
    '''
    2018년도 1~10page
    2017년도 11~27page
    2016년도 28~41page
    2015년도 42~66page
    '''
    # URL 합성
    TARGET_URL = BASE_URL + KEYWORD_URL+ quote(keyword)+REST_URL
    # get 기사의 뉴스 플랫폼
    get_newsplatforms_from_news_title(page_start_num, page_end_num, TARGET_URL)
    # count 뉴스 플랫폼 수
    count_newsplatform()
 
if __name__ == '__main__':
    main()
