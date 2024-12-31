menu = ["Dogs", "Cats", "Other." "D, C, O"]
Dogs = ["Corgi", "Huskey", "WolfDog", "GermanShepard"]
Cats = ["Tabby", "Manecoon", "Siamese", "BobCat"]
Other = ["Fish", "Lizard", "Snake"]

menu_select = input(f"Select an {menu} animal")

if menu_select == "D":
    print("You Wish to adopt a dog")
    Dog_Selection = input(f"Select a {Dogs}model Dog you want!")
    print(f"you have chosen {Dog_Selection}!")

elif menu_select == "C":
    print("You Wish to adopt a cat")
    Cat_Selection = input(f"Select a {Cats} model Cat you want!")
    print(f"You have chosen {Cat_Selection}!")

else:
    Other_selection = input(f"Select a type of {Other} Animal You want")
    print(f"you have chosen {Other_selection}!")