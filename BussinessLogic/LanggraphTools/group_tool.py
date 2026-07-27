# from ..Services.Json_Loader_Service import JsonLoaderService
from Services.Json_Loader_Service import JsonLoaderService
import asyncio


#  BussinessLogic/JsonFiles/GroupsFiles/mpc.json

# path = "BussinessLogic/JsonFiles/GroupsFiles/"

async def group_tool(group_name:str):

    # directory_path = f"{path}{group_name}.json"
    service =await JsonLoaderService().load_json(category="GroupsFiles",filename=group_name)

    return type(service)


async def main(inp):
    content = await group_tool(inp)
    print(content)

inp = input("enter a group name : ",)
if __name__ == "__main__":
    asyncio.run(main(inp))