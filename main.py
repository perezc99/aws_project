import streamlit as st
from pathlib import Path
from streamlit_phone_number import st_phone_number
import datetime

st.set_page_config(layout="wide")

#hacla_logo = Path("hcc-hacla.gif")
st.image("images.png", width=200)

with open("hacla_properties.txt") as file:
    hacla_sites_tuple_tmp = sorted(tuple(file.read().splitlines()))

with open("reasons.txt") as file2:
    reasons_for_visit_tuple_tmp = sorted(tuple(file2.read().splitlines()))

hacla_sites_tuple_lst = list(hacla_sites_tuple_tmp)
hacla_sites_tuple_lst.insert(0, "")
hacla_sites_tuple = tuple(hacla_sites_tuple_lst)

reasons_for_visit_lst = list(reasons_for_visit_tuple_tmp)
reasons_for_visit_lst.insert(0, "")
reasons_for_visit_tuple = tuple(reasons_for_visit_lst)

site = st.selectbox("Which HACLA Computer Lab are you Visiting?/¿Cual Laboratorio de Computación de HACLA Estás Visitando?", hacla_sites_tuple,
                            placeholder="Choose an option")

if site == "":
    print("empty")
else:
    st.header("")
    st.header(f"Welcome to ***{site}'s Computer Lab***!")
    st.header(f"¡Bienvenido al ***Laboratorio de Computación de {site}***!")
    st.header("")


    visited_before = st.radio(f"Have You Signed-In Digitally Before?/¿Te Has Registrado Digitalmente Antes?", ["Yes/Sí", "No/No"],
                        horizontal=True)

    if visited_before == "Yes/Sí":
        with st.form("HACLA CLC PARTICIPATION", clear_on_submit=True):
            st.write("Computer Lab Sign-In/Laboratorio De Computación Registro")
            colw, colx, coly, colz = st.columns(4)

            with colw:
                dt_now = datetime.datetime.now()
                dt = st.date_input("Date of Visit/Fecha de Visita:", dt_now, format="MM/DD/YYYY")

            with colx:
                tm = st.text_input("Check-In Time/Hora de Registro", dt_now.strftime("%I:%M %p"))

            with coly:
                sign_in_token = st.text_input("Registration Code/Código de Registracion:")
                #st.write("code should look like")

            with colz:
                reason = st.selectbox("Reason for Visit/Motivo de la Visita:", reasons_for_visit_tuple,
                                      placeholder="Choose an option")
            submit = st.form_submit_button("Submit")

    else:
        with st.form("HACLA CLC PARTICIPATION", clear_on_submit=True):
            st.write("Computer Lab Sign-In/Laboratorio De Computación Registro")

            col1, col2, col3, col4, col5 = st.columns([.16,.16,.29,.29,.1])

            with col1:
                dt_now = datetime.datetime.now()
                dt = st.date_input("Date of Visit/Fecha de Visita:", dt_now, format="MM/DD/YYYY")

            with col2:
                tm = st.text_input("Check-In Time/Hora de Registro", dt_now.strftime("%I:%M %p"))

            with col3:
                fn = st.text_input("First Name/Nombre:")

            with col4:
                ln = st.text_input("Last Name/Apellido:")

            with col5:
                age = st.number_input("Age/Edad:", value=0)

            cola, colb, colc, cold, cole = st.columns([.16, .16, .24, .24, .20])

            with cola:
                phone_number = st.text_input("Phone Number/Número Telefónico", placeholder="XXX-XXX-XXXX")

            with colb:
                email = st.text_input("Email/Correo Electrónico")

            with colc:
                mode_of_contact = st.radio(f"Preferred Contact Method/Método de Contacto Preferido:",
                                           ["Phone Number/Número Telefónico",
                                            "Email/Correo Electrónico"], horizontal=True)
            with cold:
                resident = st.radio(f"Are you a Resident of {site}?/¿Es Ysted Residente de {site}?",
                                    ["Yes/Sí", "No/No"], horizontal=True)

            with cole:
                reason = st.selectbox("Reason for Visit/Motivo de la Visita:", reasons_for_visit_tuple,
                                    placeholder="Choose an option")
                #else:
                 #   unit = st.number_input("Unit/Unidad", label_visibility="collapsed")

            #with cold:

            submit = st.form_submit_button("Submit")

        if submit:
            site_lst = site.split(" ")
            new_token = ""
            for w in site_lst:
                new_token += w[0]
            if resident == "Yes/Sí":
                new_token += "R"
            else:
                new_token += "V"
            new_token += fn[0] + ln[0]
            new_token += str(age)
            st.title(f"Your future check in code is/Tu Código Futuro de Registro es: :rainbow[{new_token}]")
