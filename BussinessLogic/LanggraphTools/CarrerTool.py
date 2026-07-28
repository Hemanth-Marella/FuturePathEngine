from ..Services.Json_Loader_Service import JsonLoaderService  ## FOR MODULAR CODE
# from Services.Json_Loader_Service import JsonLoaderService  ## FOR INDIVIDUAL IMPLEMET
import asyncio
from langchain.tools import tool

@tool
async def carrer_tool(carrer_name:str,):

    """
    Retrieves detailed information about a specific career from the knowledge base.

    Use this tool whenever the user asks about:
    - A particular career or profession.
    - Career eligibility.
    - Required qualifications or education.
    - Skills needed for a career.
    - Job roles and responsibilities.
    - Career roadmap.
    - Higher education after choosing a career.
    - Salary information.
    - Future scope and career opportunities.

    Examples:
    - "Tell me about Software Engineer."
    - "Explain MBBS career."
    - "What is the salary of a Data Scientist?"
    - "How can I become a Pilot?"
    - "Give details about Chartered Accountant."

    Input:
        carrer_name (str): Name of the career.
        Examples: "Software Engineer", "Doctor", "Data Scientist",
        "Pilot", "Chartered Accountant", "Civil Engineer"

    Returns:
        A JSON object containing complete information about the requested
        career, including eligibility, education path, required skills,
        career roadmap, salary, job roles, and future opportunities.
        If the career is not found, return an appropriate error message.
    """
    service =await JsonLoaderService().load_json(category="CarrerFiles/BipsFiles",filename=carrer_name)

    return service


async def main(inp):
    content = await carrer_tool(inp)
    print(content)

inp = input("enter a carrer name : ",)
if __name__ == "__main__":
    asyncio.run(main(inp))