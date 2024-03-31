class Jewellery:
    
    def __init__(self, name, brand, price,karat):
        self.name = name
        self.brand = brand
        self.price = price
        self.karat = karat


class Clothes:
    def __init__(self,name,brand,price,material,size,color):
         self.name = name
         self.brand = brand
         self.price = price
         self.material = material
         self.size = size
         self.color = color
         
         
class Shoes:
    def __init__(self,name,brand,price,color):
        self.name = name
        self.brand = brand
        self.price = price
        self.color = color

jewellery = [
    Jewellery("Rubi necklaace","Tiffany" ,120000,99),
    Jewellery("Golden ring","Tiffany" ,3550,556),
    Jewellery("Silver watch","Tiffany",2000,925),
    Jewellery("Golden bracelet","Tiffany",12000,1000)
]


clothes = [
    Clothes("bloose","ZARA",55,"cottom","xs,s,m,l","white,beeje,light blue"),
    Clothes("jeans","GAP",30,"jeans","28,30,32,34","all blue shades"),
    Clothes("top","Top Shop",15,"cotton","xs-xxl","white,black,red"),
    Clothes("jacket","Dior",70,"barxat","s,m,l","indigo,black,dark red,dark green"),
    Clothes("skirt","Dior",40,"silk","28,30,32","golden,black,grey")
]


shoes = [
    Shoes("sneackers","Nike",1000,"brown and beeje, red and black"),
    Shoes("highhills","Zara",56,"black,white,beeje"),
    Shoes("converse","Dior",985,"black"),
    Shoes("highhills","Gucci",600,"dark blue,white,brown"),
    Shoes("sneakers","Puma",500,"black and dark red")
]        


all_instances = {
    "jewellery": jewellery,
    "clothes":  clothes,
    "shoes":  shoes
}


        
products = input("Eneter the type of product: ")

if products.lower() in all_instances:
    print(f'Available brands for {products}: ')

    for instance in all_instances[products.lower()]:
       print(instance.__dict__)
else:
   print("Out of stock")
    




