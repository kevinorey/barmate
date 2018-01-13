import json

class Cocktail:
    cocktailId = 0
    cocktailName = ""

    def function(self):
        print("Entered Cocktail Constructor")

    def setCockTailId(self, inputId):
        print("Input Id = ", inputId)
        if isinstance(inputId, int):
            print("Input is a number")
            if inputId > 0:
                print("Input number is greater than 0")
                self.cocktailId = inputId
            else:
                print("Input number is less than or equal to 0")
        else:
            print("Invalid input must be an integer")

                
                
##        if inputId.isalpha():
##            print("Invalid input:  Input must be an integer")
##        elif inputId.isdigit():
##            print("Input is a number... checking valid ranges")
##            if ( inputId > 0 ):
##                self.cocktailId = inputId
##            else:
##                print("Input is less than or equal to 0")
                

    def getCockTailId(self):
        return self.cocktailId;


def main():
    print("Entered Main")
    x = Cocktail()
    print("id = ", x.getCockTailId())
    x.setCockTailId(0)
    print("id = ", x.getCockTailId())
    print("Leaving Main")

main()
