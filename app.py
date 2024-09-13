import streamlit as st
from ml_app import run_ml_app
from eda_app import run_eda_app

def main():
    st.subheader('Iris EDA')
    
    menu = ['Home', 'EDA', 'ML', 'etc']
    choice = st.sidebar.selectbox('Menu', menu)
    
    if choice == 'Home':
        st.subheader('Home')
        pass
    elif choice == 'EDA':
        st.subheader('EDA')
        run_eda_app()
    elif choice == 'ML':
        st.subheader('ML')
        run_ml_app()
    else:
        st.subheader('etc')
        pass

if __name__ == '__main__':
    main()