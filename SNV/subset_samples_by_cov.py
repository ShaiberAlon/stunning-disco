import pandas as pd
import numpy as np

def subset_samples_by_cov(mean_cov_file, thresh, output):
    """
    Outputs .txt file of sample names for samples that have mean coverage
    above a threshold value.
    
    INPUTS
    
    mean_cov_file:
        filepath of the mean coverage text file generated by anvi'o. I think 
        the default names are either "mean_coverage.txt" or 
        "mean_coverage_Q2Q3.txt"
    thresh:
        all samples with a mean coverage value below thresh will not be
        included in the output file
    output:
        filepath of output.
    """

    df = pd.read_csv(mean_cov_file, header=None, index_col=0, sep='\t')
    df = df.transpose()
    cols = df.columns.values
    df[cols[1]] = df[cols[1]].astype(float)

    df = df[df[cols[1]] >= thresh]
    df = df.sort_values(by=cols[1],ascending=True).reset_index(drop=True)

    print("{}\n\nsamples retained are above.".format(df))

    df.to_csv(output+".table",index=False,sep='\t')
    df_names = df[cols[0]]
    df_names.to_csv(output,index=False)

    print("list of names saved to {}".format(output))
    print("complete table saved to {}".format(output+".table"))
 
