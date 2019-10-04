import requests
from bs4 import BeautifulSoup
import json

def UserProfile(username):  
    headers = {
        'Authorization' : 'token d543f91e99801f8d99f8bb77ced568ee5d644732'
    }

    url = "https://api.github.com/users/" +username
    detail = requests.get(url,headers=headers)
    return detail.text

def UserDetail(username):
    headers = {
        'Authorization' : 'token d543f91e99801f8d99f8bb77ced568ee5d644732'
    }
    
    url = "https://api.github.com/users/"+username+"/repos"
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.text, 'lxml')

    li = soup.find('p')
    new=json.loads(str(li.text))
    data = list()
    for i in range(0,len(new)):
        url = new[i]['url']
        page = requests.get(url,headers=headers)
        soup = BeautifulSoup(page.text,'lxml')
        temp = soup.find('p').text
        content = dict()
        content['owner'] = username
        lst =  ('name', 'owner.login', 'owner.type', 'description', 'created_at', 'updated_at', 'pushed_at', 'stargazers_count', 'watchers_count', 'language', 'open_issues', 'default_branch', 'subscribers_count')
        for i in temp[1:len(temp)-1].split(','):
            if i.split(':')[0].lower().strip('"') in lst:
                content[i.split(':')[0].strip('"')] = i.split(':')[1].strip('"')
        data.append(content)
        del content
    return data
