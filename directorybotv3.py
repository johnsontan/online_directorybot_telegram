from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
import requests
import ast
from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urlparse
import lxml
import sys


bot = Updater(token='1230857962:AAHpuYePPMEXGITrhqvDi35SnkzYseImc3Y', use_context=True)

dispatcher = bot.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def search(update, context):
    reply_markup = ''
    query= ""
    returnMessage = ""
    context.args
    #context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    for k in context.args:
        query += " "
        query += k

    outputt = searchfordetails(query)
    keyboard = []
    try:
        for k, v in outputt.items():
            if(k.lower() == 'location'):
                try:
                    keyboard.append([InlineKeyboardButton("Location", url=v)])
                    reply_markup = InlineKeyboardMarkup(keyboard)
                except Exception as e:
                    pass
            elif(k.lower() == 'facebook'):
                try:
                    keyboard.append([InlineKeyboardButton(k, url=v)])
                    reply_markup = InlineKeyboardMarkup(keyboard)
                except Exception as e:
                    pass
            elif(k.lower() == 'youtube'):
                try:
                    keyboard.append([InlineKeyboardButton(k, url=v)])
                    reply_markup = InlineKeyboardMarkup(keyboard)
                except Exception as e:
                    pass
            elif(k.lower() == 'twitter'):
                try:
                    keyboard.append([InlineKeyboardButton(k, url=v)])
                    reply_markup = InlineKeyboardMarkup(keyboard)
                except Exception as e:
                    pass
            elif(k.lower() == 'instagram'):
                try:
                    keyboard.append([InlineKeyboardButton(k, url=v)])
                    reply_markup = InlineKeyboardMarkup(keyboard)
                except Exception as e:
                    pass
            elif(k.lower() == 'tumblr'):
                try:
                    keyboard.append([InlineKeyboardButton(k, url=v)])
                    reply_markup = InlineKeyboardMarkup(keyboard)
                except Exception as e:
                    pass
            elif(k.lower() == 'pinterest'):
                try:
                    keyboard.append([InlineKeyboardButton(k, url=v)])
                    reply_markup = InlineKeyboardMarkup(keyboard)
                except Exception as e:
                    pass
            elif(k.lower() == 'linkedin'):
                try:
                    keyboard.append([InlineKeyboardButton(k, url=v)])
                    reply_markup = InlineKeyboardMarkup(keyboard)
                except Exception as e:
                    pass
            elif(k.lower() == 'myspace'):
                try:
                    keyboard.append([InlineKeyboardButton(k, url=v)])
                    reply_markup = InlineKeyboardMarkup(keyboard)
                except Exception as e:
                    pass
            elif (isinstance(outputt[k], dict) and k.lower() == 'albums'):
                try:
                    returnMessage += '<b>Albums: </b>'
                    for ke, va in outputt[k].items():
                        returnMessage = returnMessage + ke + va + ' | '
                    returnMessage += '\n'
                except Exception as e:
                    pass
            elif (isinstance(outputt[k], dict) and k.lower() == 'movies'):
                try:
                    returnMessage += '<b>Movies: </b>'
                    for ke, va in outputt[k].items():
                        returnMessage = returnMessage + ke + va + ' | '
                    returnMessage += '\n'
                except Exception as e:
                    pass
            elif (isinstance(outputt[k], dict) and k.lower() == 'upcoming movies'):
                try:
                    returnMessage += '<b>Upcoming Movies: </b>'
                    for ke, va in outputt[k].items():
                        returnMessage = returnMessage + ke + va + ' | '
                    returnMessage += '\n'
                except Exception as e:
                    pass
            elif (isinstance(outputt[k], dict) and k.lower() == 'spouse'):
                try:
                    returnMessage += '<b>Spouse: </b>'
                    for ke, va in outputt[k].items():
                        returnMessage = returnMessage + ke + va + ' | '
                    returnMessage += '\n'
                except Exception as e:
                    pass
            elif (isinstance(outputt[k], dict) and k.lower() == 'children'):
                try:
                    returnMessage += '<b>Children: </b>'
                    for ke, va in outputt[k].items():
                        returnMessage = returnMessage + ke + va + ' | '
                    returnMessage += '\n'
                except Exception as e:
                    pass
            elif (isinstance(outputt[k], dict) and k.lower() == 'movies and tv shows'):
                try:
                    returnMessage += '<b>Movies and Tv Shows: </b>'
                    for ke, va in outputt[k].items():
                        returnMessage = returnMessage + ke + va + ' | '
                    returnMessage += '\n'
                except Exception as e:
                    pass
            elif (isinstance(outputt[k], dict) and k.lower() == 'characters'):
                try:
                    returnMessage += '<b>Characters: </b>'
                    for ke, va in outputt[k].items():
                        returnMessage = returnMessage + ke + va + ' | '
                    returnMessage += '\n'
                except Exception as e:
                    pass
            elif (isinstance(outputt[k], dict) and k.lower() == 'siblings'):
                try:
                    returnMessage += '<b>Siblings: </b>'
                    for ke, va in outputt[k].items():
                        returnMessage = returnMessage + ke + va + ' | '
                    returnMessage += '\n'
                except Exception as e:
                    pass
            elif (isinstance(outputt[k], dict) and k.lower() == 'tv shows'):
                try:
                    returnMessage += '<b>Tv Shows: </b>'
                    for ke, va in outputt[k].items():
                        returnMessage = returnMessage + ke + va + ' | '
                    returnMessage += '\n'
                except Exception as e:
                    pass
            elif (isinstance(outputt[k], dict) and k.lower() == 'screenplay'):
                try:
                    returnMessage += '<b>Screenplay: </b>'
                    for ke, va in outputt[k].items():
                        returnMessage = returnMessage + ke + va + ' | '
                    returnMessage += '\n'
                except Exception as e:
                    pass
            else:
                returnMessage = returnMessage + '<b>' + k +": </b>" + v +"\n" 
    except Exception as e:
        print(e.__class__)
    if(returnMessage):
        if(reply_markup):
            context.bot.send_message(chat_id=update.effective_chat.id, text=returnMessage, reply_markup=reply_markup,parse_mode='HTML')
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=returnMessage,parse_mode='HTML')     
    else:
        update.message.reply_text("Unable to find")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="To search for a business type /search 'Input'")

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Online Directory bot, to start type /help")


def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Search',
            input_message_content=InputTextMessageContent('/search '+ query)
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)


inline_handler = InlineQueryHandler(inline_caps)
help_handler = CommandHandler('help', help)    
start_handler = CommandHandler('start', start)
search_handler = CommandHandler('search', search)
dispatcher.add_handler(search_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(inline_handler)

bot.start_polling()


#Google
import csv, json, re, sys

headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

html_tags = {
    'knowledge_panel': 'kp-blk knowledge-panel Wnoohf OJXvsb',
    'claimed': "Own this business?",
    'name': "kno-ecr-pt kno-fb-ctx",
    'phone': 'LrzXr zdqRlf kno-fv',
    'days': "kc:/location/location:hours",
    'address': "kc:/location/location:address",
    'website': "IzNS7c duf-h",
    'founder': "LrzXr kno-fv"
}

def google(q):
    s = requests.Session()
    q = '+'.join(q.split())
    url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8&gl=sg'
    r = s.get(url, headers=headers_Get)
    return r.text

def searchfordetails(query):
    fieldnames = {}
    knowledgeP = ''
    #get html
    soup = BeautifulSoup(google(query), 'lxml')
    try:
        knowledgeP = soup.find('div', class_=['kp-blk knowledge-panel Wnoohf OJXvsb', 'kp-wholepage kp-wholepage-osrp HSryR EyBRub'])
    except Exception as e:
        print(e.__class__ + 'KNOWLEDGEP ERROR')


    #LOCAL BUSINESS & BUSINESS
    if(knowledgeP):
        #Business title
        title = knowledgeP.find('h2', attrs={'data-attrid':'title'})
        titleText = title.span.text
        if(titleText):
            fieldnames['Title'] = titleText

        #Company type
        try:
            type = knowledgeP.find('div', attrs={'data-attrid':'subtitle'})
            typeText = type.text
            if(type):
                fieldnames['Nature'] = typeText
        except Exception as e:
            print('Company type ERROR')

        #release date
        try:
            releaseDate = knowledgeP.find('div', attrs={'data-attrid': 'kc:/film/film:theatrical region aware release date'})
            if(releaseDate):
                releaseDatev2 = releaseDate.find('span', class_='LrzXr kno-fv')
                if(releaseDatev2):
                    releaseDateText = releaseDatev2.text
                    fieldnames['Release date'] = releaseDateText
        except Exception as e:
            print('Release Date ERROR')

        #initial release
        try:
            initialRelease = knowledgeP.find('div', attrs={'data-attrid':'kc:/film/film:initial theatrical regional release date'})
            if(initialRelease):
                initialReleasev2 = initialRelease.find('span', class_='LrzXr kno-fv')
                if(initialReleasev2):
                    initialReleaseText = initialReleasev2.text
                    fieldnames['Initial Release'] = initialReleaseText
        except Exception as e:
            print('Release Date ERROR')

        #director
        try:
            director = knowledgeP.find('div', attrs={'data-attrid':'kc:/film/film:director'})
            if(director):
                directorv2 = director.find('span', class_='LrzXr kno-fv')
                if(directorv2):
                    directorText = directorv2.text
                    fieldnames['Director'] = directorText
        except Exception as e:
            print('Director ERROR')     

        #producer
        try:
            producer = knowledgeP.find('div', attrs={'data-attrid':'kc:/film/film:producer'})
            if(producer):
                producerv2 = producer.find('span', class_='LrzXr kno-fv')
                if(producerv2):
                    producerText = producerv2.text
                    fieldnames['Producer'] = producerText
        except Exception as e:
            print('Producer ERROR') 
        
        #boxoffice
        try:
            boxoffice = knowledgeP.find('div', attrs={'data-attrid':'hw:/collection/films:box office'})
            if(boxoffice):
                boxofficev2 = boxoffice.find('span', class_='LrzXr kno-fv')
                if(boxofficev2):
                    boxofficeText = boxofficev2.text
                    fieldnames['Box office'] = boxofficeText
        except Exception as e:
            print('Box office ERROR')

        #budget
        try:
            budget = knowledgeP.find('div', attrs={'data-attrid':'kc:/film/film:budget'})
            if(budget):
                budgetv2 = budget.find('span', class_='LrzXr kno-fv')
                if(budgetv2):
                    budgetText = budgetv2.text
                    fieldnames['Budget'] = budgetText
        except Exception as e:
            print('Budget ERROR')

        #awards
        try:
            awards = knowledgeP.find('div', attrs={'data-attrid':'kc:/award/award_winner:awards'})
            if(awards):
                awardsv2 = awards.find('span', class_='LrzXr kno-fv')
                if(awardsv2):
                    awardsText = awardsv2.text
                    fieldnames['Awards'] = awardsText
        except Exception as e:
            print('Awards ERROR')
        
        #music composed by
        try:
            musicComp = knowledgeP.find('div', attrs={'data-attrid':'kc:/film/film:music'})
            if(musicComp):
                musicCompv2 = musicComp.find('span', class_='LrzXr kno-fv')
                if(musicCompv2):
                    musicCompText = musicCompv2.text
                    fieldnames['Music composed by'] = musicCompText
        except Exception as e:
            print('music composed by ERROR') 

        #nominations
        try:
            nominations = knowledgeP.find('div', attrs={'data-attrid':'kc:/award/award_winner:nominations'})
            if(nominations):
                nominationsv2 = nominations.find('span', class_='LrzXr kno-fv')
                if(nominationsv2):
                    nominationsText = nominationsv2.text
                    fieldnames['Nominations'] = nominationsText
        except Exception as e:
            print('Nominations ERROR') 

        #screenplay
        try:
            screenplay = knowledgeP.find('div', attrs={'data-attrid':'kc:/film/film:screenplay'})
            if(screenplay):
                screenplayv2 = screenplay.find('span', class_='LrzXr kno-fv')
                if(screenplayv2):
                    screenplayv3 = screenplayv2.find_all('a')
                    if isinstance(screenplayv3, list):
                        fieldnames['Screenplay'] = {}
                        for spv3 in screenplayv3:
                            screenplayText = spv3.text
                            fieldnames['Screenplay'][screenplayText] = ''
        except Exception as e:
            print('screenplay ERROR') 

        #Stock price
        stockText = ''
        try:
            stock = knowledgeP.find('div', attrs={'data-attrid':'kc:/business/issuer:stock quote'})
            if(stock):
                stockName = stock.find('span', class_='kno-fv')
                if(stockName):
                    stockName = stockName.find('a')
                    stockFrom = stock.find('span', class_='r3IKmc')
                    stockInfo = stock.find('span', text=re.compile('[$€₽₺₴د.إ₪₦]'))
                    stockFluc = stock.find('span', text=re.compile('[%]'))
                    if(stockName or stockFrom or stockInfo or stockFluc):
                        stockName = stockName.text
                        stockFrom = stockFrom.text
                        stockInfo = stockInfo.text
                        stockFluc = stockFluc.text
                        stockText = stockText + stockName + stockFrom +' '+ stockInfo + ' [' + stockFluc +']'
                        fieldnames['Stock'] = stockText
        except Exception as e:
            print('Stock ERROR')

        #Headquaters
        try:
            headquater = knowledgeP.find('div', attrs={'data-attrid':'kc:/organization/organization:headquarters'})
            if(headquater == None):
                headquater = knowledgeP.find('div', attrs={'data-attrid':'hw:/collection/organizations:garrison/hq'})
            if(headquater):
                headquaterv2 = headquater.find('span', class_='LrzXr kno-fv')
                if(headquaterv2):
                    headquaterText = headquaterv2.a.text
                    fieldnames['Headquater'] = headquaterText
        except Exception as e:
            print('Headquaters ERROR')

        #Founder
        founders=''
        try:
            founder = knowledgeP.find('div', attrs={'data-attrid':'kc:/business/business_operation:founder'})
            if(founder):
                founderv2 = founder.find('span', class_='LrzXr kno-fv')
                if(founderv2):
                    founderv3 = founderv2.find_all('a')
                    if(founderv3):
                        for f in founderv3:
                            founders = founders + f.text + ' | '
                        fieldnames['Founders'] = founders
        except Exception as e:
            print('Founders ERROR')

        #Founded
        try:
            founded = knowledgeP.find('div', attrs={'data-attrid':'kc:/organization/organization:founded'})
            if(founded):
                foundedv2 = founded.find('span', class_='LrzXr kno-fv')
                if(foundedv2):
                    dateFounded = foundedv2.text
                    fieldnames['Founded'] = dateFounded
                    if(foundedv2.a.text):
                        whereFounded = foundedv2.a.text
                        fieldnames['Founded'] = dateFounded + ' ' + whereFounded
                    
        except Exception as e:
            print('Founded ERROR')

        #CEO
        ceo = ''
        try:
            ceo = knowledgeP.find('div', attrs={'data-attrid':'hw:/collection/organizations:ceo'})
            if(ceo == None):
                ceo = knowledgeP.find('div', attrs={'data-attrid':'kc:/organization/organization:ceo'})
            if(ceo):
                ceov2 = ceo.find('span', class_='LrzXr kno-fv')
                if(ceov2):
                    ceov2 = ceov2.a.text
                    fieldnames['CEO'] = ceov2
        except Exception as e:
            print('CEO ERROR')

        #address
        try:
            address = knowledgeP.find('div', attrs={'data-attrid':'kc:/location/location:address'})
            addressv2 = address.find('span', class_='LrzXr')
            addressv2Text = addressv2.text
            if(addressv2Text):
                fieldnames['Address'] = addressv2Text
        except Exception as e:
            print('Address ERORR')

        #Revenue
        try:
            revenue = knowledgeP.find('div', attrs={'data-attrid':'hw:/collection/organizations:revenue'})
            if(revenue):
                revenuev2 = revenue.find('span', class_='LrzXr kno-fv')
                if(revenuev2):
                    fieldnames['Revenue'] = revenuev2.text
        except Exception as e:
            print('Revenue ERROR')

        #parentOrganization
        parentOrangizationText = ''
        try:
            parentOrangization = knowledgeP.find('div', attrs={'data-attrid':'hw:/collection/organizations:parent'})
            if(parentOrangization == None):
                parentOrangization = knowledgeP.find('div', attrs={'data-attrid':'hw:/collection/organizations:parent organization'})
            if(parentOrangization):
                parentOrangizationv2 = parentOrangization.find('span', class_='LrzXr kno-fv')
                if(parentOrangizationv2):
                    parentOrangizationv2 = parentOrangizationv2.find_all('a')
                    for po in parentOrangizationv2:
                        parentOrangizationText = parentOrangizationText + po.text + ' | '
                    fieldnames['Parent Organization'] = parentOrangizationText
        except Exception as e:
            print('Parent Organization ERROR')

        #subsidiaries
        subsidiariesText = ''
        try:
            subsidiaries = knowledgeP.find('div',attrs={'data-attrid':'hw:/collection/organizations:subsidiaries'})
            if(subsidiaries):
                subsidiariesv2 = subsidiaries.find('span', class_='LrzXr kno-fv')
                if(subsidiariesv2):
                    subsidiariesv2 = subsidiariesv2.find_all('a')
                    for sd in subsidiariesv2:
                        subsidiariesText = subsidiariesText + sd.text + ' | '
                    fieldnames['Subsidiaries'] = subsidiariesText
        except Exception as e:
            print('Subsidiaries ERROR')

        #Area served
        areaServedText = ''
        try:
            areaServed = knowledgeP.find('div', attrs={'data-attrid':'hw:/collection/organizations:area served'})
            if(areaServed):
                areaServedv2 = areaServed.find('span', class_='LrzXr kno-fv')
                if(areaServedv2):
                    areaServedv2 = areaServedv2.find_all('a')
                    for asv2 in areaServedv2:
                        areaServedText = areaServedText + asv2.text + ' | '
                    fieldnames['Area Served'] = areaServedText
        except Exception as e:
            print('Area served ERROR')

        #phone
        try:
            phone = knowledgeP.find('span', class_='LrzXr zdqRlf kno-fv')
            phoneText = phone.span.text
            if(phoneText):
                fieldnames['Phone'] = phoneText
        except Exception as e:
            print('PHONE ERROR')

        #Company website
        try:
            companyWebsite = knowledgeP.find('a', class_='B1uW2d ellip PZPZlf', attrs={'data-attrid':'visit_official_site'})
            if(companyWebsite):
                companyWebsitev2 = companyWebsite.find('span', class_='ellip')
                if(companyWebsitev2):
                    companyWebsiteText = companyWebsitev2.text
                    fieldnames['Website'] = companyWebsiteText
        except Exception as e:
            print('Company website ERROR')

        #number of employees
        try:
            employees = knowledgeP.find('div', attrs={'data-attrid':'hw:/collection/organizations:no of employees'})
            if(employees):
                employeesv2 = employees.find('span', class_='LrzXr kno-fv')
                if(employeesv2):
                    employeesText = employeesv2.text
                    fieldnames['No. of Employees'] = employeesText
        except Exception as e:
            print('employees ERROR')

        #website
        try:
            website = knowledgeP.find('div', class_='IzNS7c duf-h')
            if(website):
                websitev2 = website.find('a', string="Website")
                if(websitev2):
                    websitev2 = websitev2['href']
                    websitev2 = (str)(websitev2)
                    try:
                        start = websitev2.find('www.')
                        ending = websitev2.find('%2F&')
                        websiteText = websitev2[start:ending]
                    except Exception as e:
                        print(e.__class__ + 'has occurred.')
                    if(websiteText):
                        fieldnames['Website'] = websiteText
        except Exception as e:
            print('WEBSITE ERROR')

        #Location
        try:
            location = knowledgeP.find('div', class_='IzNS7c duf-h')
            if(location):
                locationv2 = location.find('a', string='Directions')
                if(locationv2):
                    locationv2 = locationv2['data-url']
                    locationv2 = (str)(locationv2)
                    locationText = 'www.google.com' + locationv2
                    fieldnames['Location'] = locationText
        except Exception as e:
            print('Location ERROR')

        #work hours
        workinghours = {}
        try:
            workhours = knowledgeP.find('div', attrs={'data-attrid':'kc:/location/location:hours'})
            wh = workhours.find('table', class_='WgFkxc')
            whv2 = wh.find_all('td')
            if(whv2):
                tempDays = []
                fieldnames['Hours'] =''
                for final in whv2:
                    de = final.text
                    tempDays.append(de)
                workinghours = {tempDays[i]: tempDays[i + 1] for i in range(0, len(tempDays), 2)}
        except Exception as e:
            print('working hours ERROR')

        #full name
        try:
            fullName = knowledgeP.find('div', attrs={'data-attrid':'kc:/people/person:full name'})
            if(fullName):
                fullNamev2 = fullName.find('span', class_='LrzXr kno-fv')
                if(fullNamev2):
                    fullNameText = fullNamev2.text
                    fieldnames['Full Name'] = fullNameText
        except Exception as e:
            print('full name ERROR')

        #born
        try:
            born = knowledgeP.find('div', attrs={'data-attrid':'kc:/people/person:born'})
            if(born):
                bornv2 = born.find('span', class_='LrzXr kno-fv')
                if(bornv2):
                    bornText = bornv2.text
                    fieldnames['Born'] = bornText
        except Exception as e:
            print('Born ERROR')

        #height
        try:
            height = knowledgeP.find('div', attrs={'data-attrid':'kc:/people/person:height'})
            if(height):
                heightv2 = height.find('span', class_='LrzXr kno-fv')
                if(heightv2):
                    heightText = heightv2.text
                    fieldnames['Height'] = heightText
        except Exception as e:
            print('Height ERROR')

        #networth
        try:
            networth = knowledgeP.find('div', attrs={'data-attrid':'kc:/people/person:height'})
            if(networth):
                networthv2 = networth.find('span', class_='LrzXr kno-fv')
                if(networthv2):
                    networthText= networthv2.text
                    fieldnames['Networth'] = networthText
        except Exception as e:
            print('Networth ERROR')

        #movies
        try:
            movies = knowledgeP.find('div', attrs={'data-attrid':'kc:/people/person:movies'})
            if(movies):
                moviesv2 = movies.find_all('div', class_='fl ellip oBrLN')
                if(not moviesv2):
                    moviesv3 = movies.find('span', class_='LrzXr kno-fv')
                
                if isinstance(moviesv2, list):
                    fieldnames['Movies'] = {}
                    for m in moviesv2:
                        movieText = m.text
                        fieldnames['Movies'][movieText] = ''
                if(moviesv3):
                    moviesv4 = moviesv3.find_all('a')
                    if(moviesv4):
                        fieldnames['Movies'] = {}
                        for mo in moviesv4:
                            movieTextv2 = mo.text
                            fieldnames['Movies'][movieTextv2] = ''
        except Exception as e:
            print('Movie ERROR') 

        #albums
        try:
            albums = knowledgeP.find('div', attrs={'data-attrid':'kc:/music/artist:albums'})
            if(albums):
                albumsv2 = albums.find_all('div', class_='fl ellip oBrLN')
                if(not albumsv2):
                    albumsv3 = albums.find('span', class_='LrzXr kno-fv')

                if isinstance(albumsv2, list):
                    fieldnames['Albums'] = {}
                    for k in albumsv2:
                        albumsText = k.text
                        fieldnames['Albums'][albumsText] = ''
                if(albumsv3):
                    fieldnames['Albums'] = {}
                    albumsv4 = albumsv3.find_all('a')
                    if(albumsv4):
                        for k in albumsv4:
                            albumsTextv2 = k.text
                            fieldnames['Albums'][albumsTextv2] = ''
        except Exception as e:
            print('Albums ERROR')
        
        #published
        try:
            published = knowledgeP.find('div', attrs={'data-attrid':'kc:/book/written_work:published'})
            if(published):
                publishedv2 = published.find('span', class_='LrzXr kno-fv')
                if(publishedv2):
                    publishedText = publishedv2.text
                    fieldnames['Originally Published'] = publishedText
        except Exception as e:
            print('Originally published ERROR')

        #author
        try:
            author = knowledgeP.find('div', attrs={'data-attrid':'kc:/book/written_work:author'})
            if(author):
                authorv2 = author.find('span', class_='LrzXr kno-fv')
                if(authorv2):
                    authorText = authorv2.a.text
                    fieldnames['Author'] = authorText
        except Exception as e:
            print('Author ERROR')

        #illustrator
        try:
            illustrator = knowledgeP.find('div', attrs={'data-attrid':'hw:/collection/written_works:illustrator'})
            if(illustrator):
                illustratorv2 = illustrator.find('span', class_='LrzXr kno-fv')
                if(illustratorv2):
                    illustratorv2 = illustratorv2.find_all('a')
                    if isinstance(illustratorv2, list):
                        fieldnames['Illustrator'] = {}
                        for illus in illustratorv2:
                            illustratorText = illus.text
                            fieldnames['Illustrator'][illustratorText] = ''
        except Exception as e:
            print('Illustrator ERROR')

        #publisher
        try:
            publisher = knowledgeP.find('div', attrs={'data-attrid':'hw:/collection/written_works:publisher'})
            if(publisher):
                publisherv2 = publisher.find('span', class_='LrzXr kno-fv')
                if(publisherv2):
                    publisherText = publisherv2.text
                    fieldnames['Publisher'] = publisherText
        except Exception as e:
            print('publisher ERROR')

        #original title
        try:
            originalTitle = knowledgeP.find('div', attrs={'data-attrid':'ss:/webfacts:origin_titl'})
            if(originalTitle):
                originalTitlev2 = originalTitle.find('span', class_='LrzXr kno-fv')
                if(originalTitlev2):
                    originalTitleText = originalTitlev2.text
                    fieldnames['Original Title'] = originalTitleText
        except Exception as e:
            print('original title ERROR')

        #page count
        try:
            pageCount = knowledgeP.find('div', attrs={'data-attrid':'hw:/collection/books:pages'})
            if(pageCount):
                pageCountv2 = pageCount.find('span', class_='LrzXr kno-fv')
                if(pageCountv2):
                    pageCountText = pageCountv2.text
                    fieldnames['Page count'] = pageCountText
        except Exception as e:
            print('page count ERROR') 

        #characters
        try:
            characters =  knowledgeP.find('div', attrs={'data-attrid':'kc:/book/book:characters'})
            if(characters == None):
                characters = knowledgeP.find('div', attrs={'data-attrid':'kc:/theater/play:characters'})
            if(characters):
                charactersv2 = characters.find('span', class_='LrzXr kno-fv')
                if(charactersv2):
                    charactersv2 = charactersv2.find_all('a')
                    if isinstance(charactersv2, list):
                        fieldnames['Characters'] = {}
                        for chara in charactersv2:
                            charactersText = chara.text
                            fieldnames['Characters'][charactersText] = ''
        except Exception as e:
            print('characters ERROR')

        #genres
        try:
            genres = knowledgeP.find('div', attrs={'data-attrid':'kc:/book/book:genre'})
            if(genres):
                genresv2 = genres.find('span', class_='LrzXr kno-fv')
                if(genresv2):
                    genresText = genresv2.text
                    fieldnames['Genres'] = genresText
        except Exception as e:
            print('genres ERROR')

        #adaptation
        try:
            adaptation = knowledgeP.find('div', attrs={'data-attrid':'kc:/media_common/adapted_work:adaptations'})
            if(adaptation):
                adaptationv2 = adaptation.find('span', class_='LrzXr kno-fv')
                if(adaptationv2):
                    adaptationText = adaptationv2.text
                    fieldnames['Adaptation'] = adaptationText
        except Exception as e:
            print('adaptation ERROR')
            
        #siblings
        try:
            siblings = knowledgeP.find('div', attrs={'data-attrid':'kc:/people/person:sibling'})
            if(siblings):
                siblingsv2 = siblings.find('span', class_='LrzXr kno-fv')
                if(siblingsv2):
                    siblingsv2 = siblingsv2.find_all('a')
                    if isinstance(siblingsv2, list):
                        fieldnames['Siblings'] = {}
                        for sib in siblingsv2:
                            siblingsText = sib.text
                            fieldnames['Siblings'][siblingsText] = ''
        except Exception as e:
            print('siblings ERROR')

        #music group
        try:
            musicGroup = knowledgeP.find('div', attrs={'data-attrid':'kc:/music/group_member:group'})
            if(musicGroup):
                musicGroupv2 = musicGroup.find('span', class_='LrzXr kno-fv')
                if(musicGroupv2):
                    musicGroupText = musicGroupv2.text
                    fieldnames['Music group'] = musicGroupText
        except Exception as e:
            print('music group ERROR')  

        #description
        try:
            description = knowledgeP.find('div', attrs={'data-attrid':'description'})
            if(description):
                descriptionv2 = description.find('div', class_='kno-rdesc')
                if(descriptionv2):
                    descriptionText = descriptionv2.find('span').text
                    fieldnames['Description'] = descriptionText
        except Exception as e:
            print('description ERROR')

        #Upcoming movie
        try:
            upcomingMovie = knowledgeP.find('div', attrs={'data-attrid':'kc:/people/person:upcoming movie'})
            if(upcomingMovie):
                upcomingMoviev2 = upcomingMovie.find('span', class_='LrzXr kno-fv')
                if(upcomingMoviev2):
                    upcomingMoviev2 = upcomingMoviev2.find_all('a')
                    if isinstance(upcomingMoviev2,list):
                        fieldnames['Upcoming movies'] = {}
                        for um in upcomingMoviev2:
                            upcomingMovieText = um.text
                            fieldnames['Upcoming movies'][upcomingMovieText] = ''
        except Exception as e:
            print('Upcoming movie ERROR')

        #spouse
        try:
            spouse = knowledgeP.find('div', attrs={'data-attrid':'kc:/people/person:spouse'})
            if(spouse):
                spousev2 = spouse.find('span', class_='LrzXr kno-fv')
                if(spousev2):
                    spousev3 = spousev2.find_all('a')
                    if(spousev3):
                        fieldnames['Spouse'] = {}
                        for sp in spousev3:
                            spouseText = sp.text
                            fieldnames['Spouse'][spouseText] = ''
        except Exception as e:
            print('Spouse ERROR')

        #children
        try:
            children = knowledgeP.find('div', attrs={'data-attrid':'kc:/people/person:children'})
            if(children):
                childrenv2 = children.find('span', class_='LrzXr kno-fv')
                if(childrenv2):
                    childrenv2 = childrenv2.find_all('a')
                    if isinstance(childrenv2, list):
                        fieldnames['Children'] = {}
                        for ch in childrenv2:
                            childrenText = ch.text
                            fieldnames['Children'][childrenText] = ''
        except Exception as e:
            print('Children ERROR')

        #movies and tv shows
        try:
            moviesnTv = knowledgeP.find('div', attrs={'data-attrid':'kc:/people/person:tv-shows-and-movies'})
            if(moviesnTv):
                moviesnTvv2 = moviesnTv.find_all('div', class_='fl ellip oBrLN')
                if isinstance(moviesnTvv2, list):
                    fieldnames['Movies and Tv Shows'] = {}
                    for mtv in moviesnTvv2:
                        print(mtv.text)
                        moviesnTvText = mtv.text
                        fieldnames['Movies and Tv Shows'][moviesnTvText] = ''
        except Exception as e:
            print('Movies and Tv Shows ERROR')

        #Tv shows
        try:
            tvShows = knowledgeP.find('div', attrs={'data-attrid':'kc:/people/person:tv shows'})
            if(tvShows):
                tvShowsv2 = tvShows.find('div', class_='zVvuGd MRfBrb')
                if(tvShowsv2):
                    tvShowsv2 = tvShowsv2.find_all('a')
                    if isinstance(tvShowsv2, list):
                        fieldnames['Tv shows'] = {}
                        for tvs in tvShowsv2:
                            tvShowsText = tvs['title']
                            fieldnames['Tv shows'][tvShowsText] = ''
        except Exception as e:
            print('Tv Shows ERROR')

        #socialMediaProfiles
        socialMediaProfilesDict = {}
        try:
            socialMediaProfiles = knowledgeP.find('div', attrs={'data-attrid':'kc:/common/topic:social media presence'})
            if(socialMediaProfiles):
                socialMediaProfilesv2 = socialMediaProfiles.find('div', class_='OOijTb')
                if(socialMediaProfilesv2):
                    socialMediaProfilesv2 = socialMediaProfilesv2.find_all('g-link')
                    for smp in socialMediaProfilesv2:
                        temp = smp.a['href']
                        tempName = smp.find('div', class_='CtCigf')
                        socialMediaProfilesDict[tempName.text] = temp
        except Exception as e:
            print('Social media profiles ERROR')

        if(workinghours):
            fieldnames.update(workinghours)
        if(socialMediaProfilesDict):
            fieldnames.update(socialMediaProfilesDict)
        return fieldnames
    else:
        print("Error")




