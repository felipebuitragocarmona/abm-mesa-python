from mesa import Agent
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

        if len(cellmates)>1:
            print("tipo " +str(type(cellmates[0])))

            other=self.random.choice(cellmates)
            other.wealth+=1
            self.wealth-=1
    def move(self)->None:
        possible_steps=self.model.grid.get_neighborhood(
            self.pos,moore=True,include_center=False
        )
        #print("acutal "+str(self.pos)+" posibles "+str(possible_steps))
        new_position=self.random.choice(possible_steps)
        self.model.grid.move_agent(self,new_position)