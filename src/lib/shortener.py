import requests

def tinyurl(url):
    response = requests.get(f'http://tinyurl.com/api-create.php?url={url}')
    return response.text