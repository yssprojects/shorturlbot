import requests as r
main_url = 'https://url-shorten-api.vercel.app/create?u='
long_url = input('Enter Long URL \n')
if 'http' in long_url:
    url = main_url+long_url
    res = r.get(url).json()
    ide = res['unique_id']
    print("http://127.0.0.1:5000/"+ide)