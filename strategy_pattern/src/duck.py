class Duck:
    def __init__(self):
        self.fly_behavior = None
        self.quack_behavior = None

    def display(self):
        raise NotImplementedError

    def perform_fly(self):
        if self.fly_behavior:
            self.fly_behavior.fly()

    def perform_quack(self):
        if self.quack_behavior:
            self.quack_behavior.quack()

    def swim(self):
        print("All ducks float, even decoys!")
    
    def set_fly_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior
    
    def set_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior