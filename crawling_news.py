import sys
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
from collections import Counter
import pandas as pd

BASE_URL='http://www.daejonilbo.com/ksearch/search.asp?'
KEYWORD_URL = 'kwd='
REST_URL='&xwd=&pageNum=1&pageSize=10&category=NEWS&subCategory=00&reSrchFlag=false&sort=d&searchRange=a&detailSearch=false&detailDate=0&startDate=&endDate=&srchFd=all&paperNum=&PDFpaperNum=&startHit=&sliderCheck=40&groupsearch=all&preKwd='

# get 뉴스 링크
def get_newslink(page_start_num, page_end_num, URL):
    print(URL)
    for i in range(page_start_num,page_end_num+1):
        current_page_num = i
        URL_with_page_num = URL.replace('&pageNum=1','&pageNum='+str(current_page_num))
       # urlopen() : 봇으로 인식하므로 header 추가
        request = urllib.request.Request(URL_with_page_num,headers={'User-Agent': 'Mozilla/5.0'})
        source_code_from_URL = urllib.request.urlopen(request).read()
        soup = BeautifulSoup(source_code_from_URL, 'html.parser',from_encoding='utf-8')
        print(i)
        for ultag in soup.find_all('ul', 'list_df cate_documents'):
            atag_list = ultag.select('a')
            newslink_list = [atag['href'] for atag in atag_list]
            for index, newslink in enumerate(newslink_list):
                # get 뉴스 텍스트
                get_news(newslink, 'news/news'+str((i-1)*10 + index)+'.txt')
 
# get 뉴스
def get_news(URL, output_file):
    request = urllib.request.Request(URL,headers={'User-Agent': 'Mozilla/5.0'})
    source_code_from_url = urllib.request.urlopen(request).read()
    soup = BeautifulSoup(source_code_from_url, 'html.parser', from_encoding='utf-8')
    news = soup.find(id='fontSzArea').get_text()
    with open(output_file, 'w',encoding='utf-8') as filewriter:
        filewriter.write(news)
 
def main():
    # 검색 단어
    keyword = '%B4%EB%B4%F6%BC%D2%C7%C1%C6%AE%BF%FE%BE%EE%B8%B6%C0%CC%BD%BA%C5%CD%B0%ED'
    # 검색 페이지
    page_start_num=1
    page_end_num =4
    '''
    대전일보 1~4pages
    '''
    # URL 합성
    TARGET_URL = BASE_URL + KEYWORD_URL+ keyword+REST_URL+keyword
    # get 뉴스 링크
    get_newslink(page_start_num, page_end_num, TARGET_URL)
 
 
if __name__ == '__main__':
    main()

