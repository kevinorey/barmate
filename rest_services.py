import json
##from urllib.request import urlopen

import urllib.request
with urllib.request.urlopen("http://www.thecocktaildb.com/api/json/v1/1/filter.php?i=Scotch") as response:
    print(response.geturl())
    print(response.getcode())
    html = response.read()
    print(html)


##parsed_json = json.loads(html)



##print(parsed_json['drinks'])

