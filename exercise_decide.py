import os
from dotenv import load_dotenv
load_dotenv()
import asyncio
from langchain_groq import ChatGroq
from langchain.messages import HumanMessage

async def exercise_decide():

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=os.getenv("FUTURE_GROQ_KEY"),
        temperature=0.1
    )

    exercise_type = "beginner"
    food_preferences = "non veg"
    country_type = "indian"

    prompt = f"""
        You are an experienced fitness coach and nutritionist.

        Generate a personalized workout plan and diet plan based on the user's details.

        ## User Details
        - Age: 25 years
        - Gender: Male
        - Height: 183 cm
        - Weight: 60 kg
        - Goal: Weight Loss
        - Fitness Level: Beginner
        - Workout Duration: 30 minutes
        - Workout Days Per Week: 7
        - Routine: Morning
        - Diet Preference: {food_preferences}
        - Injuries: No injuries, but has mild lower back pain.

        ## Exercise Database
        You MUST select exercises ONLY from the following list. Do not generate or recommend any exercise outside this list.

        - Cross Crunches
        - Donkey Kicks
        - Forward Lunges
        - Jumping Jacks
        - Knee Push-ups
        - Lateral Raises
        - Side Lunges
        - Squats
        - Superman
        - Forward Crunches
        - Reverse Crunches

        ## Workout Instructions

        1. Create a {exercise_type}-friendly workout.
        2. Workout duration should be close to 30 minutes.
        3. Avoid excessive stress on the lower back.
        4. Include warm-up and cool-down sections.
        5. Select only suitable exercises from the provided database.
        6. For each exercise provide:
        - Exercise Name
        - Sets
        - Repetitions (or seconds if applicable)
        - Rest Time
        7. Arrange the exercises in a logical order.

        ## Diet Plan Instructions

        Create a {food_preferences} diet plan based on {country_type} divided into:

        - Morning
        - Breakfast
        - Mid-Morning Snack
        - Lunch (Afternoon)
        - Evening Snack
        - Dinner (Night)

        For every food item mention:

        - Food Name
        - Quantity in grams (g) or milliliters (ml)

        Example:

        Breakfast
        - Oats - 50 g
        - Milk - 250 ml
        - Banana - 120 g

        ## Important Rules

        - Do NOT mention calories.
        - Do NOT mention protein, carbohydrates, fats, fiber, vitamins, or any nutrients.
        - Do NOT explain why a food is chosen.
        - Do NOT recommend supplements.
        - Keep the output simple and clean.
        - Use markdown headings and bullet points.
        - Return only the workout plan followed by the diet plan.
        """

    response = await llm.ainvoke(
        [HumanMessage(content=prompt)]
    )
    
    # print("execution plan is : ",response.content)

    return  response.content

async def main():
    content = await exercise_decide()
    print(content)


if __name__ == "__main__":
    asyncio.run(main())