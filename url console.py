from http.client import HTTPConnection
conn=HTTPConnection('https://www.google.com/')
conn.request("GET",'/')
result=conn.getresponse()
conents=result.read()
print(conents)
