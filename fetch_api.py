import requests


contacts_url = 'https://api.rootnet.in/covid19-in/contacts'
notifications_url = 'https://api.rootnet.in/covid19-in/notifications'
hospitals_beds_url = 'https://api.rootnet.in/covid19-in/hospitals/beds' 
medical_colleges_url = 'https://api.rootnet.in/covid19-in/hospitals/medical-colleges'


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

    date_list = []
    title_list = []
    link_list = []
    notification = data['data']['notifications']
    i = 0
    for item in notification:
        title = item['title']
        if len(title.split()[0]) == 10 and title[6:8]=='20':
            date = title[0:10]
            date_list.append(date)
            #date_dict[str(i)] = date
            #notification_dict[title[11:]] = item['link']
            title_list.append(title[11:])
            link_list.append(item['link'])
            i+=1

    return (date_list, title_list, link_list)

def fetch_data_hospitals_beds(url):
    result = requests.get(url)
    data = result.json()

    regional = data['data']['regional']
    s_l = []
    rh_l = []
    rb_l = []
    uh_l = []
    ub_l = []
    th_l = []
    tb_l = []
    for item in regional:
        s_l.append(item['state'])
        rh_l.append(item['ruralHospitals'])
        rb_l.append(item['ruralBeds'])
        uh_l.append(item['urbanHospitals'])
        ub_l.append(item['urbanBeds'])
        th_l.append(item['totalHospitals'])
        tb_l.append(item['totalBeds'])

    return (s_l, rh_l, rb_l, uh_l, ub_l, th_l, tb_l)


def fetch_data_medical_colleges(url):
    result = requests.get(url)
    data = result.json()

    medical_colleges = data['data']['medicalColleges']
    state_l = []
    name_l = []
    city_l = []
    own_l = []
    ac_l = []
    hb_l = []
    for item in medical_colleges:
        state_l.append(item['state'])
        name_l.append(item['name'])
        city_l.append(item['city'])
        own_l.append(item['ownership'])
        ac_l.append(item['admissionCapacity'])
        hb_l.append(item['hospitalBeds'])

    return (state_l, name_l, city_l, own_l, ac_l, hb_l)

#print(fetch_data_contacts(contacts_url))
#print(fetch_data_notifications(notifications_url))
#print(fetch_data_hospitals_beds(hospitals_beds_url))
#print(fetch_data_medical_colleges(medical_colleges_url))
