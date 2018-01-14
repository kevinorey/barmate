import json

class Cocktail:
    cocktailId = 0
    cocktailName = ""

    def function(self):
        print("Entered Cocktail Constructor")

    def setCockTailId(self, inputId):
        print("Input Id = ", inputId)

        #Check to see if value is an integer
        if isinstance(inputId, int):
            print("Input is a number")

            #Value must be greater than 0
            if inputId > 0:
                print("Input number is greater than 0")
                self.cocktailId = inputId

            #Raise Exception value less than or equal to 0
            else:
                print("Input number is less than or equal to 0")
                raise ValueError("Input number is less than or equal to 0")

        #Invalid input
        else:
            print("Invalid input must be an integer")
            raise ValueError("Invalid input must be an integer")
                

    def getCockTailId(self):
        return self.cocktailId;


def main():
    print("Entered Main")
    x = Cocktail()
    print("id = ", x.getCockTailId())
    x.setCockTailId(100)
    print("id = ", x.getCockTailId())
    print("Leaving Main")

main()
