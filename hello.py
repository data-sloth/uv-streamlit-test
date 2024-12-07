from lib import utils
import streamlit as st

def main():
    st.header("Hello from test2!")
    val = utils.div(1,2)
    st.write(val)

if __name__ == "__main__":
    main()

