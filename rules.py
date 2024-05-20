def parser_rules(soup):




    
    MYBISNES = soup.find_all('a', class_="grid-card-item") + soup.find_all('div', class_="news_slide_date grid-description grid-title products__item products__item_white") 
    RB_CHANCE = soup.find_all('div', class_='chance__container')
    RB_NEWS = soup.find_all('a', class_="news-item__read-more") + soup.find_all('div', class_="news-item__text") 
    return RB_CHANCE + RB_NEWS + MYBISNES


#links = soup.find_all('a') + soup.find_all('b') + soup.find_all('li') + soup.find_all('p') + soup.find_all('span') + soup.find_all('string') chance__cards chance__cards-date chance__card-date-label chance__card-date-number-ng-binding
#.get("href")


