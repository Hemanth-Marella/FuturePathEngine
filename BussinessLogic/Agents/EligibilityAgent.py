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
                temperature=0.5
            )


    prompt = f"""
                You are an Eligibility Verification Agent for a student career guidance system.

                Your ONLY responsibility is to determine whether the student is academically eligible for the requested career or study path.

                Student Details:
                - Query: {query}
                - Selected Group: {group}
                - Marks: {marks}
                - CGPA: {cgpa}
                - Requested Career: {carrer}

                Instructions:

                1. Read the student's requested career carefully.
                2. Verify whether the student's selected Intermediate group satisfies the academic subject requirements for that career.
                3. If marks or CGPA are required for the requested career and are available, verify them as well.
                4. If required information is missing, return "INSUFFICIENT_INFORMATION".
                5. If the selected group does not satisfy the academic requirements, return "NOT_ELIGIBLE".
                6. Never assume eligibility.
                7. Never guess.
                8. Use standard Indian education eligibility rules.
                9. If uncertain, return "INSUFFICIENT_INFORMATION" instead of making assumptions.
                10. Do NOT provide career guidance, roadmap, colleges, exams, salary, or alternative careers.
                11. Return ONLY the eligibility decision.

                1. Read and understand the student's query and requested career.
                Determine the commonly accepted Intermediate group required for the requested career.
                Do not invent new subject requirements.
                Do not assume Computer Science is mandatory unless the career explicitly requires it.
                If multiple educational pathways exist, consider the commonly accepted Indian pathway.
                If you are not confident, return INSUFFICIENT_INFORMATION instead of making assumptions.
                3. Compare the student's selected Intermediate group with those requirements.
                4. If the selected group satisfies the academic requirements, return:
                - eligible = true
                - status = "ELIGIBLE"
                - next_action = "planner"
                5. If the selected group does not satisfy the academic requirements, return:
                - eligible = false
                - status = "NOT_ELIGIBLE"
                - next_action = "PLEASE_CHECK_SELECTED_GROUP_AND_CAREER_BOTH_ARE_MISMATCHING"
                6. If the required information is missing or the career cannot be determined confidently, return:
                - eligible = false
                - status = "INSUFFICIENT_INFORMATION"
                - next_action = "USER_INFORMATION"

                Return ONLY valid JSON.

                JSON Schema:

                
                "eligible": true,
                "status": "ELIGIBLE",
                "reason": "Clear academic eligibility explanation.",
                "missing_information": [],
                "next_action": "planner"

                Possible status values:
                - ELIGIBLE
                - NOT_ELIGIBLE
                - INSUFFICIENT_INFORMATION

                IF ELIGIBLE ONLY TIME PASS NEXT_ACTION IS PLANNER 
                AND IF NOT ELIGIBLE TIME PROVIDE A NEXT_ACTION IS PLEASE CHECK SELECTED GROUP AND CARRER BOTH ARE MIS MATCHING
                AND IF INSUFFICIENT_INFORMATION TIME PROVIDE A NEXT_ACTION IS USER_INFORMATION

                Rules:

                - Return ONLY JSON.
                - Do NOT return markdown.
                - Do NOT invent eligibility rules.
                - Do NOT assume all careers are available for every group.
                - Verify the required Intermediate group before returning ELIGIBLE.
                - If the career has mandatory subject requirements that are not met, return NOT_ELIGIBLE.
                - Provide explanation when it is mismatching and give a correct explanation about selected group and carrer
                - Please mention the required fields from the student details when it is not sufficient information
                - please give motivation also when the next action is planner . Like you selected perfect group try to achieve them by hardwork like this
            """

    response = llm.invoke([HumanMessage(content=prompt)])

    # print(response.content)

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