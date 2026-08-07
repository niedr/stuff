from langchain.chat_models import init_chat_model
from deepagents import create_deep_agent
from langchain.tools import tool
from langchain.tools import ToolException

import requests
import argparse

SYSTEM_PROMPT = """ You are a general agent for multiple tasks. Currently you are able to do:
    - `get_stoicism_quote`: requests an api for stoic content
    
    If the request fails don't answer with quotes from yourself. Answer 'tool: {tool_name} failed miserably'

    """

@tool
def get_stoicism_quote() -> dict:
    """ Function to request stoic quote from api"""
    try:
        url = 'https://stoic.tekloon.net/stoic-quote'
        resp = requests.get(url, timeout=20)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        raise ToolException(f"API request failed {e}")


def main():

    parser = argparse.ArgumentParser(description="Run the local agent with a custom prompt")
    parser.add_argument("--prompt", help="write your prompt here", default="Please think of a short joke")
    args = parser.parse_args()

    local_model = init_chat_model("Qwythos-9B-Claude-Mythos-5-1M-MTP-Q6_K.gguf", 
                            model_provider="openai", 
                            base_url="http://localhost:8080/v1",
# hier fehlt noch klammer zu und a p i k e y none
    deep_agent = create_deep_agent(
            model=local_model,
            tools=[get_stoicism_quote],
            system_prompt=SYSTEM_PROMPT
            )

    content = args.prompt


    deep_agent_result = deep_agent.invoke(
    {"messages": [{"role": "user", "content": content}]},
    config={"configurable": {"thread_id": "stoic-answers"}},
    )   

    print(deep_agent_result["messages"][-1].content)
    

if __name__ == "__main__":
    main()
