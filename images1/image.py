import urllib.request

def takuma(url, file_path, file_name):
    full_path = file_path+file_name+'.jpg'
    urllib.request.urlretrieve(url,full_path)

url = input('enter image url')

file_name =input('enter file name')

takuma(url, '___', file_name)
