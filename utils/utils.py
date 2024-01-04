import pandas as pd
import math

class Utils:

    @staticmethod
    def Count(column):
        return sum(1 for value in column if not pd.isna(value))
    
    @staticmethod
    def Mean(column):
        if (Utils.Count(column) == 0):
            return None
        return sum(float(value) for value in column if not pd.isna(value)) / Utils.Count(column)
    
    @staticmethod
    def Std(column):
        if (Utils.Count(column) == 0):
            return None
        return math.sqrt(sum((float(value) - Utils.Mean(column))**2 for value in column if not pd.isna(value)) / Utils.Count(column))
    
    @staticmethod
    def Min(column):
        if (Utils.Count(column) == 0):
            return None
        val_min = float(column[0])
        for value in column[1:]:
            if val_min > float(value):
                val_min = float(value)
        return val_min
    
    @staticmethod
    def Max(column):
        if (Utils.Count(column) == 0):
            return None
        val_max = float(column[0])
        for value in column[1:]:
            if val_max < float(value):
                val_max = float(value)
        return val_max

    @staticmethod
    def Mediane(column):
        count = Utils.Count(column)
        if (count == 0):
            return None
        column = [float(value) for value in column if not pd.isna(value)]
        column = sorted(column)
        if count % 2 == 0:
            return (column[int(count / 2)] + column[int((count / 2) - 1)]) / 2
        else:
            return column[int((count - 1) / 2)]
    
    @staticmethod
    def Quartile(column):
        count = Utils.Count(column)
        if (count < 4):
            return None
        column = [float(value) for value in column if not pd.isna(value)]
        column = sorted(column)
        if (count % 2 == 0):
            return (Utils.Mediane(column[0:(count // 2) - 1]), Utils.Mediane(column[count // 2:]))
        else:
            return (Utils.Mediane(column[0:count // 2]), Utils.Mediane(column[(count) // 2:]))

    @staticmethod
    def normalize_column(column):
        normalized_column = column.copy()
        normalized_column = (normalized_column - normalized_column.min()) / (
            normalized_column.max() - normalized_column.min())
        return normalized_column
    
    def classify_values(value):
        try: 
            pd.to_numeric(value)
        except (ValueError, TypeError):
            raise TypeError()
    
    @staticmethod
    def keep_num_values(df):
        for column in df.columns:
            try:
                df[column].apply(Utils.classify_values)
            except (TypeError):
                df = df.drop(column, axis=1)
        return df