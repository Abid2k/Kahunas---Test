from sqlalchemy import create_engine
import pandas as pd
from typing import Dict, List

class PostgresProcessor:
    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)
    
    def get_user_fitness_data(self, user_id: int) -> Dict:
        query = """
        SELECT 
            workouts.date,
            workouts.type,
            workouts.duration,
            metrics.heart_rate,
            metrics.calories_burned
        FROM workouts
        JOIN metrics ON workouts.id = metrics.workout_id
        WHERE workouts.user_id = %(user_id)s
        ORDER BY workouts.date DESC
        """
        
        df = pd.read_sql(query, self.engine, params={'user_id': user_id})
        return df.to_dict('records')
    
    def get_coaching_programs(self) -> List[Dict]:
        query = """
        SELECT 
            programs.name,
            programs.description,
            programs.difficulty_level,
            coaches.name as coach_name
        FROM programs
        JOIN coaches ON programs.coach_id = coaches.id
        """
        
        df = pd.read_sql(query, self.engine)
        return df.to_dict('records') 