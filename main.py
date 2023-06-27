import os

os.environ["OPENAI_API_KEY"] = "enter your key here"


from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from langchain.agents.agent_types import AgentType

agent = create_csv_agent(OpenAI(temperature=0),
                         'station_data.csv',
                         verbose=True,
                         agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

questions = [
    'What is the average charging session duration in minutes? (float)',
    'What is the average energy usage per charging session in kWh? (float)',
    'What is the average amount paid by users for charging sessions in USD? (float)',
    'What is the most common start hour for charging sessions? (integer)',
    'What is the most common end hour for charging sessions? (integer)',
    'What is the average total charge time per session in hours? (float)',
    'Which day of the week has the highest percentage of charging sessions? (string)',
    'What is the percentage distribution of different platforms used by EV users? (float)'
]

#run this to view test questions
# for _, i in enumerate(questions):
#     ans=agent.run(i)
#     print(ans)

while True:
    ans=agent.run(input("Enter your question here:\n"))
    print(ans)