import json
import urllib.request

with urllib.request.urlopen("http://www.thecocktaildb.com/api/json/v1/1/filter.php?i=Scotch") as response:

    print(response.geturl(), "\n")

    ##Get response status code and check for errors
    statusCode = response.getcode()
    print("Status Code Returned = <" ,statusCode, ">\n")

    #HTTP 200 Success.  Treat all others as failure
    if statusCode == 200:
        print("Success")

        #Get HTML response and decode from byte to string in order
        #for json to load properly
        html =  response.read().decode('utf-8')
        print("HTML return <",html,">\n")

        #Load json from HTML string
        json_data = json.loads(html)

        #print json data
        print(json_data['drinks'])
        
    #Return system code 1 if anything other that http 200 is returned
    else:
        print ("HTTP Status Code Failure =",statusCode)
        sys.exit(1)
        

    
 
    


    ##parsed_json = json.loads(html)



##print(parsed_json['drinks'])

