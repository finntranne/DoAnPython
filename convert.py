import pandas as pd
import csv
from package.cleaning import loadAndCleanCSV

inFile = "Males.csv"
outFile = "NewMales.csv"

loadAndCleanCSV(inFile,outFile)

df = pd.read_csv("NewMales.csv")

df['age'] = 6 + df['school'] + df['exper']

df['exper level'] = pd.cut(df['exper'], bins=[0, 3, 8, 12, 18], labels=['beginner', 'intermediate', 'advanced', 'expert'], right=True)

df['school level'] = pd.cut(df['school'], bins=[0, 5, 9, 12, 16], labels=['very low', 'low', 'intermediate', 'high'], right=True)

df['wage level'] = pd.cut(df['wage'], bins=[-float('inf'), -2, 0, 2, 3.5, float('inf')], labels=['very low', 'low', 'medium', 'high', 'very high'], right=True)

df.to_csv("NewMales.csv", index=False)
