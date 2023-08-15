from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from model import MoneyModel

def agent_portrayal(agent):
    portrayal={"Shape":"circle","Filled":"true","r":0.5}
    if agent.wealth>0:
        portrayal["Color"]="green"
        portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 1
        portrayal["r"]=0.2
    return portrayal

num_row_width=50
num_row_height=50

grid=CanvasGrid(agent_portrayal,num_row_width,num_row_height,500,500)
server=ModularServer(MoneyModel,[grid],"Money Model",{"N":5,"width":num_row_width,"height":num_row_height})
server.port=8521
server.launch()