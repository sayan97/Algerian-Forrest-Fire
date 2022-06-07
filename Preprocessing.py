from sklearn.preprocessing import StandardScaler
import pandas as pd
class Preprocessor:
    def __init__(self,data):
        self.data=data

    def to_dataframe(self):
        df=pd.DataFrame([self.data])
