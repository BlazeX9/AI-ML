model = ChatOpenAI(model='gpt-4', temperature=1.5)  
<br>
**Temperature**: controls how much randomness LLM generates during a response. If we want the LLM to give more consistent and predictable outputs for the same input, we use a low temperature such as `0`. If we want the LLM to generate more varied, creative, and diverse outputs for the same input, we use a higher temperature.  

**Prompt**: based on input there is two type of prompt  
1. `Text-based prompt`: input contains only text  
2. `Multimodal prompt`: input contains multiple types of data such as Image + Audio + Text
