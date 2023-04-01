from __future__ import annotations

import os.path

from langchain.agents import Tool, AgentExecutor
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.memory import ConversationBufferWindowMemory
from langchain.vectorstores import Chroma

from agent import MyConversationalAgent
from data import full_menu, StringLoader, full_menu_text
from prompt import GREETING
from tools import MenuTool, CartViewTool, CartAddTool, CartRemoveTool, OrderTool

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, request_timeout=60)
persist_directory = 'db'
embeddings = HuggingFaceEmbeddings()

if not os.path.exists(persist_directory):
    index = VectorstoreIndexCreator(vectorstore_kwargs={'persist_directory': persist_directory})
    index.embedding = embeddings
    index = index.from_loaders([StringLoader(full_menu_text)])
    index.vectorstore.persist()
else:
    index = VectorStoreIndexWrapper(
        vectorstore=Chroma(persist_directory=persist_directory, embedding_function=embeddings))

menu = MenuTool(index)
cartView = CartViewTool(full_menu=full_menu)
cartAdd = CartAddTool(full_menu=full_menu)
cartRemove = CartRemoveTool(full_menu=full_menu)
order = OrderTool(full_menu=full_menu)

tools = [
    Tool(
        name="Menu",
        func=menu.run,
        description="useful for when you need to answer questions about the menu, the dishes, food"
    ),
    Tool(
        name="CartView",
        func=cartView.run,
        description="useful to see what items were added to order, and see total amount"
    ),
    Tool(
        name="CartAdd",
        func=cartAdd.run,
        description="useful when you need to add item to order. Please supply dish name from menu"
    ),
    Tool(
        name="CartRemove",
        func=cartRemove.run,
        description="useful when you need to remove item to order. Please supply id of dish instead of name"
    ),
    Tool(
        name="Order",
        func=order.run,
        description="useful when you are ready to submit the order"
    )]

memory = ConversationBufferWindowMemory(memory_key="chat_history", return_messages=True)
memory.chat_memory.add_ai_message(GREETING)

agent_obj = MyConversationalAgent.from_llm_and_tools(llm=llm, tools=tools, verbose=True)

agent_chain = AgentExecutor.from_agent_and_tools(
    llm=llm,
    agent=agent_obj,
    tools=tools,
    verbose=True,
    memory=memory,
    max_iterations=6
)

count_exception = 0
output = ''
while True:
    input_str = input()
    try:
        output = agent_chain.run(input=input_str)

    except Exception as ex:
        print(ex)
        count_exception += 1
        if count_exception >= 2:
            break

    print(output)
