#Program to read in information on EU referendum results and constituency \
#demographics and use them to predict voter preferences using ML techniques

def pritn(x):
    print(x)
    return 0

def main():

    import pandas

    print("Hello voting")

    #Reading in EU referendum results in to data frame
    referendum_results_filename = 'eureferendum_constitunecy.xlsx'
    referendum_results_df = pandas.read_excel(referendum_results_filename, sheet_name='DATA', skiprows=3)

    # print(referendum_results_df)
    print(referendum_results_df.columns.ravel())
    print(referendum_results_df[1:10])
    pritn(referendum_results_df[['ONS ID']])

    #Removing data with ONS ID of NaN
    referendum_results_df.dropna(subset=['ONS ID'], how='any', inplace = True)
    print(referendum_results_df)

    #Removing data with ONS ID that doesn't start with E i.e. not from England
    referendum_results_df = referendum_results_df[referendum_results_df['ONS ID'].str.contains('E')]
    # referendum_results_df = referendum_results_df.drop(referendum_results_df[ (referendum_results_df['ONS ID']) == 'E'].index)

    print(referendum_results_df['ONS ID'])

    # print(referendum_results_df.columns())
    for column in referendum_results_df.columns:
        print(column)

    #Removing column if all of it is NaN
    referendum_results_df = \
    referendum_results_df.dropna(axis = 1, how='all')

    #Removing CH leave estimate, Known result, and Known leave headers
    referendum_results_df = \
    referendum_results_df.drop(columns = ['CH leave estimate', 'Known leave', 'Known leave'])

    print(referendum_results_df)
    #Reading in age descriptions in to data frame

    #Calculating mean, median and mode for ages


    #Plotting


main()
