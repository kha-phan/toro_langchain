# from langchain_community.agents import load_tools, initialize_agent, AgentType
# from langchain_community.llms import OpenAI
# from langchain_community.memory import ConversationBufferMemory


from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.llms import OpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory


from dotenv import load_dotenv


load_dotenv()

# memory = ConversationBufferMemory(memory_key="chat_history")

llm = OpenAI(temperature=0)
tools = load_tools(["llm-math"], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    # memory=memory,
    verbose=True
)

response = agent.run("Hi, I'm Rainee")
print(response)

response = agent.run("What's my name?")
print(response)
