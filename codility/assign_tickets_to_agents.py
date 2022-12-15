"""
Assign tickets to Agents

We got 2 strategies: assign to least loaded Agent, or assign to Least Flexible one.

Least Flexible:
    - if skills required is "English" and you got agent A with "English", and agent B with "English", "French", you want to use A as B is more flexible.

"""


from typing import List


SKILLS = ["French", "English", "Italian"]

class NoAgentFoundException(Exception):
    pass


class Agent:
   
    def __init__(self, name: str, skills: List[str], load: int):
        self._name = name
        self.skills = skills
        self.load = load

    def __repr__(self):
        return f"{self.name} - {self.skills} - {self.load}"


    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> str:
        self._name = name
        return self._name

class Ticket:

    def __init__(self, id: str, restrictions: List[str]):
        self.ticket_id = id
        self.restrictions = restrictions

    def __repr__(self):
        return f"{self.ticket_id} - {self.restrictions}"



class LeastLoadedAgent:
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        agents_with_capacity = filter(lambda a: a.load <=2, agents)  # returns a filter object, which is a generator (similar to map)
        sorted_agents = sorted(agents_with_capacity, key=lambda a: a.load)

        try:
            return sorted_agents[0]
        except IndexError:
            raise NoAgentFoundException() 


class LeastFlexibleAgent:
    # the one with the fewest skills

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        sorted_agents = sorted(agents, key=lambda a: len(a.skills))  # returns a list (alternative agents.sort(key=lambda ....))

        for agent in sorted_agents:
            if agent.load <= 2 and set(ticket.restrictions).issubset(set(agent.skills)):
                return agent

        raise NoAgentFoundException()



ticket = Ticket(id=1, restrictions=["English"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)
agent3 = Agent(name="C", skills=["English", "Italian", "japanese"], load=3)


agents = [agent1, agent2, agent3]

least_loaded_policy = LeastLoadedAgent()
agent_result = least_loaded_policy.find(ticket, agents.copy())
print(f"Least loaded agent: {agent_result.name}")

least_flexible_policy = LeastFlexibleAgent()
agent_result = least_flexible_policy.find(ticket, agents.copy())
print(f"Least flexible agent: {agent_result.name}")


