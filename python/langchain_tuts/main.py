from langchain.agents import create_agent


def get_weather(city: str) -> str:
    """Get weather for a given city"""
    return f"It's always sunny in {city}!"

agent = create_agent(
        model="openai:gpt-5.4-nano",
        tools=[get_weather],
        system_prompt="You are a helpful assisstant.",
       )

result = agent.invoke(
        {"messages": [{"role": "user", "content":"Whats the weather in München?"}]})

print(result["messages"][-1].content_blocks)

