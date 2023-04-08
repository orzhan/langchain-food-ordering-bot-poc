from typing import List

from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.tools import BaseTool


class MenuTool(BaseTool):
    name = "menu"
    description = "input is a query string, output is list of menu items with names, descriptions and item ids"
    index: VectorStoreIndexWrapper = None

    def __init__(self, index: VectorStoreIndexWrapper):
        super(MenuTool, self).__init__()
        self.index = index

    def _run(self, query: str) -> str:
        ret = ''

        if query == 'None' or query == '':
            return 'Please provide a query'
            # query = ''
            # ret = 'Warning, listing all items on the menu since no query is provided. \n'

        # document_count = len(index.vectorstore.similarity_search(query, k=len(full_menu)))

        # ret += index.query(query, llm=llm, chain_type="map_reduce",
        #                  chain_type_kwargs={'question_prompt': QUESTION_PROMPT, 'combine_prompt': COMBINE_PROMPT})

        summaries = '\n'.join([doc.page_content for doc in self.index.vectorstore.similarity_search(query)])

        ret = f"""Given the following extracted parts of a long document and a question, create a final short answer. 
       If you don't know the answer, just say that you don't know. Don't try to make up an answer.

       =========
       {summaries}
       =========
       Answer:"""

        if ret == '':
            return "Nothing was found"

        # ret += f"\nNumber of relevant documents: {document_count}"

        return ret

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("MenuTool does not support async")


cart = {}


def describe_cart(full_menu):
    if len(cart.keys()) == 0:
        return "cart is empty"
    else:
        s = ""
        total = 0
        for k, v in cart.items():
            name = 'unknown'
            for item in full_menu:
                if int(item['id']) == int(k):
                    name = item['name']
                    total += item['price'] * int(v)
                    break
            s += f"{name}: {v}\n"
        s += f"Total: {total}\n"
        return s


class CartViewTool(BaseTool):
    name = "cartView"
    description = "input: 'view'"
    full_menu: List = None

    def __init(self, full_menu):
        super(CartViewTool, self).__init__()
        self.full_menu = full_menu

    def _run(self, query: str) -> str:
        return describe_cart(self.full_menu)

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("CartTool does not support async")


class CartAddTool(BaseTool):
    name = "cartAdd"
    description = "input: dish name from menu"
    full_menu: List = None

    def __init(self, full_menu):
        super(CartAddTool, self).__init__()
        self.full_menu = full_menu

    def _run(self, query: str) -> str:
        query = query.lower()
        n = -1
        for item in self.full_menu:
            if item['name'].lower() == query:
                n = item['id']
        if n == -1:
            return '''error: could not find in the menu'''
        if n not in cart:
            cart[n] = 1
        else:
            cart[n] += 1

        return describe_cart(self.full_menu)

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("CartTool does not support async")


class CartRemoveTool(BaseTool):
    name = "cartRemove"
    description = "input: dish name from menu"
    full_menu: List = None

    def __init(self, full_menu):
        super(CartRemoveTool, self).__init__()
        self.full_menu = full_menu

    def _run(self, query: str) -> str:
        query = query.lower()
        n = -1
        for item in self.full_menu:
            if item['name'].lower() == query:
                n = item['id']
        if n == -1:
            return '''error: could not find in the menu'''
        if n not in cart:
            return 'it is not in cart'
        else:
            cart[n] -= 1

        return describe_cart(self.full_menu)

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("CartTool does not support async")


class OrderTool(BaseTool):
    name = "order"
    description = "input: delivery address or None"
    full_menu: List = None

    def __init__(self, full_menu):
        super(OrderTool, self).__init__()
        self.full_menu = full_menu

    def _run(self, query: str) -> str:
        print("OrderTool", query)
        return "created order id=1, estimated delivery time 30 min"

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("OrderTool does not support async")

