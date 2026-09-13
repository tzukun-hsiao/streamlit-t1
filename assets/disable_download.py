import streamlit as st


def hide_toolbar(key):
    st.markdown(
        f"""
        <style>
        .st-key-{key} [data-testid="stElementToolbar"] {{
            display: none;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
