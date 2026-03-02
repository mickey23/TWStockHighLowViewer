# -*- coding: utf-8 -*-
def calculate_score(df):
    df['Score'] = df[['MA5','MA20','MA60','MA50','MA120']].sum(axis=1)
    return df['Score']
