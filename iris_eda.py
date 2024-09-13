import streamlit as st
import pandas as pd 

url = 'https://raw.githubusercontent.com/rusita-ai/data/master/iris.csv'
DF = pd.read_csv(url)
