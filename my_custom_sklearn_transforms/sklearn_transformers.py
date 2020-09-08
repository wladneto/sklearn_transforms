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
    
class Ingles(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        data.update(data['INGLES'].fillna(0))
        data['INGLES'] = data['INGLES'].astype('bool')
        return data

class NotasNaoPreenchidas(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        #adiciona coluna de medias relacionadas
        df = X.copy()
        m_DE = df.loc[df["NOTA_DE"] >= 0, "NOTA_DE"].mean()
        m_EM = df.loc[df["NOTA_EM"] >= 0, "NOTA_EM"].mean()
        m_MF = df.loc[df["NOTA_MF"] >= 0, "NOTA_MF"].mean()
        m_GO = df.loc[df["NOTA_GO"] >= 0, "NOTA_GO"].mean()
        
        df.update(df['NOTA_DE'].fillna(m_DE))
        df.update(df['NOTA_EM'].fillna(m_EM))
        df.update(df['NOTA_MF'].fillna(m_MF))
        df.update(df['NOTA_GO'].fillna(m_GO))
        
        df.loc[df.NOTA_GO > 10, 'NOTA_DE'] = 10
        df.loc[df.NOTA_EM > 10, 'NOTA_EM'] = 10 
        df.loc[df.NOTA_MF > 10, 'NOTA_MF'] = 10 
        df.loc[df.NOTA_GO > 10, 'NOTA_GO'] = 10 
        
        df.loc[df.NOTA_DE <= 0, 'NOTA_DE'] = m_DE
        df.loc[df.NOTA_EM <= 0, 'NOTA_EM'] = m_EM 
        df.loc[df.NOTA_MF <= 0, 'NOTA_MF'] = m_MF
        df.loc[df.NOTA_GO <= 0, 'NOTA_GO'] = m_GO

        return df  

class MediasRelacionadas(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        #adiciona coluna de medias relacionadas
        df = X.copy()
        df['REPROVACOES_H'] = df['REPROVACOES_DE'] + df['REPROVACOES_EM']
        df['REPROVACOES_E'] = df['REPROVACOES_MF'] + df['REPROVACOES_GO']
        df['MEDIA_H'] = ((df['NOTA_DE']+df['NOTA_EM'])/2)/10
        df['MEDIA_E'] = ((df['NOTA_MF']+df['NOTA_GO'])/2)/10
        df['NOTA_DE'] = df['NOTA_DE']/10
        df['NOTA_EM'] = df['NOTA_EM']/10
        df['NOTA_MF'] = df['NOTA_MF']/10
        df['NOTA_GO'] = df['NOTA_GO']/10
        df['MEDIA_GERAL'] = (df['NOTA_DE']+df['NOTA_MF']+df['NOTA_EM']+df['NOTA_GO'])/4
        
        return df
