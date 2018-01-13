import json
import urllib.request

with urllib.request.urlopen("http://www.thecocktaildb.com/api/json/v1/1/filter.php?i=Scotch") as response:

    print(response.geturl(), "\n")

    ##Get response status code and check for errors
    statusCode = response.getcode()
    print("Status Code Returned = <" ,statusCode, ">\n")

    if statusCode == 200:
        print("Success")

        ##Get HTML from response
        #html = response.read().decode(response.headers.get_content_charset())

        #response.decode('utf-8')

        #Get HTML response and decode from byte to string in order
        #for json to load properly
        html =  response.read().decode('utf-8')
        print("HTML return <",html,">\n")

        #Load json from HTML string
        json_data = json.loads(html)
    else:
        print ("Failure")
        

    
 
    


    ##parsed_json = json.loads(html)



##print(parsed_json['drinks'])

