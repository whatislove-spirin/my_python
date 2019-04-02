def read_url(url):
    import urllib.request
    try:
        with urllib.request.urlopen(url) as webpage:
            text = webpage.read().decode('utf-8')
        return text
    except Exception as e: 
        return e

def histogram(s):
    '''
    Функция для подсчета встречаемости элементов в коллекции.

    s - последовательность
    '''
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

text = read_url("http://dfedorov.spb.ru/python3/src/romeo.txt")
words_freq = histogram(text.split())
for i in words_freq:
    print(i+': '+str(words_freq[i]))
