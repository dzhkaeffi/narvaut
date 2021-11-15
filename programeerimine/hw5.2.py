url = input("Please enter url: ")
print('Username is {}'.format(url[url.find("~")+1:url.find("/", url.find("~")+1)]))