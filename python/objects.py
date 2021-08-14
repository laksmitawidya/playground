""" 
Object is a bit of self contained code and data
- Break thr poblem into smaller understandable parts (divide & conquer)
- Have boundaries that allow us to ignore un needed detail
- I.e: String objects, integer objects, dictionary objects, list objects
 """

""" 
Definition
- Class - a template - Dog
- Method of message - defined capabitlity of class - bark()
- Field or attribute - A bit of data in a class - length
- Object or instance - A particular instance of a class - Lassie
 """

""" 
Terminology 
A pattern (exemplar) of class. Thr class of dog defines all possible dogs
by listing the characteristics and behaviors they can have; the object
Lassie is one particular dog, with particular versions of the characteristics
A Dog has fur, lassie has brown and white fur
"""

""" 
Instance
One can have an instance of class or a particular object.
The instance is actual object created at runtime. In programmer jargon,
the Lassie object is an instance of the Dog class. The set of values of the 
attributes of particular object is called its state.
The object consists of state and the behavior that's defined in the object's class
 """

""" 
 Method
 An object's abbilities. In language, method are verbs. Lassie, being
 a dog, has the ability to bark. So bark() is one of Lasie's method.
 She may have other methods as well, for example sit() or eat() or walk()
 """


class PartyAnimal:
    counter=0
    name=""

    # def __init__(self): # constructor
    #     print('Iam Constructed')

    def __init__(self, name): # constructor, can have additional params
        self.name = name
        print(self.name, 'is constructed')

    def party(self): # constructing party animal template
        self.counter = self.counter + 1
        print("Hi", self.name, "let's go party: ", self.counter)
    
    def __del__(self):
        print(self.name, " is destructed ", self.counter)

partyDog = PartyAnimal("Dog")

partyDog.party() # or PartyAnimal.party(party)
partyDog.party()
partyDog.party()
# print(type(party))
# print(dir(party))
partyDog = 10 # throwing away, no longer points at that object, created new object integer
print("Party contains", partyDog)

partyPeacok = PartyAnimal("Peacock")
partyPeacok.party()

partyKoala = PartyAnimal("Koala")
partyKoala.party()
partyPeacok.party()

# Dir and Type
# inspect variable with dir and type in object
# Dir: ignore the ones with underscores - these are used by Python itself
# The rest are real operations that the object can perform
# It is like type() - it tells us something *about* a variable

# list = list()
# print(type(list))
# print(dir(list))


""" Object Lifecycle
Objects are created, used and discarded
We have special blocks of code (methods) that get called
- At the moment of creation(constructor)
- At the moment of desctruction(destructor)
Constructors are used a lot
Desctructors are seldom used
 """

""" Constructor
 Set up some instance variables to have the proper initial values
 when the object is created
  """


""" Inheritance
The ability to extend a class to make a new class
- Instead of creating class from start, we can reuse an existing class
and inherit all the capabilities of an existing class and then
add our own lil bit to make our new class
- Another form of store and reuse
- Write once, reuse many times
- The new class(child) has all the capabilities of the old class(parent) and then some more
 
Terminology
Subclasses are more specialized versions of a class, which inherit attributes and behavior form their
parent classes and can introduce their own
 """


class PartyBirds(PartyAnimal):
    counterBirds = 0
    def homeParty(self):
        self.counterBirds = self.counterBirds + 7
        self.party()
        print(self.name, "counter", self.counter)
    
partyOwl = PartyBirds("Owl")
partyOwl.party()
partyOwl.homeParty()

# PartyBird is a class which extemds PartyAnimal. it has all the 
# capabilities of PartyAnimal