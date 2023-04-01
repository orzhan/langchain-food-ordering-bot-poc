# langchain-food-ordering-bot-poc
An implementation of a food ordering bot with langchain and chatgpt

# configuration

export OPENAI_API_KEY, and edit data.py. Run with `python start.py`. 

# capabilities

Question answering on a custom data (I'm using a list of dicts here but it can handle larger files and databases), and custom tool execution (this bot allows to track some internal state for example cart, calculate something for example total, and call external APIs, for example submit an order)

# example dialog

**AI: I am TestSushi food ordering assistant. We have various rolls and sashimi. I am ready to answer your questions and accept an order**

**Human: what rolls do you have?**

*Entering new AgentExecutor chain...
Thought: Do I need to use a tool? Yes
Action: Menu
Action Input: None
Observation: Please provide a query
Thought:Do I need to use a tool? Yes
Action: Menu
Action Input: rolls*
Observation: Given the following extracted parts of a long document and a question, create a final answer.
       *If you don't know the answer, just say that you don't know. Don't try to make up an answer.
       =========
       Dragon Roll (4) - 14.5 - Eel, cucumber, avocado, and crab meat rolled in nori and sushi rice, topped with avocado and eel sauce.
California Roll (2) - 8.5 - Crab meat, avocado, cucumber, and masago rolled in nori and sushi rice.
Philadelphia Roll (13) - 8.5 - Smoked salmon, cream cheese, cucumber, and avocado rolled in nori and sushi rice.
Sake Roll (16) - 9.5 - Grilled salmon, cucumber, and avocado rolled in nori and sushi rice.*
       =========
       *Answer:
Thought:Do I need to use a tool? No
AI: We have Dragon Roll, California Roll, Philadelphia Roll, and Sake Roll.
Finished chain*

**AI: We have Dragon Roll, California Roll, Philadelphia Roll, and Sake Roll.**

**Human: add sake roll plese**

*Entering new AgentExecutor chain...
Thought: Do I need to use a tool? Yes
Action: CartAdd
Action Input: Sake Roll
Observation: Sake Roll: 1
Total: 9.5
Thought:Do I need to use a tool? No
AI: Sake Roll has been added to your order. Is there anything else you would like to add?*

*Finished chain*

**AI: Sake Roll has been added to your order. Is there anything else you would like to add?**

**Human: no**

*Entering new AgentExecutor chain...
Thought: Do I need to use a tool? No
AI: Alright, let me know if you have any other questions or if you're ready to submit your order.
Finished chain.*

**AI: Alright, let me know if you have any other questions or if you're ready to submit your order.**
**Human: submt order, deliver to Main street 28**

*Entering new AgentExecutor chain...
Thought: Do I need to use a tool? Yes
Action: Order
Action Input: deliver to Main street 28OrderTool deliver to Main street 28
Observation: created order id=1, estimated delivery time 30 min
Thought:Do I need to use a tool? No
AI: Your order has been submitted with ID 1 and estimated delivery time of 30 minutes. Thank you for choosing TestSushi!
Finished chain.*

**AI: Your order has been submitted with ID 1 and estimated delivery time of 30 minutes. Thank you for choosing TestSushi!**
