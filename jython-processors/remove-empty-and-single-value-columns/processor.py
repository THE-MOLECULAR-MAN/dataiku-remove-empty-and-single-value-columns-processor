# This file is the actual code for the custom Jython step remove-empty-and-single-value-columns

# global- and project-level variables are passed as a dss_variables dict

# the step parameters are passed as a params dict

# Define here a function that returns the result of the step.
def process(rows):
    # row is a dict of the row on which the step is applied
    

    def find_empty_columns(df):
        """x"""
        return [col for col in df.columns if df[col].isnull().all()]
    
    df = pd.DataFrame(rows)


    python_test1_df = df.drop(find_empty_columns(df), axis=1)
    # python_test1_df.dropna(thresh=2, axis=1, inplace=True)

    for col in python_test1_df:
        if(len(python_test1_df.loc[:,col].unique()) < 2):
            python_test1_df.pop(col)

    
    
    return str(type(rows))
