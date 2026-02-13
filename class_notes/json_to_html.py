from json2html import json2html
import json

with open('C:\\Users\\karth\\Downloads\\test1-1770519756962.json') as fobj:
	data = json.load(fobj)

html_result = json2html.convert(json=data)

with open("test.html","w") as wobj:
	wobj.write(html_result)
