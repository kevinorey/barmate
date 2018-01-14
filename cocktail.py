import json

class Cocktail:
    drinkID = 0
    name = ""
    imageURL = ""

    def setDrinkID(self, inputId):
        print("Input Id = ", inputId)

        #Check to see if value is an integer
        if isinstance(inputId, int):
            print("Input is a number")

            #Value must be greater than 0
            if inputId > 0:
                print("Input number is greater than 0")
                self.drinkID = inputId

            #Raise Exception value less than or equal to 0
            else:
                print("Input number is less than or equal to 0")
                raise ValueError("Input number is less than or equal to 0")

        #Invalid input
        else:
            print("Invalid input must be an integer")
            raise ValueError("Invalid input must be an integer")

    def setName(self, inputName):
        print("Input Name = ", inputName)
        self.name = inputName

    def setImageURL(self, inputImageURL):
        print("Input Image URL = ", inputImageURL)
        self.imageURL = inputImageURL

    def getDrinkID(self):
        return self.drinkID

    def getName(self):
        return self.name

    def getImageURL(self):
        return self.imageURL


def main():
    print("Entered Main")
    x = Cocktail()
    print("id = ", x.getDrinkID())
    x.setDrinkID(100)
    print("id = ", x.getDrinkID())
    x.setName("Manhattan")
    x.setImageURL("http:\/\/www.thecocktaildb.com\/images\/media\/drink\/rysb3r1513706985.jpg")
    print("Leaving Main")

main()
