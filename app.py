import pickle
import streamlit as st
import numpy as np 
import pandas as pd

st.title("Car Price prediction Using ML ")

# Loading pickle files here
final_model = pickle.load(open('webfiles/final_model.pkl', 'rb'))
df = pickle.load(open('webfiles/df.pkl', 'rb'))



# Getting Input from users
# Age Input
age = st.number_input(
    "Enter Age of your car *",
    placeholder='Enter Age of your car',max_value=80,value=None
)
# KM Input
km = st.number_input(
    "Enter Kilometer running of your car *",
    placeholder='Enter Kilometer running of your car',min_value=1,max_value=250000,value=None
)
# HP Input
hp = st.number_input(
    "Enter Horsepower of your car *",
    placeholder='Enter Horsepower of your car',min_value=50,max_value=2000,value=None
)
# cylinders Input
cylinders = st.selectbox(
    "Select number of Cylinders *",
    df.Cylinders.unique(), placeholder="Choose an option",index=None,
)
# Doors Input
doors = st.selectbox(
    "Select number of Doors *",
    df.Doors.unique(), placeholder="Choose an option",index=None,
)
# Weight Input
weight = st.number_input(
    "Enter Weight of your car *",
    placeholder='Enter Weight of your car',min_value=1000,max_value=3000,value=None
)
# Gears Input
gears = st.selectbox(
    "Select number of Gears *",
    df.Gears.unique(), placeholder="Choose an option",index=None,
)

# Function to predict price
def predict_price(final_model, age,km,hp,cylinders,doors,weight,gears):
    new_data = pd.DataFrame({'Age':age, 'KM':km, 'HP':hp, 'Doors':doors, 'Cylinders':cylinders, 'Gears':gears, 'Weight':weight}, index=[1])
    prediction = final_model.predict(new_data).iloc[0]
    # new_data = 1241242
    return prediction

st.write('All fields are mandatory *')
if st.button('Check Price'):
    data = predict_price(final_model,age,km,hp,cylinders,doors,weight,gears)
    st.text('Your Car Price is:')
    st.text(round(data,2))