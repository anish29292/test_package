import pandas as pd
import numpy as np

def create_empty_dataframe(new_column_list, num_rows):

    col_list = new_column_list
    num_missing_cols = len(new_column_list)
    fill_with_zeroes = np.zeros(shape=(num_rows, num_missing_cols))
    new_df = pd.DataFrame(fill_with_zeroes, columns=[col_list])
    return new_df
