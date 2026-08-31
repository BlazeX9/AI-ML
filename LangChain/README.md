model = ChatOpenAI(model='gpt-4', temperature=1.5)  

**Temperature**: controls how much randomness LLM generates during a response. If we want the LLM to give more consistent and predictable outputs for the same input, we use a low temperature such as `0`. If we want the LLM to generate more varied, creative, and diverse outputs for the same input, we use a higher temperature.
