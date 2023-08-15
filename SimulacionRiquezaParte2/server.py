
from mesa.visualization.ModularVisualization import ModularServer
from model import MoneyModel
import mesa
from mesa.visualization.modules import CanvasGrid,ChartModule

NUMBER_OF_CELLS=3
SIZE_OF_CANVAS_IN_PIXELS_X=500
SIZE_OF_CANVAS_IN_PIXELS_Y=500

simulation_params={

    "number_of_agents":mesa.visualization.Slider(name='Number of Agents', value=2, min_value=1, max_value=200, step=1, description="seleccionar numero de agentes"),
    "width":NUMBER_OF_CELLS,
    "height":NUMBER_OF_CELLS
}

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


grid=CanvasGrid(agent_portrayal,NUMBER_OF_CELLS,NUMBER_OF_CELLS,SIZE_OF_CANVAS_IN_PIXELS_X,SIZE_OF_CANVAS_IN_PIXELS_Y)

chart_currents=mesa.visualization.ChartModule(
    [
        {"Label": "Wealthy Agents", "Color": "","label":"Poder","backgroundColor": "Blue"},
        {"Label": "Non Wealthy Agents", "Color": "","label":"No Poder","backgroundColor": "Red"},
    ],
data_collector_name="datacollector"
)

server=mesa.visualization.ModularServer(MoneyModel,[grid,chart_currents],"Money Model",model_params=simulation_params)
server.port=8521
server.launch()