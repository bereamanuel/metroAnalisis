def flatten(t): 
    """
    Utilizamos la funcion para apilar listas
    """
    return [item for sublist in t for item in sublist]

def boxplots_algorithms(results, names):
    """ 
    For plot the results
    
    Para plotear los resultados 
    Input
    --------
    results (Pandas DF): Results of training models
    names: Names of the models

    Output
    --------
    Image in the notebook
    """
    import matplotlib.pyplot as plt

    plt.figure(figsize=(8,8))
    plt.boxplot(results)
    plt.xticks(range(1,len(names)+1), names)
    plt.show()


def mediasMoviles(df,n):
    c = df.rolling(n).mean().fillna(method = 'bfill')
    return c

def desvestMovil(df,n):
    c = df.rolling(n).std().fillna(method = 'bfill')
    return c

def medianMovil(df,n):
    c = df.rolling(n).median().fillna(method = 'bfill')
    return c

def diffDF(df,n):
    c = df.diff(n).fillna(method = 'bfill')
    return c