# Initialising a generic ClothesStore class with common values for all clothes 
class ClothesStore:
    def __init__(self, name, TypeOfClothes,price, brand, size, material, season):
        self.TypeOfClothes = TypeOfClothes
        self.name = name
        self.price = price
        self.brand = brand
        self.size = size
        self.material = material
        self.season = season

    def ShowInfoClothes(self):
        pass

# Divide clothes into classes depending on which parts of the body they are worn on
# Initialising a generic Outerwear class which contains "ClothesStore" values and unique value and the output of data on which clothes are listed  
class Outerwear(ClothesStore):
    def __init__(self, name, TypeOfClothes, price, brand, size, material, season, isWaterproof):

        super().__init__(name, TypeOfClothes, price, brand, size, material, season)
        self.isWaterproof = isWaterproof

    def ShowInfoClothes(self):
        print(f"Name of clothes: {self.name}\n" +
              f"Type: {self.TypeOfClothes}\n" +
              f"Price of it: {self.price} zł \n" +
              f"Brand: {self.brand}\n" +
              f"Size: {self.size}\n" +
              f"Material form which made: {self.material}\n" +
              f"Seasone: {self.season}\n" + 
              f"{self.isWaterproof}\n")

# Initialising a generic ClothesForBody class which contains "ClothesStore" values and unique value and the output of data on which clothes are listed          
class ClothesForBody(ClothesStore):
    def __init__(self, name, TypeOfClothes, price, brand, size, material, season, PartOfBody):

        super().__init__(name, TypeOfClothes, price, brand, size, material, season)
        self.PartOfBody = PartOfBody

    def ShowInfoClothes(self):
        print(f"Name of clothes: {self.name}\n" +
              f"Type: {self.TypeOfClothes}\n" +
              f"Price of it: {self.price} zł \n" +
              f"Brand: {self.brand}\n" +
              f"Size: {self.size}\n" +
              f"Material form which made: {self.material}\n" +
              f"Seasone: {self.season}\n" + 
              f"This thing is worn on {self.PartOfBody}\n")

# Initialising a generic ClothesForLegs class which contains "ClothesStore" values and unique value and the output of data on which clothes are listed  
class CLothesForLegs(ClothesStore):
    def __init__(self, name, TypeOfClothes, price, brand, size, material, season, isOpentoed):

        super().__init__(name, TypeOfClothes, price, brand, size, material, season)
        self.isOpentoed = isOpentoed

    def ShowInfoClothes(self):
        print(f"Name of clothes: {self.name}\n" +
              f"Type: {self.TypeOfClothes}\n" +
              f"Price of it: {self.price} zł \n" +
              f"Brand: {self.brand}\n" +
              f"Size: {self.size}\n" +
              f"Material form which made: {self.material}\n" +
              f"Seasone: {self.season}\n" + 
              f"{self.isOpentoed}\n")

# Initialising a generic Accessory class which contains "ClothesStore" values and unique value and the output of data on which clothes are listed  
class Accessory(ClothesStore):

    def __init__(self, name, TypeOfClothes, price, brand, size, material, season, isStyling):
           
        super().__init__(name, TypeOfClothes, price, brand, size, material, season)
        self.isStyling = isStyling

    def ShowInfoClothes(self):
        print(f"Name of clothes: {self.name}\n" +
              f"Type: {self.TypeOfClothes}\n" +
              f"Price of it: {self.price} zł \n" +
              f"Brand: {self.brand}\n" +
              f"Size: {self.size}\n" +
              f"Material form which made: {self.material}\n" +
              f"Seasone: {self.season}\n" + 
              f"{self.isStyling}\n")

# Output information about all clothes in Store
# Skarpetki, buty, chustka, chusta, czapka, rękawiczki, spodnie,sukienka, spódnica, płaszcz, koszula, podkoszulka, okulary, opaska na głowę || szal, bluza, sweter
Skarpetki = CLothesForLegs("Skarpetki/Socks", "Men's socks", 40.00, "PUMA", "39 - 42", "Cotton 75%, Polyester 25%", "For every seasone", "Socks are made in mesh type")
Skarpetki.ShowInfoClothes()

Buty = CLothesForLegs("Buty/Shoes", "Hiking shoes", 599.00, "Mil-Tec", 43, "Leather and a bit synthetic", "Winter", "Shoes are protected and waterproof")
Buty.ShowInfoClothes()

Chustka = Accessory("Chustka/Bandana", "Multifumctional bandana", 59.99, "HI-TEC", "Universal", "Polyester 100%", "Autumn", "Perfect for rappers and rockers")
Chustka.ShowInfoClothes()

Chusta = Accessory("Chusta/Shawl", "Female shawl", 199.99, "Gucci", "Universal", "Cotton 100%", "Summer", "Perfect for woman who are going to church")
Chusta.ShowInfoClothes()

Czapka = Outerwear("Czapka/Hat", "Children hat", 60.00, "The North Face", "Small", "Viscose 7%, Nylon 93%", "Winter", "Hat isn't waterproof, but very quckly dries up")
Czapka.ShowInfoClothes()

Rekawiczki = Outerwear("Rekawiczki", "Gloves for woman", 99.99, "TheStoneIsland", 21, "Polyester 100%", "Winter", "Isn't waterproof")
Rekawiczki.ShowInfoClothes()

Spodnie = ClothesForBody("Spodnie/Pants", "Men's pants", 80.99, "Gucci", "45", "Polyester 64% Nylon 36%", "summer", "legs")
Spodnie.ShowInfoClothes()

Sukienka = ClothesForBody("Sukienka/Dress", "Clidren's dress", 150.00, "Adidas", "Small", "Cotton 75%, Polyester 25%", "Summer", "chest(body)")
Sukienka.ShowInfoClothes

Spodnica = ClothesForBody("Spodnica/Skirt", "Woman's skirt", 100.00, "Gucci", "Large", "Viscose 7%, Nylon 93%", "Summer", "legs")
Spodnica.ShowInfoClothes()

Plaszcz = Outerwear("Plaszcz/Coat", "Inisex coat", 145.20, "TheStoneIsland", "Small", "Cotton 28%  Polyester 26% Viscose 46%", "Spring", "Coat is waterproof")
Plaszcz.ShowInfoClothes

Koszula = ClothesForBody("Koszula/Shirt", "Men's shirt", 150.00, "CROPP", 45, "Polyester 100%", "For all seasones",  "chest(body)")
Koszula.ShowInfoClothes()

Podkoszula = ClothesForBody("Podkoszula/T-shirt", "Boys t-shirt", 59.99, "Kappahl", "45 M", "Cotton 100 %", "For all seasones", "body(chest)")
Podkoszula.ShowInfoClothes()

Okulary = Accessory("Okullary/Glasses", "Sunglasses", 25.00, "Vogue", "Doesn't have size", "Plastic", "Spring/Summer", "Styling your face")
Okulary.ShowInfoClothes()

Opaska_Na_Glowie = Accessory("Opaska na glowie/Headband", "Headband for sport activities", 40.00, "Nike", "Universal", "Cotton 99%", "For any season", "Styling head and hairstyle")
Opaska_Na_Glowie.ShowInfoClothes()

Shal = Accessory("Shal/Scarf", "Woman's scarf", 75.49, "Mohito", "Universal", "Polyester after recycling 100%", "Spring/Summer/Autumn", "Styling head and neck")
Shal.ShowInfoClothes()

Bluza = ClothesForBody("Bluza/Sweatshirt", "Unisex sweatshirt", 150.00, "Puma", "38 - 42", "Cotton 80 %, Polyester 20%", "Winter", "chest")
Bluza.ShowInfoClothes()

Sweter = ClothesForBody("Sweter/Pullover", "Junior pullover", 100.00, "CROPP", "32-34 XS", "100% Acrylic", "For every seasone", "chest(body)")
Sweter.ShowInfoClothes()
