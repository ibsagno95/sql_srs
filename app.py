import streamlit as st
import pandas as pd
import duckdb
import io
from pygments.lexer import default

st.title ("Mon premier APP")

st.write("SQL repetition practice")

option = st.selectbox(
    "what would you like to review?",
    ("Joins","GroupBy","Windows functions"),
    index=None,
    placeholder = "select a theme"
)

st.write("You selected",option)

csv = '''
beverage,price
orange juice,2.5
Expresso,2
Tea,3
'''
beverages = pd.read_csv(io.StringIO(csv))

csv2 = '''
food_item,food_price
cookie,2.5
choco,2.5
muffin,3
'''
food_items = pd.read_csv(io.StringIO(csv2))

answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution = duckdb.sql(answer).df()
st.header("Entrez votre code")

query = st.text_area(label="entrez votre input",key="user_input")

if query: #Affichage conditionnelle
    result = duckdb.sql(query).df()
    st.dataframe(result)

tab1,tab2 = st.tabs(["Tables","Solution"])

with tab1:
    st.write("table:beverages")
    st.dataframe(beverages)
    st.write("tables: food_items")
    st.dataframe(food_items)
    st.write("expected table:")
    st.dataframe(solution)

with tab2:
    st.write(answer)

#data = {"a": [1, 2, 3], "b": [4, 5, 6]}
#df = pd.DataFrame(data)

#tab1 = st.tabs(["text"])

#with tab1:
#sql_query = st.text_area(label="entrez votre input")
#result= duckdb.query(sql_query).df()
#query = st.write(f"vous avez rentrez la requête suivante {sql_query}")
#st.dataframe(result)



