#created the main Python file
import streamlit as sl
sl.title('My Parents New Healthy Diner')
sl.header('Breakfast Favorites')
sl.text('🥣 Omega 2 & Blueberry Oat Meal')
sl.text('🥗 Kale, Spinach, and Rocket Smoothie')
sl.text('🐔 Hard-Boiled Free-Range Egg')
sl.text('🥑🍞 Avocado Toast')


sl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# added ability to pick fruits by Name rather than numbers (index numbers)
my_fruit_list = my_fruit_list.set_index('Fruit')

# Lets put a picklist here so they can choose the fruit they want to include
fruits_selected = sl.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display Table on the Page
sl.dataframe(fruits_to_show)

# New section to display Fruityvice advice
sl.header("Fruityvice Fruit Advice!")
fruit_choice = sl.text_input('What fruit would you like information about?', 'kiwi')
sl.write ('The Entered Choice is ' + fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#sl.text(fruityvice_response.json())

fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
sl.dataframe(fruityvice_normalized)


pip install h5py
pip install typing-extensions
pip install wheel
pip install urllib3==1.26.16

# import connector
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
sl.text("Hello from Snowflake:")
sl.text(my_data_row)
