## DECIDES WHICH TOOLS TO CALL

from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
import os
from ..LanggraphTools import Langgraph_state
from langchain.messages import HumanMessage

class PlannerAgent:

    def __init__(self,state:Langgraph_state.LanggraphState):

        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            api_key=os.getenv("FUTURE_GROQ_KEY"),
            temperature=0.1
        )

        self.state = state

    async def planner_agent(self):

        planner_prompt = f"""
            You are an intelligent Planner Agent for a Future Career Guidance AI.

            Your job is NOT to answer the student's question.

            Your only responsibility is to create an execution plan that tells the system
            which knowledge sources should be loaded before generating the final answer.

            Student Query:
            {self.state['query']}

            Selected Intermediate Group:
            {self.state['group']}

            got marks:
            {self.state['marks']}

            Available Knowledge Sources:

            1. group
            - Information about the selected intermediate group.
            - Example:
                MPC
                BiPC
                MEC
                CEC
                HEC
                Vocational

            2. careers
            - Career options after the selected group.

            3. skills
            - Required technical and soft skills.

            4. degrees
            - Degree courses after Intermediate.

            5. diploma
            - Diploma options.

            6. colleges
            - Colleges offering the recommended course.

            7. exams
            - Entrance exams.

            8. roadmap
            - Step-by-step career roadmap.

            9. salary
            - Salary information.

            10. higher_studies
            - Masters and higher education.

            11. abroad
            - Study abroad opportunities.

            12. scholarships
            - Scholarships and financial aid.

            13. generate_answer
            - Final answer generation node.
            - This MUST always be the last step.

            Rules:

            - Think carefully about what information is needed.
            - Include only the required nodes.
            - Do NOT include unnecessary nodes.
            - The first node must always be "group".
            - The last node must always be "generate_answer".
            - Return ONLY a JSON array.
            - Do NOT explain anything.
            - Do NOT use markdown.

            Examples

            Example 1

            Query:
            I want to become an AI Engineer.

            Output

            [
                "group",
                "careers",
                "skills",
                "degrees",
                "colleges",
                "roadmap",
                "salary",
                "generate_answer"
            ]

            Example 2

            Query:
            Can I study abroad after MPC?

            Output

            [
                "group",
                "degrees",
                "abroad",
                "scholarships",
                "generate_answer"
            ]

            Example 3

            Query:
            What entrance exams are required for MBBS?

            Output

            [
                "group",
                "careers",
                "degrees",
                "exams",
                "generate_answer"
            ]

            Generate the execution plan now.
            """

        response = await self.llm.ainvoke(
            [HumanMessage(content=planner_prompt)]
        )

        print("execution plan is : ",response.content)

        return  {
            'Execution_plan' : response.content
        }

