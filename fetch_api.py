import requests


contacts_url = 'https://api.rootnet.in/covid19-in/contacts'

def fetch_data_contacts(url):
    result = requests.get(url)
    #print(result.status_code)
    #print(result.text)
    data = result.json()
    #print(data)

    #print('Let\'s make the data more simplify')

    #print(data['data']['contacts'])
    #print(type(data)) data is in a form of dictionary

    primary_contacts = data['data']['contacts']['primary']
    regional_contacts = data['data']['contacts']['regional']
    #print(regional_contacts)
    #print(type(regional_contacts))
    print('State Name'+'\t\t'+'Helpline Number')
    for item in regional_contacts:
        print(item['loc']+'\t\t'+item['number'])


fetch_data_contacts(contacts_url)
