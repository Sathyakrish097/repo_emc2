import pandas as pd
import numpy as np
import datetime


def main():
    start_time= datetime.time()
    
    df_test= pd.read_csv(r'D:\Power BI\Utube-tute\Hospitality-Project\fact_aggregated_bookings.csv')
    print(df_test.columns)
    print(df_test.shape)
    print("File loaded")
    
    print("Script has Completed")
    
    end_time= datetime.time()
    
    total= (end_time-start_time)/60
    print("Total time taken: ", total)

if __name__ == "__main__":
    main()