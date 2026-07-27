# from ..Services.Json_Loader_Service import JsonLoaderService  ## FOR MODULAR CODE
from Services.Json_Loader_Service import JsonLoaderService  ## FOR INDIVIDUAL IMPLEMET
import asyncio

async def carrer_tool(carrer_name:str,):

    # directory_path = f"{path}{group_name}.json"
    service =await JsonLoaderService().load_json(category="CarrerFiles/BipsFiles",filename=carrer_name)

    return service


async def main(inp):
    content = await carrer_tool(inp)
    print(content)

inp = input("enter a carrer name : ",)
if __name__ == "__main__":
    asyncio.run(main(inp))