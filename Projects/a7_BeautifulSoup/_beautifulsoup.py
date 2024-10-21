from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First WebSite</title>
</head>

<body>
    <!-- header label -->
    <h1 id = "header">
        Mehmet Nuri Başa
    </h1>

    <!-- create a group -->
    <div class = "group 1">
        <h2>
            Python Course
        </h2>

        <!-- list label -->
        <ul>
            <!-- element of list -->
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>
        </ul>
    </div>
    
    <div class = "group 2">
        <h2>
            C Course
        </h2>

        <!-- list label -->
        <ul>
            <!-- element of list -->
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>
        </ul>
    </div>

    <img src="pyt.jpeg" alt="">

    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>

</body>

</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser') #Parse(analyze) this html file.

result = soup.prettify()    #Fix this html file.
result = soup.title
result = soup.head
result = soup.body

result = soup.title.name
result = soup.title.string

result = soup.h1
result = soup.h2

result = soup.find_all("h2")
result = soup.find_all("h2")[1]


result = soup.div
result = soup.find_all("div")
result = soup.find_all("div")[1].ul
result = soup.find_all("div")[1].ul.find_all("li")

result = soup.div.findChildren()

result = soup.div.findNextSibling().findPreviousSibling()

# print(result)

result = soup.find_all("a")
for link in result:
    # print(link)
    print(link.get("href"))
