import streamlit as st
from streamlit_phone_number import st_phone_number
import datetime
import csv

st.set_page_config(layout="wide")

with st.form("HACLA CLC PARTICIPATION"):
    st.write("Computer Lab Sign-In/Laboratorio De Computación Registro")

    with open("hacla_properties.txt") as file:
        hacla_sites_tuple = sorted(tuple(file.read().splitlines()))

    cola, colb, colc, cold = st.columns(spec=[.5, .25, .12, .12])

    with cola:
        site = st.selectbox("HACLA Site/Residencia de HACLA", hacla_sites_tuple,
                            placeholder="Choose an option")

    with colb:
        resident = st.radio("Are you a HACLA Resident?/¿Es usted residente de HACLA?", ["Yes/Sí", "No/No"], horizontal=True)

    with colc:
        unit = st.number_input("Unit/Unidad:", value=0)
        #else:
         #   unit = st.number_input("Unit/Unidad", label_visibility="collapsed")

    with cold:
        age = st.number_input("Age/Edad:", value=0)

    col1, col2 = st.columns(2)

    with col1:
        fn = st.text_input("First Name/Nombre:")

        col1a, col1b = st.columns(2)

        with col1a:
            #contact_method = st.selectbox("How would you like to be contacted?/"
            #                       "¿Cómo le gustaría que nos comuniquemos con usted?",
            #                       ("Mobil Phone/Teléfono Móvil", "Home Phone/Teléfono Residencial",
            #                        "Email/Correo Electrónico"),
            #                       placeholder="Choose an option")
            phone_number = st_phone_number(f":blue[{'Phone Number/Número Telefónico'}]", placeholder="XXX-XXX-XXXX", default_country="US")

        with col1b:
            email = st.text_input("Email/Correo Electrónico")

    with col2:
        ln = st.text_input("Last Name/Apellido:")

        col3, col4 = st.columns(2)

        with col3:
            dt_now = datetime.datetime.now()
            dt = st.date_input("Date of Visit/Fecha de Visita:", dt_now, format="MM/DD/YYYY")

        with col4:
            tm = st.text_input("Check-In Time/Hora de Registro", datetime.time(dt_now.hour, dt_now.minute))




    submit = st.form_submit_button("Submit")

    if submit:
        st.write("fag")
