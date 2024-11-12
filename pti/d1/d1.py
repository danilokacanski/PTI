from Agent import Agent
from Network import AgentNetwork

# Initilazing agents

A = Agent('A', 25)
B = Agent('B', 26)
C = Agent('C', 26)
D = Agent('D', 26)
E = Agent('E', 28)
F = Agent('F', 26)

# Creating network

network = AgentNetwork()
network.clear_network()
network.add_agent(A.name, A.measurement)
network.add_agent(B.name, B.measurement)
network.add_agent(C.name, C.measurement)
network.add_agent(D.name, D.measurement)
network.add_agent(E.name, E.measurement)
network.add_agent(F.name, F.measurement)
network.connect_agents('A','B')
network.connect_agents('B','C')
network.connect_agents('C','A')
network.connect_agents('C','B')
network.connect_agents('D','B')
network.connect_agents('D','E')
network.connect_agents('D','F')
network.connect_agents('E','C')
network.connect_agents('E','F')
network.connect_agents('F','E')

# Running simulation of agents consulting each other about temperature

network.run_simulation()

# Printing network results

print(network)
