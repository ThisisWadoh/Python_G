# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.__brand = brand  # Private attribute (encapsulation)
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    # Getter for private attribute
    def get_brand(self):
        return self.__brand

    # Method to display smartphone details
    def display_info(self):
        print(f"Brand: {self.__brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage} GB")
        print(f"Battery Life: {self.battery_life} hours")

    # Method to simulate turning on the phone
    def turn_on(self):
        print(f"{self.__brand} {self.model} is now turning on...")

# Derived class: GamingSmartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, gpu):
        super().__init__(brand, model, storage, battery_life)
        self.gpu = gpu

    # Overriding the turn_on method (polymorphism)
    def turn_on(self):
        print(f"{self.get_brand()} {self.model} with {self.gpu} GPU is booting into gaming mode...")

# Derived class: CameraSmartphone
class CameraSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, camera_megapixels):
        super().__init__(brand, model, storage, battery_life)
        self.camera_megapixels = camera_megapixels

    # Overriding the turn_on method (polymorphism)
    def turn_on(self):
        print(f"{self.get_brand()} {self.model} is ready to capture stunning {self.camera_megapixels} MP photos!")

# Creating instances of the classes
phone1 = Smartphone("Samsung", "Model AO4e", 128, 24)
phone2 = GamingSmartphone("GameMaster", "Ultra G1", 256, 18, "Adreno 650")
phone3 = CameraSmartphone("PhotoPro", "CamX 500", 512, 20, 108)

# Demonstrating polymorphism and encapsulation
print("\n--- Smartphone Details ---")
phone1.display_info()
phone1.turn_on()

print("\n--- Gaming Smartphone Details ---")
phone2.display_info()
phone2.turn_on()

print("\n--- Camera Smartphone Details ---")
phone3.display_info()
phone3.turn_on()
