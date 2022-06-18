import streamlit as st
import pandas as pd
import gdown
import streamlit as st
from streamlit_option_menu import option_menu

@st.experimental_memo
################################################################################
def download_data(ID, output):
  #https://drive.google.com/uc?id=
  url = "https://drive.google.com/uc?id="+ID
  #output = 'data.csv'
  gdown.download(url,output,quiet=False)
###########################
def lectura_grafico(filename):
    bd=pd.read_csv(filename,sep=";")
    download_data("1hChbBm8B6njU6pTH1bSTI9R-aWQhB0eg","Limites_ECA.csv")
    eca=pd.read_csv("Limites_ECA.csv",sep=";")

    x1=bd["CO (ug/m3)"]
    x2=bd["H2S (ug/m3)"]
    x3=bd["NO2 (ug/m3)"]
    x4=bd["O3 (ug/m3)"]
    x5=bd["PM10 (ug/m3)"]
    x6=bd["PM2.5 (ug/m3)"]
    x7=bd["SO2 (ug/m3)"]
#CO
    eca1=eca["CO (ug/m3)"]
    eca1=np.ones(len(x1.values))*eca1.values
    data1 = {"CO (ug/m3)":x1.values,'Límite ECA':eca1}
    data_frame1 = pd.DataFrame(data1)
#H2S
    eca2=eca["H2S (ug/m3)"]
    eca2=np.ones(len(x2.values))*eca2.values
    data2 = {"H2S (ug/m3)":x2.values,'Límite ECA':eca2}
    data_frame2 = pd.DataFrame(data2)
#NO2
    eca3=eca["NO2 (ug/m3)"]
    eca3=np.ones(len(x3.values))*eca3.values
    data3 = {"NO2 (ug/m3)":x3.values,'Límite ECA':eca3}
    data_frame3 = pd.DataFrame(data3)
#O3
    eca4=eca["O3 (ug/m3)"]
    eca4=np.ones(len(x4.values))*eca4.values
    data4 = {"O3 (ug/m3)":x4.values,'Límite ECA':eca4}
    data_frame4 = pd.DataFrame(data4)
#PM10
    eca5=eca["PM10 (ug/m3)"]
    eca5=np.ones(len(x5.values))*eca5.values
    data5 = {"PM10 (ug/m3)":x5.values,'Límite ECA':eca5}
    data_frame5 = pd.DataFrame(data5)
#PM2.5
    eca6=eca["PM2.5 (ug/m3)"]
    eca6=np.ones(len(x6.values))*eca6.values
    data6 = {"PM2.5 (ug/m3)":x6.values,'Límite ECA':eca6}
    data_frame6 = pd.DataFrame(data6)
#SO2
    eca7=eca["SO2 (ug/m3)"]
    eca7=np.ones(len(x7.values))*eca7.values
    data7 = {"SO2 (ug/m3)":x7.values,'Límite ECA':eca7}
    data_frame7 = pd.DataFrame(data7)

    print (st.line_chart(data_frame1))
    print (st.line_chart(data_frame2))
    print (st.line_chart(data_frame3))
    print (st.line_chart(data_frame4))
    print (st.line_chart(data_frame5))
    print (st.line_chart(data_frame6))
    print (st.line_chart(data_frame7))
################################################################################

ID= ["1yeuGoOyUwFqspXrFO38NMwyTr3A70QZt","1DNg5Q-9cbrma29MUiboao9Tvqdz2S4OG","1FN1Kfk8-VxhFYfr-nwlUS1UJbbwrBbjY","14XXeYmJDDxzHhuwGgPs2vhf4VZ1U2HwN",
"17AcQoWeZCOBaE7VXvlXvEv8cL5hiakBI","10kFn6tCRt1oC4E9hdNKgllayTqYPfIrj","1Fi6Nx2Q0J6tbNIYkEnkX07EaLg4g-3aL","1rB1guYHETcsXHwJziaq1CU3c_EuXgm2L",
"1gvoRrP82043bixWXnpOtQCckfVIbDMNB","1mfCl7rKGqgeq-HoIgnR9wSwu8fJG0t9V","1jxYnzKw7_jLmWvKNAwjrfjnZj7F_ECZx","1Ay91ksz32w7hAGlnC1jG5PGaS9usDtwM",
"1pPM4Ok65R-_cMEYs3gCvWckjvv2ZZaVP","1bsjoKMEvNHiGYQv7vehNSdVAnbguVmC8"]
output = ['julio_2020.csv','agosto_2020.csv','setiembre_2020_bonilla.csv','setiembre_2020_miraflores.csv',
'octubre_2020_miraflores.csv','octubre_2020_manuel.csv','noviembre_2020_manuel.csv','noviembre_2020_miraflores.csv',
'diciembre_2020_manuel.csv','diciembre_2020_miraflores.csv','enero_2021_manuel.csv','enero_2021_miraflores.csv',
'febrero_2021_miraflores.csv','marzo_2021_miraflores.csv']

for i in range(0,len(ID)):
    download_data(ID[i],output[i])
    lectura_grafico(output[i])
