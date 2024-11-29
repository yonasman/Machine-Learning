from bs4 import BeautifulSoup

html_doc = """
<html>
    <head><title>Sample Page</title></head>
    <body>
        <p class="intro">Hello, World!</p>
        <p>Hello yoni</p>
        <a href="http://example.com" id="link1">Example Link</a>
    </body>
</html>
"""
# parse the html doc
soup = BeautifulSoup(html_doc,'html.parser')
# access the elements
# print(soup.title.text)
# print(soup.p['class'])
# print(soup.find('p'))
# print(soup.find_all('p'))
# find by class name
# print(soup.find('p',class_='intro'))
# manipulate the document
# soup.p.string = "NOW WAY"
# print(soup.p.string)
# adding a new element
new_tag = soup.new_tag('h1')
new_tag.string = 'welcome to this home'
soup.body.append(new_tag)
# print(soup.body)
print(soup.get_text())