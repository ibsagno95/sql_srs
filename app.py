#pylint:disable=missing-module-docstring
import io
import os

import duckdb
import pandas as pd
import streamlit as st

if "data" not in os.listdir():
    os.mkdir("data")

if "sql_exercises.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())

con = duckdb.connect(database="data/sql_exercises.duckdb",read_only=False)

with st.sidebar:
    theme = st.selectbox(
        "what would you like to review?",
        ("cross_joins", "GroupBy", "Windows functions"),
        index=None,
        placeholder="select a theme",
    )

    st.write("You selected", theme)

    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}' ").df().sort_values("last_reviewed").reset_index()
    st.write(exercise)

    exercise_name = exercise.loc[0,"exercise_name"]

    with open(f"answer/{exercise_name}.sql","r") as f:
        answer_str=f.read()

    solution_df = con.execute(answer_str).df()

st.title("Mon premier APP")

st.header("Entrez votre code")

query = st.text_area(label="entrez votre input", key="user_input")

if query:
    result = con.execute(query).df()
    st.dataframe(result)

    if len(solution_df.columns) != len(result.columns):
        st.write("Il manque des colonnes")

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Il manque des colonnes")

    n_difference = abs(solution_df.shape[0] - result.shape[0])

    if n_difference != 0:
        st.write(f"Il y'a {n_difference} lignes de difference entre les solution")



tab1, tab2 = st.tabs(["Tables", "Solution"])
with tab1:
    exercises_tables = exercise.loc[0,"tables"]
    for table in exercises_tables:
        st.write(f"table: {table}")
        df_table=con.execute(f"SELECT * FROM {table} ").df()
        st.dataframe(df_table)


with tab2:
    st.text(answer_str)