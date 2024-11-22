import pandas as pd
import csv
from package.cleaning import loadAndCleanCSV

inFile = "Males.csv"
outFile = "NewMales.csv"

df = loadAndCleanCSV(inFile,outFile)
