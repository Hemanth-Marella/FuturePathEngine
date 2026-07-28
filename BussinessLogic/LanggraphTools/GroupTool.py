from ..Services.Json_Loader_Service import JsonLoaderService
# from Services.Json_Loader_Service import JsonLoaderService
import asyncio
from langchain.tools import tool


@tool
async def group_tool(group:str):

    """
    Load the complete knowledge of an intermediate education group from the knowledge base.

    Call this tool whenever the execution plan contains "group" or when the user's
    query requires information about an intermediate group.

    Examples:
    - "Tell me about MPC."
    - "What subjects are there in BiPC?"
    - "Explain MEC group."
    - "Which group is suitable for engineering?"
    - "Give details of CEC."

    Input:
        group_name (str): Group name (e.g., MPC, BiPC, MEC, CEC, HEC, Vocational)

    Output:
        JSON containing the group's complete details including subjects,
        description, eligibility, career opportunities, and other stored information.
    """
    service =await JsonLoaderService().load_json(category="GroupsFiles",filename=group)

    print("service is ",service)

    return service


# async def main(inp):
#     content = await group_tool(inp)
#     print(content)

# inp = input("enter a group name : ",)
# if __name__ == "__main__":
#     asyncio.run(main(inp))