from Agent import Agent


class AgentNetwork:
    def __init__(self):
        self.agents = {}

    def add_agent(self, agent_name, measurement):
        if agent_name not in self.agents:
            self.agents[agent_name] = Agent(agent_name, measurement)

    def remove_agent(self, agent_name):
        if agent_name in self.agents:
            # Remove this agent from other agents' connections
            for agent in self.agents.values():
                agent.remove_connection(self.agents[agent_name])
            del self.agents[agent_name]

    def connect_agents(self, agent_name, other_name):
        if agent_name in self.agents and other_name in self.agents:
            self.agents[agent_name].add_connection(self.agents[other_name])

    def disconnect_agents(self, agent_name, other_name):
        if agent_name in self.agents and other_name in self.agents:
            self.agents[agent_name].remove_connection(self.agents[other_name])

    def update_agent_measurement(self, agent_name, measurement):
        if agent_name in self.agents:
            self.agents[agent_name].update_measurement(measurement)

    def clear_network(self):
        self.agents = {}

    def run_simulation(self, max_iterations=100, tolerance=1e-5, gamma=0.1):
        for iteration in range(max_iterations):
            updates = {}
            for agent in self.agents.values():
                if agent.connections:
                    avg_measurement = sum([other.measurement for other in agent.connections]) / len(agent.connections)
                    updates[agent.name] = avg_measurement

            # Update measurements if changes are above tolerance
            stable = True
            for agent_name, new_measurement in updates.items():
                if abs(self.agents[agent_name].measurement - new_measurement) > tolerance:
                    self.agents[agent_name].update_measurement(new_measurement)
                    stable = False

            if stable:
                print(f"Convergence reached after {iteration + 1} iterations.")
                return

        print("Maximum iterations reached without convergence.")

    def __str__(self):
        return ', '.join(f"{agent.name}: {agent.measurement}" for agent in self.agents.values())
