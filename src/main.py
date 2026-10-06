class Player:
    def __init__(self, name):
        self.name = name
        self.bag = []

    def collect(self, item):
        if item not in self.bag:
            self.bag.append(item)
            print(f"{self.name} collected {item}.")
        else:
            print(f"{self.name} already has {item} in the bag.")

    def show_bag(self):
        if self.bag:
            print(f"{self.name}'s bag contains: {', '.join(self.bag)}")
        else:
            print(f"{self.name}'s bag is empty.")

class Place:
    def __init__(self, name, item=None):
        self.name = name
        self.item = item

    def visit(self, player):
        print(f"{player.name} is visiting {self.name}. ")
        if self.item is not None:
            print(f"{player.name} found {self.item} in {self.name}.")
            player.collect(self.item)


class LockedPlace(Place):
    def __init__(self, name, required_item, item):
        super().__init__(name, item)
        self.required_item = required_item

    def visit(self, player):
        if self.required_item in player.bag:
            print(f"{player.name} unlocked {self.name} and can now visit.")
            player.collect(self.item)
        else:
            print(f"{player.name} cannot visit {self.name} without a key.")


class Chest:
    def __init__(self, required_item, item, is_open=False):
        self.required_item = required_item
        self.item = item
        self.is_open = is_open

    def open(self, player):
        if self.required_item in player.bag:
            if not self.is_open:
                print(f"{player.name} opened the chest and found {self.item}.")
                self.is_open = True
                player.collect(self.item)
            else:
                print("The chest is already open.")
        else:
            print(f"{player.name} cannot open the chest without a {self.required_item}.")


player = Player("Suraj")

canteen = Place("Canteen", "Secret Key")
computer_lab = LockedPlace("Computer Lab", "Secret Key", "Secret Code")
main_stage = Place("Main Stage")
chest = Chest("Secret Code", "Trophy")

player.show_bag()
canteen.visit(player)
computer_lab.visit(player)
main_stage.visit(player)
player.show_bag()

chest.open(player)

player.show_bag()
