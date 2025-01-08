from data_processors.postgres_processor import PostgresProcessor
from data_processors.pdf_processor import PDFProcessor
from llm.llm_handler import LLMHandler
import yaml
from typing import Dict, Any

class FitnessChatbot:
    def __init__(self, config_path: str):
        self.load_config(config_path)
        self.setup_components()
    
    def load_config(self, config_path: str):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
    
    def setup_components(self):
        self.db_processor = PostgresProcessor(self.config['postgres']['connection_string'])
        self.pdf_processor = PDFProcessor(self.config['pdf']['directory'])
        self.llm_handler = LLMHandler(self.config['openai']['api_key'])
    
    def process_query(self, query: str, user_id: int) -> Dict[str, Any]:
        # Get user's fitness data
        fitness_data = self.db_processor.get_user_fitness_data(user_id)
        
        # Get available coaching programs
        programs = self.db_processor.get_coaching_programs()
        
        # Analyze fitness data using LLM
        fitness_analysis = self.llm_handler.analyze_fitness_data(fitness_data)
        
        # Get program recommendation
        program_recommendation = self.llm_handler.get_program_recommendation(
            query, programs
        )
        
        # If a specific program is recommended, get its instructions
        program_instructions = None
        if program_recommendation:
            program_name = program_recommendation.split('\n')[0]  # Extract program name
            program_instructions = self.pdf_processor.extract_workout_instructions(program_name)
        
        return {
            'fitness_analysis': fitness_analysis,
            'program_recommendation': program_recommendation,
            'program_instructions': program_instructions
        }

def main():
    chatbot = FitnessChatbot('config/config.yaml')
    
    # Example usage
    query = "I'm looking for a beginner-friendly strength training program"
    user_id = 123
    
    response = chatbot.process_query(query, user_id)
    print(response)

if __name__ == "__main__":
    main() 