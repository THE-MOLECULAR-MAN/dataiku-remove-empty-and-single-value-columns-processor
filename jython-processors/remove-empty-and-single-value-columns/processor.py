# This file is the actual code for the custom Jython step remove-empty-and-single-value-columns

import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format='remove-empty-and-single-value-columns-processor plugin %(levelname)s - %(message)s')

remove_empty_columns               = params.get('remove_empty_columns')
remove_columns_with_only_one_value = params.get('remove_columns_with_only_one_value')

logger.info("======================== about to import pandas ==============================")
import pandas
logger.info("======================== finished importing pandas ==============================")

# global- and project-level variables are passed as a dss_variables dict

# the step parameters are passed as a params dict

# Define here a function that returns the result of the step.
def process(rows):
    logger.info("======================== process start ==============================")

    def find_empty_columns(df):
        """x"""
        return [col for col in df.columns if df[col].isnull().all()]
    
    row is a dict of the row on which the step is applied
    import pandas as pd
    df = pd.DataFrame(rows)
    logger.info("======================== about to reference pandas ==============================")
    df = pandas.DataFrame(rows)
    logger.info("======================== past pandas reference ==============================")

    df_output = df.drop(find_empty_columns(df), axis=1)

    for col in df_output:
        if(len(df_output.loc[:,col].unique()) < 2):
            df_output.pop(col)

    return df_output.to_dict()