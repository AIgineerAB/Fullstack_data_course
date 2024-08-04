import streamlit as st
import pandas as pd


def layout():
    st.markdown("# First dashboard")
    st.markdown(
        "The source of the dataset comes from here https://www.kaggle.com/datasets/nitishsharma01/olympics-124-years-datasettill-2020"
    )


if __name__ == "__main__":
    layout()
