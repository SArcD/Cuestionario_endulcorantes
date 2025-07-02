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



st.header("2️⃣ Cuestionario Índice de Alimentación Saludable")

# Define preguntas, opciones y puntuación
ias_preguntas = {
    "¿Con qué frecuencia consume cereales y sus derivados?": [10, 7.5, 5, 2.5, 0],
    "¿Con qué frecuencia consume verduras?": [10, 7.5, 5, 2.5, 0],
    "¿Con qué frecuencia consume frutas frescas?": [10, 7.5, 5, 2.5, 0],
    "¿Con qué frecuencia consume lácteos bajos en grasa?": [10, 7.5, 5, 2.5, 0],
    "¿Con qué frecuencia consume carnes rojas no procesadas?": [2.5, 7.5, 10, 5, 0],
    "¿Con qué frecuencia consume leguminosas cocidas?": [2.5, 7.5, 10, 5, 0],
    "¿Con qué frecuencia consume embutidos y carnes procesadas?": [0, 2.5, 5, 7.5, 10],
    "¿Con qué frecuencia consume postres y dulces?": [0, 2.5, 5, 7.5, 10],
    "¿Con qué frecuencia consume refrescos o bebidas con azúcar añadida?": [0, 2.5, 5, 7.5, 10]
}

opciones = [
    "Diario",
    "3 o más veces a la semana pero no diario",
    "1 o 2 veces a la semana",
    "Menos de 1 vez a la semana",
    "Nunca o casi nunca"
]

ias_puntuacion = 0

for pregunta, puntos in ias_preguntas.items():
    respuesta = st.radio(pregunta, opciones, key=pregunta)
    ias_puntuacion += puntos[opciones.index(respuesta)]

# Variedad de la dieta
variedad_puntos = 0
if st.checkbox("¿Respondió 'Diario' en preguntas 1 a 4?"):
    variedad_puntos += 2 * 4  # ejemplo: suma fija si todas son 'Diario'

ias_total = ias_puntuacion + variedad_puntos

st.write(f"Puntuación total IAS: {ias_total}")

if ias_total < 50:
    st.warning("Clasificación: No saludable")
elif 50 <= ias_total <= 80:
    st.info("Clasificación: Necesita cambios")
else:
    st.success("Clasificación: Saludable")

