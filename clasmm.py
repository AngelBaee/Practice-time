class Mascara:
    def __init__(self,name,price,currency,available):
        self.name = name
        self.price = price
        self.currency = currency
        self.available = available


class Eyeshadow:
    def __init__(self,name,price,currency,shades):
        self.name = name
        self.price = price
        self.currency = currency
        self.shades = shades


class Lipstick:
    def __init__(self,name, price, currency,available):
        self.name = name 
        self.price = price
        self.currency = currency
        self.available = available


class Highlighter:
    def __init__(self,name,price,currency):
        self.name = name
        self.price = price
        self.currency = currency

class Foundation:
    def __init__(self,name,price,currency,available):
        self.name = name
        self.price = price
        self.currency = currency
        self.currency = available        


lipsticks = [
    Lipstick("Rare Beauty",28,"$","15, 17, 22, 28"),
    Lipstick("Viviene Sabo",23,"$","20, 16, 07"),
    Lipstick("NYX",18,"$","09, 08, 12"),
    Lipstick("Dior",32,"$", "08, 14, 07, 05"),
    Lipstick("Chanele",32,"$","22, 06, 08, 09, 12"),
    Lipstick("Maybelline",12,"$", "21, 20, 06, 08")
]


highlighters = [
   Highlighter("Huda Beauty",55,"$"),
   Highlighter("Dior",67,"$"),
   Highlighter("Rare Beauty",58,"$"),
   Highlighter("Viviene Sabo",60,"$")
]


foundations = [
   Foundation("Estelauder",70,"$","1, 2, 5"),
   Foundation("Dior",77,"$", "1, 2, 3, 4"), 
   Foundation("Missha",25,"$", "1, 2, 3"),
   Foundation("Collagen",15,"$", "1, 2 "),
   Foundation("Viviene Sabo",30,"$", "1, 4"),
   Foundation("Rare Beauty",33,"$", "1, 2, 3, 4 , 5")       
]


eyeshadows = [
   Eyeshadow("Huda beauty", 30 , "$" ,"dark shades"), 
   Eyeshadow("Rare Beauty",40,"$","all shades"),
   Eyeshadow("Dior", 50,"$","light shadows")
]


mascaras = [
   Mascara("NYX", 22, "$","1,3" ),
   Mascara("Rare Beauty", 35, "$","2,3" ),
   Mascara("Maybelline", 28, "$","1,2,3" ),
   Mascara("Dior", 50, "$","1" ),
   Mascara("Viviene Sabo", 40, "$","2"),
   Mascara("Chanele",52,"$","1,2")
]

all_instances = {
    "mascaras": mascaras,
    "lipsticks": lipsticks,
    "eyeshadows": eyeshadows,
    "highlighters": highlighters,
    "foundations": foundations
}

        
cosmetics = input("Eneter the type of product: ")

if cosmetics.lower() in all_instances:
    print(f'Available brands for {cosmetics}: ')

    for instance in all_instances[cosmetics.lower()]:
       print(instance.__dict__)
else:
   print("Out of stock")
    











 


