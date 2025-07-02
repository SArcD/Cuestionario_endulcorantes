import streamlit as st

st.title("Cuestionario: Asociación del consumo de edulcorantes no calóricos")

st.header("1️⃣ Datos sociodemográficos y clínicos")

# Datos personales
nombre = st.text_input("Nombre del paciente")
fecha_nacimiento = st.date_input("Fecha de nacimiento")
numero_contacto = st.text_input("Número de contacto")
municipio = st.text_input("Municipio")
ocupacion = st.text_input("Ocupación")

estado_civil = st.selectbox(
    "Estado civil",
    ["Casado", "Soltero", "Divorciado", "Viudo", "Unión libre"]
)

nivel_educacion = st.selectbox(
    "Nivel de educación formal",
    ["Ninguno", "Primaria", "Secundaria", "Bachillerato", "Universitario", "Postgrado"]
)

# Escala Framingham
st.subheader("Datos de escala clásica de Framingham")
sexo = st.radio("Sexo", ["Masculino", "Femenino"])
edad = st.number_input("Edad", min_value=0, max_value=120, step=1)
pas = st.number_input("Presión arterial sistólica (PAS)")
tabaquismo = st.radio("¿Presenta el hábito de tabaquismo?", ["Sí", "No"])
diabetes = st.radio("¿Presenta diagnóstico de diabetes por un médico?", ["Sí", "No"])

# Datos antropométricos
st.subheader("Datos antropométricos")
peso = st.number_input("Peso (kg)")
talla = st.number_input("Talla (m)")
imc = st.number_input("IMC (kg/m2)")
icc = st.number_input("Índice cintura cadera")

# Datos del expediente
st.subheader("Datos del expediente clínico")
col_total = st.number_input("Colesterol total")
col_hdl = st.number_input("Colesterol HDL")
hba1c = st.number_input("HbA1c (%)")
glucosa = st.number_input("Glucosa (mg/dL)")
das28 = st.number_input("DAS28")
pcr = st.number_input("Proteína C reactiva")
factor_reumatoide = st.number_input("Factor reumatoide")
vsg = st.number_input("Velocidad de sedimentación globular")
leucocitos = st.number_input("Leucocitos totales")
tiempo_enfermedad = st.text_input("Tiempo de evolución de la enfermedad")
comorbilidades = st.text_area("Comorbilidades")
comorbilidades_cv = st.text_area("Comorbilidades cardiovasculares")
tratamiento = st.text_area("Tratamiento")
