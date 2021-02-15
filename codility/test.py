from typing import List, Text


class NoAgentFoundException(Exception):
    pass


class Agent(object):
    def __str__(self):
        return "<Agent: {}>".format(self.name)

    def __init__(self, name: Text, skills: List[str], load: int) -> None:
        self.name = name
        self.skills = skills
        self.load = load

class Ticket(object):

    def __init__(self, id: Text, restrictions: List[str]) -> None:
        self._id = id
        self.restrictions = restrictions


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        raise NotImplemented

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        return self._filter_loaded_agents(agents)

    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        least_loaded_agent = None

        for agent in agents:
            if agent.load == 0:
                return agent
            if agent.load == 3:
                continue
            if not least_loaded_agent:
                least_loaded_agent = agent
                continue
            if agent.load < least_loaded_agent.load:
                least_loaded_agent = agent

        if not least_loaded_agent:
            raise NoAgentFoundException()

        return least_loaded_agent


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        restrictions = set(ticket.restrictions)
        least_agent = None

        for agent in agents:
            agent_skills = set(agent.skills)
            if restrictions and not restrictions.intersection(agent_skills) == agent_skills:
                continue
            extra_agent_skills =  len(agent_skills) - len(restrictions)

            if extra_agent_skills == 0:
                return agent
            
            if not least_agent:
                least_agent = agent
                continue

            if len(agent_skills) < len(least_agent.skills):
                least_agent = agent

        if not least_agent:
            raise NoAgentFoundException()
        return least_agent






ticket = Ticket(id="1", restrictions=[])
agent1 = Agent(name="A", skills=['A'], load=2)
agent2 = Agent(name="B", skills=['C', 'D'], load=0)


lista = [agent1, agent2]

lista = sorted(lista, key=lambda agent: agent.load)

finder = LeastFlexibleAgent()

print(finder.find(ticket, [agent1, agent2]))


