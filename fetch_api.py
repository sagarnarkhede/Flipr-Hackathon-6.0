import requests


contacts_url = 'https://api.rootnet.in/covid19-in/contacts'
notifications_url = 'https://api.rootnet.in/covid19-in/notifications'

def fetch_data_contacts(url):
    result = requests.get(url)
    #print(result.status_code)
    #print(result.text)
    data = result.json()
    #print(data)

    #print('Let\'s make the data more simplify')

    #print(data['data']['contacts'])
    #print(type(data)) data is in a form of dictionary

    regionals_dict = {}
    primary_contacts = data['data']['contacts']['primary']
    regional_contacts = data['data']['contacts']['regional']
    #print(regional_contacts)
    #print(type(regional_contacts))
    print('State Name'+'\t\t'+'Helpline Number')
    for item in regional_contacts:
        #print(item['loc']+'\t\t'+item['number'])
        regionals_dict[item['loc']]=item['number']

    return regionals_dict

def fetch_data_notifications(url):
    result = requests.get(url)
    data = result.json()

    date_dict = {}
    notification_dict = {}
    notification = data['data']['notifications']
    i = 0
    for item in notification:
        title = item['title']
        if len(title.split()[0]) == 10 and title[6:8]=='20':
            date = title[0:10]
            date_dict[str(i)] = date
            notification_dict[title[11:]] = item['link']
            i+=1

    return (date_dict, notification_dict)


#print(fetch_data_contacts(contacts_url))
print(fetch_data_notifications(notifications_url))
