from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from typing import Dict, Any

class LLMHandler:
    def __init__(self, api_key: str):
        self.llm = OpenAI(
            api_key=api_key,
            model="gpt-3.5-turbo-instruct"
        )
        self.setup_prompts()
    
    def setup_prompts(self):
        self.fitness_analysis_template = PromptTemplate(
            input_variables=["fitness_data"],
            template="""
            Analyze the following fitness data and provide actionable insights:
            {fitness_data}
            
            Please provide:
            1. Progress analysis
            2. Areas of improvement
            3. Recommendations
            """
        )
        
        self.coaching_template = PromptTemplate(
            input_variables=["user_query", "program_data"],
            template="""
            Based on the user query: {user_query}
            And the available program data: {program_data}
            
            Provide a personalized recommendation for the most suitable program.
            Include:
            1. Program name
            2. Why it's suitable
            3. Key benefits
            """
        )
    
    def analyze_fitness_data(self, fitness_data: Dict[str, Any]) -> str:
        chain = LLMChain(llm=self.llm, prompt=self.fitness_analysis_template)
        return chain.run(fitness_data=str(fitness_data))
    
    def get_program_recommendation(self, query: str, program_data: Dict[str, Any]) -> str:
        chain = LLMChain(llm=self.llm, prompt=self.coaching_template)
        return chain.run(user_query=query, program_data=str(program_data)) 