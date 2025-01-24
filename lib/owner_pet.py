
class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all= []
    def __init__(self,name,pet_type,owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception (f"invalid pet type:{pet_type}Valid types are: {', '.join(Pet.PET_TYPES)}.")
        self.pet_type =pet_type
        self.owner = owner
        self.name = name
        if isinstance(self.owner, Owner) or self.owner is None:
            Pet.all.append(self)
        
class Owner:
    def __init__(self, name):
      self.name  = name         
    def pets(self):
        return[pet for pet in Pet.all if pet.owner == self]
    def add_pet(self, pet):
        if not isinstance(pet,Pet):
            raise Exception("The provided object is not of type Pet.") 
        pet.owner = self
    def get_sorted_pets(self):
        pets = self.pets()
        return sorted(self.pets(),key=lambda pet: pet.name )