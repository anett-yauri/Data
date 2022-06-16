import streamlit as st
import pandas as pd
import gdown

# id = 1yeuGoOyUwFqspXrFO38NMwyTr3A70QZt
@st.experimental_memo

def download_data(ID, output):
  #https://drive.google.com/uc?id=
  url = "https://drive.google.com/uc?id="+id
  #output = 'data.csv'
  gdown.download(url,output,quiet=False)

ID = ["1yeuGoOyUwFqspXrFO38NMwyTr3A70QZt","1DNg5Q-9cbrma29MUiboao9Tvqdz2S4OG","1FN1Kfk8-VxhFYfr-nwlUS1UJbbwrBbjY","14XXeYmJDDxzHhuwGgPs2vhf4VZ1U2HwN",
"17AcQoWeZCOBaE7VXvlXvEv8cL5hiakBI","10kFn6tCRt1oC4E9hdNKgllayTqYPfIrj","1Fi6Nx2Q0J6tbNIYkEnkX07EaLg4g-3aL","1rB1guYHETcsXHwJziaq1CU3c_EuXgm2L",
"1gvoRrP82043bixWXnpOtQCckfVIbDMNB","1mfCl7rKGqgeq-HoIgnR9wSwu8fJG0t9V","1jxYnzKw7_jLmWvKNAwjrfjnZj7F_ECZx","1Ay91ksz32w7hAGlnC1jG5PGaS9usDtwM",
"1pPM4Ok65R-_cMEYs3gCvWckjvv2ZZaVP","1bsjoKMEvNHiGYQv7vehNSdVAnbguVmC8"]
output = ['julio_2020.csv','agosto_2020.csv','setiembre_2020_bonilla.csv','setiembre_2020_miraflores.csv',
'octubre_2020_miraflores.csv','octubre_2020_manuel.csv','noviembre_2020_manuel.csv','noviembre_2020_miraflores.csv',
'diciembre_2020_manuel.csv','diciembre_2020_miraflores.csv','enero_2021_manuel.csv','enero_2021_miraflores.csv',
'febrero_2021_miraflores.csv','marzo_2021_miraflores.csv']

for i in range(0,len(ID)):
    download_data(ID[i],output[i])
    data = pd.read_csv(output[i], sep = ';', parse_dates = ['Fecha'])
    concentraciones = data['CO (ug/m3)']
    st.line_chart(concentraciones)
