import streamlit

#streamlit.title('hello world')
#streamlit.header('friends')
#streamlit.text('joey like food')
#streamlit.text('rachel like style')
#streamlit.text('monica like perfection')
#streamlit.text('chandler like sarcastic comments')
#streamlit.text('phoebe like rare things')
#streamlit.text('ross like marriage')
#streamlit.header('FAVOURITE')
#streamlit.text('HOW U DOING......')

import pandas

my_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_list = my_list.set_index('Fruit') 


streamlit.multiselect("pick some fruits from list:", list(my_list.index),['Grapefruit','Avocado'])
streamlit.dataframe(my_list)
