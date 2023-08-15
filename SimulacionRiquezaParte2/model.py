from mesa import Model
from agent import MoneyAgent
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import mesa
class MoneyModel(Model):
    def __init__(self,number_of_agents, width,height):
        self.num_agents=number_of_agents
        self.grid=MultiGrid(width,height,True)
        self.schedule=RandomActivation(self)
        self.running=True
        self.datacollector=mesa.DataCollector(
            model_reporters={
                "Wealthy Agents":self.current_wealthy_agents,
                "Non Wealthy Agents":self.current_non_wealthy_agents,
            }
        )

        for i in range(self.num_agents):
            newAgent=MoneyAgent(i,self)
            self.schedule.add(newAgent)
            x=self.random.randrange(self.grid.width)
            y=self.random.randrange(self.grid.height)
            self.grid.place_agent(newAgent,(x,y))
    def step(self) -> None:
        self.schedule.step()
        #Este permite actualizar los datos cada paso
        self.datacollector.collect(self)
        if MoneyModel.current_non_wealthy_agents(self)>20:
            self.running=False

    def current_wealthy_agents(model)->int:
        return sum([1 for agent in model.schedule.agents if agent.wealth>0])

    def current_non_wealthy_agents(model) -> int:
        return sum([1 for agent in model.schedule.agents if agent.wealth == 0])