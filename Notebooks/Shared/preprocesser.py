from typing import List
import pandas as pd
import numpy as np
from sklearn import preprocessing


class DataframeProcesser:
    def __init__(self, dataset: pd.DataFrame) -> None:
        self.df = dataset

    def remove_attributes(self, columns: List[str]) -> pd.DataFrame:
        self.df.drop(columns=columns, axis=1)
        return self.df

    def extract_numeric_values(self) -> pd.DataFrame:
        return self.df.select_dtypes(include=np.number)

    def normalize(self, type: str) -> pd.DataFrame:
        data = self.extract_numeric_values()

        if type == 'scalar':
            return self.__scalar_normalize(data)

        if type == 'mean':
            return self.__mean_normalize(data)

        if type == 'minmax':
            return self.__min_max_normalize(data)

        return self.df

    def rename(self, columnName: str, toName: str) -> pd.DataFrame:
        self.df.rename(columns={columnName: toName}, inplace=True)

    def time_to_deltatime(self, column: str):
        self.df[column] = pd.to_timedelta(
            self.df[column]).apply(lambda x: x.total_seconds()/60.0)

    def __mean_normalize(self, data: pd.DataFrame) -> pd.DataFrame:
        normalized_df = (data - data.mean()) / data.std()
        return normalized_df

    def __min_max_normalize(self, data: pd.DataFrame) -> pd.DataFrame:
        normalize_df = (data - data.min()) / \
            (data.max() - data.min())
        return normalize_df

    def __scalar_normalize(self, data: pd.DataFrame) -> pd.DataFrame:
        x = data.values  # returns a numpy array
        min_max_scaler = preprocessing.MinMaxScaler()
        x_scaled = min_max_scaler.fit_transform(x)
        df = pd.DataFrame(x_scaled)
        return df


class TitanicProcesser(DataframeProcesser):
    pass
