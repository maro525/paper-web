from bs4 import BeautifulSoup
import codecs

with open("hina.html") as inf:
    txt = inf.read()
    soup = BeautifulSoup(txt)

# soup = BeautifulSoup(infile)
# body = soup.new_tag('body')
body = soup.find('body')
# soup.insert(0, body)

with codecs.open('../txt/datadriven.txt', 'r', 'utf-8', 'ignore') as infile:
    for line in infile:
        p = soup.new_tag('p')
        p.string = line
        body.append(p)

with open('../datadriven.html', 'w') as outfile:
    outfile.write(soup.prettify())
