import numpy as np
import yaml
import pandas as pd
import traceback
from pathlib import Path

try:
    #Load the config file that contains the options available for various operations
    yaml_file_name='Config.yaml' # The name of the config file used
    file_path=Path.cwd().joinpath(yaml_file_name)   
    with open(file_path) as file:
        config = yaml.load(file, Loader=yaml.SafeLoader)
    agg_options=config['Preprocessor']['aggregation_options']
except:
    print("Experienced an error while processing the configuration file. Check if the file exists in the directory specified.",traceback.print_exc())
	
def timestampRegularization(df,col,rule):
    # Fill in the missing timestamps in a discontinuous date time column. By default the columns are filled with NaNs where at he points of discontinuity
    """
    Regularizes the column which is the datetime column passed for the dataframe "df".

    Parameters
    ----------
    df : DataFrame object
        The dataframe to be passed
    Following parameters retrieved from yaml file
    col : str
        The name of the column containing the timestamps
    rule: str
        The frequency offset. Follow the below link to learn more about the frequency offsets available.
        https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects
    """
    
    #Check if the arguments are passed correctly
    if isinstance(df,pd.core.frame.DataFrame)==False:
        raise TypeError("Only Data frame objects to be passed for regularization")
    if isinstance(col,str)==False:
        raise TypeError("Only strings are allowed to be passed as column names")
    if isinstance(rule,str)==False:
        raise TypeError("Only strings are allowed to be passed as the frequency offset") 
    try:
        #Set the column to be regularized as the index
        df = df.set_index(pd.DatetimeIndex(df[col]))
        df = df.drop([col], axis=1)
        # Regularize the sensor observation
        df = df.asfreq(rule)
        return df        
    except:
        print("Experienced an error while processing\n",traceback.print_exc())

def resampleDataset(df,col,rule,agg='mean'):
    # resample the dataset to a different frequency
    """
    Upsamples/Downsamples the dataframe where col is the date time column( contatining the timestamps) for the dataframe "df".

    Parameters
    ----------
    df : DataFrame object
        The dataframe to be passed
    Following parameters retrieved from yaml file    
    col : str
        The name of the column containing the timestamps
    rule: str
        The frequency offset to be resampled to  
    agg: str
        Aggregation method to follow after resampling(eg.mean,sum).Default is mean     
    """
        
    #Check if the arguments are passed correctly
    if isinstance(df,pd.core.frame.DataFrame)==False:
        raise TypeError("Only Data frame objects to be passed for resampling")
    if isinstance(col,str)==False:
        raise TypeError("Only strings are allowed to be passed as column names")
    if isinstance(rule,str)==False:
        raise TypeError("Only strings are allowed to be passed as the frequency offset") 
    if isinstance(agg,str)==False:
        raise TypeError("Only strings are allowed to be passed as the aggregation method")
    elif agg not in agg_options:
        raise Exception(agg+"is an Unknown/unsupported aggregation type")
    else:
        pass    
        
    try:
        #Set the column to be resampled as the index of the dataframe
        df = df.set_index(pd.DatetimeIndex(df[col]))
        df = df.drop([col], axis=1)
        if agg=="mean":
            # Aggregate the resampled object
            df = df.resample(rule=rule).mean()
        elif agg=="sum":
            df = df.resample(rule=rule).sum()
        elif agg=="count":
            df = df.resample(rule=rule).count()
        elif agg=="min":
            df = df.resample(rule=rule).min()  
        elif agg=="max":
            df = df.resample(rule=rule).max()
        elif agg=="std":
            df = df.resample(rule=rule).std() 
        elif agg=="var":
            df = df.resample(rule=rule).var()
        elif agg=="last":
            df = df.resample(rule=rule).last()
        else:
            pass
        return df
    except:
        print("Experienced an error while processing\n",traceback.print_exc())

def capExtremeValues(df,col,lower=None,upper=None):
    #Sets the values lying outside the user defined boundaries, specified as lower and upper thresholds and replaces them with the same accordingly.
    
    """
    clips the columns of a dataframe based on the threshold values passed

    Parameters
    ----------
    df : DataFrame object
        The dataframe to be passed
    Following parameters retrieved from yaml file
    
    col : str
        The name of the column to be clipped
    lower : int
        The lower threshold limit
    upper : int
        The upper threshold limit       
    """
      
    #Check if the arguments are passed correctly
    if isinstance(df,pd.core.frame.DataFrame)==False:
        raise TypeError("Only Data frame objects to be passed for resampling")
    if isinstance(col,str)==False:
        raise TypeError("Only strings are allowed to be passed as column names")
    if isinstance(lower,(int,float,type(None)))==False:
        raise TypeError("Only strings are allowed to be passed as the operator") 
    if isinstance(upper,(int,float,type(None)))==False:
        raise TypeError("Only integers or floating point values are allowed to be passed as inputs")
        
    try:
        df[col] = df[col].clip(upper=upper,lower=lower)
        return df
    except:
        print("Experienced an error while processing\n",traceback.print_exc())		
