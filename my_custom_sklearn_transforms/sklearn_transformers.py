from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
    
class RemoverNotasMaioresQue10(BaseEstimator, TransformerMixin):
    def __init__(self, column):
        self.columns = column

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        df_remove = data.loc[(data[column] > 10)] 
        # Retornamos um novo dataframe sem as linhas com notas maiores que 10
        return data.drop(df_remove.index)
        
         
