import sys
import numpy as np
import pandas as pd
import joblib
from src.utils import load_object
from src.exception import CustomException
import os 

class PredictPipeline:
    def __init__(self):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

            self.model = load_object(model_path)
            self.preprocessor = load_object(preprocessor_path)
            print("Pipeline loaded successfully")
        except Exception as e:
            raise CustomException(f"Error loading pipeline: {e}", sys)

    def predict(self, features):
        try:
            data_scaled = self.preprocessor.transform(features)
            preds = self.model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e, sys)


           

class CustomData:
     def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):
                 

                 self.gender = gender
                 self.race_ethnicity = race_ethnicity
                 self.parental_level_of_education = parental_level_of_education

                 self.lunch = lunch

                 self.test_preparation_course = test_preparation_course

                 self.reading_score = reading_score

                 self.writing_score = writing_score

     def get_data_as_dataframe(self):
       try:
                 custom_data={
                                       "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],



                 }
                 
                 return pd.DataFrame(custom_data)       

       except Exception as e:
                 raise CustomException(e,sys)
           
         

         
