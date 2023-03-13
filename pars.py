import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


# print(get_html('https://kaktus.media/?lable=8&date=2023-03-13&order=time'))

def get_new_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    description_list = soup.find('div', class_='Article--text').text
    # print(description_list)
    return description_list

def get_description(html):
    soup = BeautifulSoup(html, 'lxml')
    description = []
    count = 0
    for news in soup.find_all('a', class_='ArticleItem--name'):
        count += 1
        if count == 21:
            break

        description_link = news.get('href')
        # print(description_link)
        description.append(get_new_page_data(get_html(description_link)))

    # print(description)
    return description


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    news_list = soup.find('div', class_='Tag--articles').find_all('div', class_='Tag--article')
    # print(news_list)
    list_title = []
    global list_img
    list_img = []
    count = 0
    for news in news_list:
        count += 1
        if count == 21:
            break
        title = news.find('a', class_='ArticleItem--name').text
        # print(title)
        list_title.append(title.replace('\n', ''))
        img = news.find('img').get('src')
        list_img.append(img)
    return list_title
    # print(list_img)

# get_data(get_html('https://kaktus.media/?lable=8&date=2023-03-13&order=time'))

def main():
    from datetime import datetime
    current_date = datetime.now()
    # print(current_date.month)
    url = f'https://kaktus.media/?lable=8&date={current_date.year}-{current_date.month}-{current_date.day}&order=time'
    print(current_date)
    html = get_html(url)
    global titles
    global descriptions
    titles = get_data(html)
    descriptions = get_description(html)


# print(__name__)

main()
