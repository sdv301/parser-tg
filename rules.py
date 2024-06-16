def parser_rules(soup):
    # smbn = 
    # anti_krizes = 
    # grant_modoly = 
    # lgot_kredit =
    mspbank = soup.find_all('div', class_="inner-page__inner")
    #fasie = soup.find_all('div', class_="page-content") + soup.find_all('div', class_="wrap") 
    Services_sk = soup.find_all('div', class_="page-content") + soup.find_all('div', class_="page-section__main-text") + soup.find_all('div', class_="page-content-wrapper")
    #kontur = soup.find_all('div', class_="section-block__content")
    #MYBISNES_podeshka = 
    invest_Yakutia =  soup.find_all('div', class_="static__page")
    Yakutia = soup.find_all('div', class_="tmpl-contentblock")
    MYBISNES = soup.find_all('a', class_="grid-card-item") + soup.find_all('div', class_="news_slide_date grid-description grid-title products__item products__item_white") 
    RB_CHANCE = soup.find_all('div', class_='chance__container')
    RB_NEWS = soup.find_all('a', class_="news-item__read-more") + soup.find_all('div', class_="news-item__text") 
    return RB_CHANCE + RB_NEWS + MYBISNES + Yakutia + invest_Yakutia + Services_sk + mspbank


#links = soup.find_all('a') + soup.find_all('b') + soup.find_all('li') + soup.find_all('p') + soup.find_all('span') + soup.find_all('string') chance__cards chance__cards-date chance__card-date-label chance__card-date-number-ng-binding
#.get("href")


