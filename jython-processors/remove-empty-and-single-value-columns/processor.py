# This file is the actual code for the custom Jython step remove-empty-and-single-value-columns

import logging


# global- and project-level variables are passed as a dss_variables dict

# the step parameters are passed as a params dict

# Define here a function that returns the result of the step.
def process(rows):
    print("======================== process start ==============================")

    def find_empty_columns(df):
        """x"""
        return [col for col in df.columns if df[col].isnull().all()]
    
    # row is a dict of the row on which the step is applied
    # import pandas as pd
    # df = pd.DataFrame(rows)
    print("======================== about to reference pandas ==============================")
    df = pandas.DataFrame(rows)
    print("======================== past pandas reference ==============================")

    df_output = df.drop(find_empty_columns(df), axis=1)

    for col in df_output:
        if(len(df_output.loc[:,col].unique()) < 2):
            df_output.pop(col)

    return df_output.to_dict()
