import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# import utils

def run_eda_app():
    
    url = 'https://raw.githubusercontent.com/rusita-ai/data/master/iris.csv'
    iris = pd.read_csv(url)
    st.markdown('## Iris Dataset')
    st.write(iris)

    submenu = st.sidebar.selectbox('Sub Menu', ['Statistic', 'Visualization', 'Analytics'])
    if submenu == 'Statistic':
        st.dataframe(iris)
        with st.expander('Data Type'):
            result_a = pd.DataFrame(iris.dtypes)
            st.write(result_a)
        with st.expander('Statistics'):
            result_b = iris.describe()
            st.write(result_b)
        with st.expander('Frequency'):
            st.write(iris['species'].value_counts())

    elif submenu == 'Visualization':
        st.title('Title')
        with st.expander('Scatter'):
            fig_a = px.scatter(iris,
                            x = 'sepal_width',
                            y = 'sepal_length',
                            color = 'species',
                            size = 'petal_width',
                            hover_data = ['petal_length'])
            st.plotly_chart(fig_a)
            
        col_1, col_2 = st.columns(2)
        with col_1:
            st.title('seaborn')
            fig, ax = plt.subplots()
            ax = sns.boxplot(iris,
                            x = 'sepal_width',
                            y = 'sepal_length',
                            ax = ax)
            st.pyplot(fig)
            
        with col_2:
            st.title('matplotlib')
            fig, ax = plt.subplots()
            ax.hist(iris['sepal_length'],
                    color = 'green')
            st.pyplot(fig)
            
        tab_1, tab_2, tab_3, tab_4, tab_5 = st.tabs(['Select', 'Setosa', 'Versicolor', 'Virginica', 'Kaggle'])
        with tab_1:
            with tab_1:
                choice_0 = st.selectbox('Iris Data', iris['species'].unique())
                result_0 = iris[iris['species'] == choice_0]
                
                st.title('plotly')
                fig_0 = px.scatter(result_0,
                                x = 'sepal_width',
                                y = 'sepal_length',
                                size = 'sepal_width',
                                hover_data = ['sepal_length'])
                st.plotly_chart(fig_0)

        with tab_2:
            st.write('Setosa')
            choice_1 = iris['species'].unique()[0]
            result_1 = iris[iris['species'] == choice_1]
            fig_1 = px.scatter(result_1,
                            x = 'sepal_width',
                            y = 'sepal_length')
            st.plotly_chart(fig_1)
            
        with tab_3:
            st.write('Versicolor')
            choice_2 = iris['species'].unique()[1]
            result_2 = iris[iris['species'] == choice_2]
            fig_2 = px.scatter(result_2,
                            x = 'sepal_width',
                            y = 'sepal_length')
            st.plotly_chart(fig_2)
            
        with tab_4:
            st.write('Virginica')
            choice_3 = iris['species'].unique()[2]
            result_3 = iris[iris['species'] == choice_3]
            fig_3 = px.scatter(result_3,
                            x = 'sepal_width',
                            y = 'sepal_length')
            st.plotly_chart(fig_3)
            
        with tab_5:
            pass
        
    elif submenu == 'Analytics':
        pass
    else:
        st.warning('Warning')