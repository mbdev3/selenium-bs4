from bs4 import BeautifulSoup 

with open('tailwind-landing-page-main/index.html','r',encoding="utf8") as html_file:
    content = html_file.read()
    # print(content)

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    tags = soup.find_all('h2')
    # for tag in tags:
    #     print(tag.text.strip())
    lists = soup.find_all(True, {'class':['flex', 'space-y-3']})
   
   
    new_list = []
    for list in lists:
        title = list.h3
        if title is not None:
            # print(title.text.strip())
            new_list.append(title.text.strip())

    # new_list = list(dict.fromkeys(new_list))
    
    new_list = set(new_list)
    my_list = [*new_list, ]
    print(my_list)
    l = []
    for i in new_list:
        l.append(i)
    print(l)
    
    