import pandas as pd, numpy as np, json, math, sys
import matplotlib.pyplot as plt
import statsmodels.api as sm



'''
The Anomaly; Making Predictions

We saw in the example script we did in class that the mean state of the Arctic
will be ice-free in 2212 according to the linear model we derived from the data.
Ice minimum occurs annually in September.  When will Sept become ice-free?
What about March, the annual maximum?  Are they changing at the same rate?
Let's take a look now.

After: Antarctic sea ice.

When I say a line is a better model for Arctic Sea Ice Extent, what do 
I mean?  I mean that it makes better predictions of what will happen in the
future.  (From a technical point of view, it has smaller errors.  i.e. fits
the data better.)  The September sea ice next year is extremely likely to 
be closer to the line than the mean.

Revisiting hw5, fig 1: after what we've learned, is std dev the best 
measure of variability in Arctic Sea Ice Extent?  No RMSE is better.  
Because a line is a better model. Sd overestimates variability.

What possible problems are there with our predictions?  Nonlinear response
of ice to warming.  Changes in human behavior.

Compare the two figures.  How are the curves in Figure 1 related to the 
curves in Figure 2?  They are exactly the same shape, we have just subtracted
a constant from all of the y-values.  Why do they look different?  Because so
much more of the number of line is represented along the y-axis of Figure 1.
Therefore, the curves look squished vertically relative to Figure 2.  What's the
point of plotting the anomaly?  Figure 2 shows much more clearly how different 
the behavior is in summer vs. winter.  You can see much more clearly that
summer sea ice is diminishing much more rapidly than winter sea ice.
'''

def get_Mar_Sept_frame():
    '''
    This function takes no arguemnts. Reads data_79_17.csv into a hw4
    frame, creates and returns a frame.
    '''
    #########GIVEN############
    years_frame = pd.read_csv('data_79_17.csv', index_col=0)
    # will need to illustrate getting the mean of a row
    years_frame['March_means'] = years_frame.loc[:, '0301':'0331'].mean(axis=1)
    years_frame['March_anomalies'] = years_frame['March_means'] - years_frame['March_means'].mean() 
    years_frame['September_means'] = years_frame.loc[:, '0901':'0930'].mean(axis=1)
    years_frame['September_anomalies'] = years_frame['September_means'] - years_frame['September_means'].mean()
    return years_frame.loc[:, 'March_means':]
    
def get_ols_parameters():
    '''
    This function takes a Series, fits a line to it, and returns the slope, intercept, R^2,
    and the p-value in a list.
    '''
    pass
    
def make_prediction(params, description='x-intercept:', x_name='x', y_name='y', ceiling=False):
    '''
    Gets the x-intercept for an ols line.
    
    '''
    
    #####GIVEN######
    
    intercept = math.ceil(-params[1] / params[0]) if ceiling else -params[1] / params[0]
    print(description, intercept)
    # The following will print as dd.0 if params[2] is type np.float64.  Go figure.
    print(str(round(params[2] * 100)) + '% of variation in', y_name, 'accounted for by', x_name, '(linear model)')
    print('Significance level of results:', str(round(params[3] * 100, 1)) + '%')
    if params[3] <= 0.05:
        print('This result is statistically significant.')
    else:
        print('This result is not statistically significant.')
        
def make_fig_1():
    pass
    
def make_fig_2():
    pass
    
def main():
    pass
    
if __name__ == "__main__":
    main()