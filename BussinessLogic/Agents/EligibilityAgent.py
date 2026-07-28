## CHECK ELIGIBILITY
from langchain_groq import ChatGroq
from langchain.messages import HumanMessage
import os
from dotenv import load_dotenv
load_dotenv()
import asyncio

# from ..LanggraphTools.Langgraph_state import LanggraphState For Modular Coding
from LanggraphTools.Langgraph_state import LanggraphState


async def eligibility_agent(group,query,marks,cgpa,carrer):

    # group = state['group']
    # query = state['query']
    # marks = state['marks']
    # cgpa = state['cgpa']
    # carrer = state['carrer']

    llm = ChatGroq(
                model="llama-3.1-8b-instant",
                api_key=os.getenv("FUTURE_GROQ_KEY"),
                temperature=0.1
            )


    prompt = f"""
                You are an Eligibility Verification Agent for a student career guidance system.

                Your task is to verify whether the student's requested career path or study option is academically eligible.

                Student Details:
                - Query: {query}
                - Selected Group: {group}
                - Marks: {marks}
                - CGPA: {cgpa}
                - Requested Career: {carrer}

                Instructions:

                1. Read the student's query carefully.
                2. Verify whether the selected group is appropriate for the requested career.
                3. Check whether the marks/CGPA satisfy the basic eligibility requirements if they are available.
                4. If eligibility cannot be determined because information is missing, return "INSUFFICIENT_INFORMATION".
                5. Do NOT generate career guidance, roadmap, colleges, exams, or salary information.
                6. Only verify eligibility.

                Return ONLY a valid JSON object.

                JSON Format:

                
                    "eligible": True,
                    "status": "ELIGIBLE",
                    "reason": "Student satisfies the basic eligibility requirements.",
                    "missing_information": [],
                    "next_action": "planner"
                

                Possible values:

                status:
                - ELIGIBLE
                - NOT_ELIGIBLE
                - INSUFFICIENT_INFORMATION

                Examples:

                Example 1:
                Input:
                Career = Doctor
                Group = BiPC

                Output:
                
                    "eligible": True,
                    "status": "ELIGIBLE",
                    "reason": "BiPC students are eligible to pursue MBBS and related medical careers.",
                    "missing_information": [],
                    "next_action": "planner"
                

                Example 2:
                Input:
                Career = Doctor
                Group = MPC

                Output:
                
                    "eligible": False,
                    "status": "NOT_ELIGIBLE",
                    "reason": "MBBS requires BiPC in Intermediate. MPC students are generally not eligible for MBBS.",
                    "missing_information": [],
                    "next_action": "stop"
                

                Example 3:
                Input:
                Career = AI Engineer
                Group = MPC

                Output:
                
                    "eligible": True,
                    "status": "ELIGIBLE",
                    "reason": "MPC is an appropriate stream for pursuing Computer Science and Artificial Intelligence degrees.",
                    "missing_information": [],
                    "next_action": "planner"
                

                Example 4:
                Input:
                Career = IAS Officer
                Group = ""

                Output:
                
                    "eligible": True,
                    "status": "INSUFFICIENT_INFORMATION",
                    "reason": "IAS eligibility depends on completing a bachelor's degree. The current education details are incomplete.",
                    "missing_information": [
                        "Current education level"
                    ],
                    "next_action": "planner"
                

                Rules:
                - Return ONLY JSON.
                - Do not add markdown.
                - Do not explain outside the JSON.
            """

    response = llm.invoke([HumanMessage(content=prompt)])

    print(response.content)

    return response.content


async def main(group,query,marks,cgpa,carrer):
    content = await eligibility_agent(group,query,marks,cgpa,carrer)
    print(content)

group = input("enter a group name : ",)
marks = int(input("enter a marks name : ",))
cgpa = int(input("enter a cgpa ",))
query = input("enter a query name : ",)
carrer = input("enter a carrer name : ",)
if __name__ == "__main__":
   
    asyncio.run(main(group,query,marks,cgpa,carrer))