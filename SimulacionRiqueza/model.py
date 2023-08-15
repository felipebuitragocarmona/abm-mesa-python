from mesa import Model
from agent import MoneyAgent
from mesa.time import RandomActivation
from mesa.space import MultiGrid

class MoneyModel(Model):
    def __init__(self,N, width,height):
        self.num_agents=N
        self.grid=MultiGrid(width,height,True)
        self.schedule=RandomActivation(self)
        for i in range(self.num_agents):
            newAgent=MoneyAgent(i,self)
            self.schedule.add(newAgent)
            x=self.random.randrange(self.grid.width)
            y=self.random.randrange(self.grid.height)
            self.grid.place_agent(newAgent,(x,y))
    def step(self) -> None:
        self.schedule.step()