
class Smartphone:
    def __init__(self, brand, model, storage_gb, battery_mah):
        self.__brand = brand
        self.__model = model
        self.__storage_gb = storage_gb
        self.__battery_mah = battery_mah
        self.__is_on = False

    def power_on(self):
        if not self.__is_on:
            self.__is_on = True
            return f"{self.__brand} {self.__model} is now ON."
        return f"{self.__brand} {self.__model} is already ON."

    def power_off(self):
        if self.__is_on:
            self.__is_on = False
            return f"{self.__brand} {self.__model} is now OFF."
        return f"{self.__brand} {self.__model} is already OFF."

    def get_specs(self):
        return f"{self.__brand} {self.__model} | Storage: {self.__storage_gb}GB | Battery: {self.__battery_mah}mAh"

# Subclass with inheritance and polymorphism
class MidRangeSmartphone(Smartphone):
    def __init__(self, brand, model, storage_gb, battery_mah):
        super().__init__(brand, model, storage_gb, battery_mah)

    def get_specs(self):
        base_specs = super().get_specs()
        return f"{base_specs}"

# Test the class
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "Galaxy S22", 256, 4500)
    phone2 = MidRangeSmartphone("Google", "Pixel 7 Pro", 256, 5000)

    print(phone1.get_specs())
    print(phone1.power_on())

    print(phone2.get_specs())
    print(phone2.power_on())

