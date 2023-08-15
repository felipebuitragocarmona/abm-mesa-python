from mesa import Agent
from wallAgent import WallAgent
class MoneyAgent(Agent):
    def __init__(self,unique_id,model):
        super().__init__(unique_id,model)
        self.wealth=1
    def step(self) -> None:
        self.move()
        if self.wealth>0:
            self.give_money()
    def give_money(self):
        cellmates=self.model.grid.get_cell_list_contents([self.pos])
        print("vecinos "+str(cellmates))

        if len(cellmates)>1 and not self.verifyWall(cellmates):
            print("tipo " +str(type(cellmates[0])))
            if isinstance(cellmates[0], MoneyAgent):
                print("si es instancia")

            other=self.random.choice(cellmates)
            other.wealth+=1
            self.wealth-=1
    def verifyWall(self,cellmates):
        for actual in cellmates:
            if isinstance(actual, WallAgent):
                return True
        return False
    def move(self)->None:
        #moore=False -> solo ortogonal
        possible_steps=self.model.grid.get_neighborhood(
            self.pos,moore=False,include_center=False
        )
        print("acutal "+str(self.pos)+" posibles "+str(possible_steps))
        new_position=self.random.choice(possible_steps)
        cellmates = self.model.grid.get_cell_list_contents([new_position])

        if not self.verifyWall(cellmates):
            print("INTENTANDO")
            self.model.grid.move_agent(self,new_position)

        #self.model.grid.move_agent(self, new_position)