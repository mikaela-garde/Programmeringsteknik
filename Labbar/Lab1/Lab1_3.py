name =""
#Tar in ett namn och kollar om det är sauron och isånnafall säger den hej då och den går ur whileloopen
while name != "sauron":
    name =input("Vad heter du?")
    if name == "sauron":
        print("Hej då")
    else:
        print("Hej " + name)