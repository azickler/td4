import requests
from bs4 import BeautifulSoup



# selection par balise 
# print(soup.p)
# print(soup.find_all('p'))

# selection par regex 
# print(soup.find(re.compile(r'..')))


# selection de classe css 
# print(soup.find_all('nomdebalise',class_="nomdeclasse")



# Exercice 2 : 

UNI = requests.get("http://www.univ-orleans.fr")
soup = BeautifulSoup(UNI.text, "lxml")
print(soup.h1)
print(soup.find_all('div'))
print(soup.find_all('img'))
print(soup.find_all('a'))
print(soup.find('div', class_='composite-zone'))


# Exercice 3 :

UNI = requests.get("https://stackoverflow.com/questions/tagged/beautifulsoup")
soup = BeautifulSoup(UNI.text, "lxml")
listQuestion=[]
listCountPost=[]
listAnswer=[]

for node in soup.findAll(class_='question-hyperlink',limit=10):
    listQuestion.append(''.join(node.findAll(text=True)))

for node in soup.findAll(class_='vote-count-post ',limit=10):
    listCountPost.append(''.join(node.findAll(text=True)))

for node in soup.findAll(class_='status',limit=10):
    listAnswer.append(''.join(node.findAll(text=True))[1])

with open('data.csv','w') as file :
    file.write('Questions ; Votes ; Réponses ;')
    file.write('\n')
    for i in range(len(listAnswer)):
        file.write('"'+listQuestion[i]+'"; "'+listCountPost[i]+'"; "'+listAnswer[i]+'";')
        file.write('\n') 
     
# Exercice 4 :

data = {"submit-form": "", "catalog": "catalogue-2015-2016", "degree": "DP"}
r = requests.post(
    "http://formation.univ-orleans.fr/fr/formation/rechercher-une-formation.html#nav", data=data)
formations = []
soup = BeautifulSoup(r.text, "lxml")
for node in soup.find_all('li', class_='hit'):
    for formation in node.findAll('strong'):
        formations.append(''.join(formation.findAll(text=True)))
print(formations)




# Exercice 5 : 

def get_definition(x):
    URL ='http://services.aonaware.com/DictService/Default.aspx?action=define&dict=wn&query={0}'.format(x)
    html = requests.get(URL).text
    soup = BeautifulSoup(html, "lxml")
    definitions=[]
    for node in soup.find_all('pre',attrs={"class":None}):
        definitions.append(''.join(node.findAll(text=True)))
    return definitions

lines=[]
with open('vocabulary.txt') as f:
    lines=f.readlines() 

with open('definitions.txt','w') as d:
    for mot in lines:
        d.write(get_definition(mot)[0])
