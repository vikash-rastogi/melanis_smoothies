# Import python packages.
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app.
st.title(f"Place your order for healthy smoothie :cup_with_straw:")

name_on_order = st.text_input("Name on Smoothie:")
st.write("Your name on Smoothie woule be:", name_on_order)

session = get_active_session()
fruit_names = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# st.dataframe(data=my_dataframe, use_container_width=True)


ingredient_list = st.multiselect(
    "Choose upto 5 ingredients:",
    fruit_names,
    max_selections=5
)

# if ingredient list is not null
if ingredient_list: 
    # st.write(ingredient_list)
    # st.text(ingredient_list)

    ingredients_string = ''

    for fruit_chosen in ingredient_list:
        ingredients_string += fruit_chosen + ' '

    st.write(ingredients_string) 

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
                    values ('""" + ingredients_string + """', '""" + name_on_order + """')"""

    # st.write(my_insert_stmt)
    time_to_insert = st.button('Submit Order')
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success(f'{name_on_order}! Your Smoothie is ordered!', icon="✅")

import requests  
smoothiefroot_response = requests.get("[https://my.smoothiefroot.com/api/fruit/watermelon](https://my.smoothiefroot.com/api/fruit/watermelon)")  
st.text(smoothiefroot_response)
    
