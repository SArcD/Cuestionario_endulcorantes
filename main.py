import streamlit as st
import datetime



st.title("Cuestionario: Asociación del consumo de edulcorantes no calóricos")
# Etiquetas resumidas IAS
ias_labels = [
    "Cereales", "Verduras", "Frutas",
    "Lácteos", "Carnes", "Leguminosas",
    "Embutidos", "Postres", "Refrescos"
]



st.header("1️⃣ Datos sociodemográficos y clínicos")
# Valor por defecto: hoy menos 30 años (opcional)
default_date = datetime.date.today() - datetime.timedelta(days=30*365)

# Fecha mínima: hace 120 años
min_date = datetime.date.today() - datetime.timedelta(days=120*365)

# Fecha máxima: hoy
max_date = datetime.date.today()


# Datos personales
nombre = st.text_input("Nombre del paciente")
#fecha_nacimiento = st.date_input("Fecha de nacimiento")
# Campo Streamlit
fecha_nacimiento = st.date_input(
    "Fecha de nacimiento",
    value=default_date,
    min_value=min_date,
    max_value=max_date
)
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

st.header("3️⃣ Frecuencia de consumo de productos con edulcorantes no calóricos")

edulcorantes_preguntas = [
    "¿Con qué frecuencia consume sobres de sustituto de azúcar?",
    "¿Con qué frecuencia consume bebidas light o sin azúcar?",
    "¿Con qué frecuencia consume yogurt light sin azúcar?",
    "¿Con qué frecuencia consume gelatinas de caja versión regular o light?",
    "¿Con qué frecuencia consume chicles o pastillas sin azúcar?",
    "¿Con qué frecuencia consume saborizantes de agua en polvo?",
    "¿Con qué frecuencia consume postres y dulces sin azúcar?",
    "¿Con qué frecuencia consume cereales light o sin azúcar?"
]

opciones_edulcorantes = [
    "Diario",
    "Al menos 1 vez a la semana pero no diario",
    "Al menos 1 vez al mes pero no todas las semanas",
    "Nunca o muy pocas veces al año"
]

puntos_edulcorantes = [3, 2, 1, 0]

puntuacion_edulcorantes = 0

for pregunta in edulcorantes_preguntas:
    respuesta = st.radio(pregunta, opciones_edulcorantes, key=pregunta)
    puntuacion_edulcorantes += puntos_edulcorantes[opciones_edulcorantes.index(respuesta)]

st.write(f"Puntuación total edulcorantes: {puntuacion_edulcorantes} de 24")


import streamlit as st
import pandas as pd

# ------------------------------------
# 1. Captura de respuestas individuales
# ------------------------------------

# Índice de Alimentación Saludable
ias_respuestas = {}
for pregunta in ias_preguntas:
    respuesta = st.session_state.get(pregunta, "Sin respuesta")
    ias_respuestas[pregunta] = respuesta

# Cuestionario Edulcorantes
edulcorantes_respuestas = {}
for pregunta in edulcorantes_preguntas:
    respuesta = st.session_state.get(pregunta, "Sin respuesta")
    edulcorantes_respuestas[pregunta] = respuesta

# ------------------------------------
# 2. Construir diccionario de datos completo
# ------------------------------------

datos = {
    # Datos generales
    "Nombre": nombre,
    "Fecha nacimiento": fecha_nacimiento,
    "Contacto": numero_contacto,
    "Municipio": municipio,
    "Ocupación": ocupacion,
    "Estado civil": estado_civil,
    "Educación": nivel_educacion,
    "Sexo": sexo,
    "Edad": edad,
    "PAS": pas,
    "Tabaquismo": tabaquismo,
    "Diabetes": diabetes,
    "Peso": peso,
    "Talla": talla,
    "IMC": imc,
    "ICC": icc,
    "Colesterol total": col_total,
    "HDL": col_hdl,
    "HbA1c": hba1c,
    "Glucosa": glucosa,
    "DAS28": das28,
    "PCR": pcr,
    "Factor reumatoide": factor_reumatoide,
    "VSG": vsg,
    "Leucocitos": leucocitos,
    "Tiempo enfermedad": tiempo_enfermedad,
    "Comorbilidades": comorbilidades,
    "Comorbilidades CV": comorbilidades_cv,
    "Tratamiento": tratamiento,

    # Totales
    "Puntuación IAS": ias_total,
    "Puntuación Edulcorantes": puntuacion_edulcorantes
}

# Agregar cada respuesta individual IAS
for pregunta, respuesta in ias_respuestas.items():
    datos[f"IAS_{pregunta}"] = respuesta

# Agregar cada respuesta individual Edulcorantes
for pregunta, respuesta in edulcorantes_respuestas.items():
    datos[f"EDULCORANTES_{pregunta}"] = respuesta

# ------------------------------------
# 3. Convertir a DataFrame y permitir descarga
# ------------------------------------

df = pd.DataFrame([datos])
csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="📥 Descargar respuestas completas como CSV",
    data=csv,
    file_name="respuestas_cuestionario_completo.csv",
    mime="text/csv"
)



import pandas as pd

# ---------------------------------------
# Interpretación de IAS (ejemplo simple)
# ---------------------------------------

ias_analisis = []

for pregunta, respuesta in ias_respuestas.items():
    # Valor base de interpretación y recomendación
    analisis = ""
    recomendacion = ""

    if "cereales" in pregunta.lower():
        if respuesta == "Diario":
            analisis = "Consumo adecuado de energía. Revisar tipo de cereal."
            recomendacion = "Preferir integrales, moderar porciones."
        elif respuesta in ["3 o más veces a la semana pero no diario", "1 o 2 veces a la semana"]:
            analisis = "Consumo bajo."
            recomendacion = "Aumentar cereales saludables."
        else:
            analisis = "Consumo muy bajo."
            recomendacion = "Incluir cereales integrales en la dieta."

    elif "verduras" in pregunta.lower():
        if respuesta == "Diario":
            analisis = "Excelente consumo de verduras."
            recomendacion = "Mantener variedad."
        elif respuesta in ["3 o más veces a la semana pero no diario"]:
            analisis = "Consumo bueno pero no diario."
            recomendacion = "Aumentar frecuencia a diario."
        else:
            analisis = "Bajo consumo."
            recomendacion = "Incrementar verduras frescas."

    elif "frutas" in pregunta.lower():
        if respuesta == "Diario":
            analisis = "Buen aporte de vitaminas."
            recomendacion = "Mantener sin excesos de jugos."
        else:
            analisis = "Poca ingesta de fruta fresca."
            recomendacion = "Agregar fruta entera diariamente."

    elif "embutidos" in pregunta.lower():
        if respuesta == "Diario":
            analisis = "Consumo alto de carnes procesadas."
            recomendacion = "Reducir drásticamente por sodio y grasa."
        elif respuesta in ["3 o más veces a la semana pero no diario"]:
            analisis = "Consumo frecuente."
            recomendacion = "Limitar embutidos a esporádico."
        else:
            analisis = "Consumo bajo de procesados."
            recomendacion = "Mantener este hábito."

    else:
        analisis = "Verificar coherencia."
        recomendacion = "Ajustar si es necesario."

    ias_analisis.append({
        "Pregunta": pregunta,
        "Respuesta": respuesta,
        "Análisis": analisis,
        "Recomendación": recomendacion
    })

# ---------------------------------------
# Interpretación de Edulcorantes
# ---------------------------------------

edulcorantes_analisis = []

for pregunta, respuesta in edulcorantes_respuestas.items():
    if respuesta == "Diario":
        analisis = "Uso diario de edulcorantes en este producto."
        recomendacion = "Verificar tolerancia, ajustar si es excesivo."
    elif respuesta == "Al menos 1 vez a la semana pero no diario":
        analisis = "Consumo regular moderado."
        recomendacion = "Ok, mantener o reducir si se prefiere natural."
    elif respuesta == "Al menos 1 vez al mes pero no todas las semanas":
        analisis = "Consumo ocasional."
        recomendacion = "Sin problema."
    else:
        analisis = "No usa este tipo de producto."
        recomendacion = "Sin implicaciones."

    edulcorantes_analisis.append({
        "Pregunta": pregunta,
        "Respuesta": respuesta,
        "Análisis": analisis,
        "Recomendación": recomendacion
    })

# ---------------------------------------
# Unir en DataFrames y mostrar
# ---------------------------------------

df_ias = pd.DataFrame(ias_analisis)
df_edulcorantes = pd.DataFrame(edulcorantes_analisis)

st.subheader("🔍 Análisis de respuestas IAS")
st.dataframe(df_ias)
# ---------------------------------------
# 🟢 Semáforo nutricional IAS por grupo
# ---------------------------------------

ias_semaforo = []

for i, pregunta in enumerate(ias_preguntas.keys()):
    respuesta = ias_respuestas[pregunta]
    puntos = ias_preguntas[pregunta][opciones.index(respuesta)]
    
    if puntos >= 8:
        color = "🟢 Óptimo"
    elif 5 <= puntos < 8:
        color = "🟡 Moderado"
    else:
        color = "🔴 Bajo"

    ias_semaforo.append({
        "Grupo": list(ias_labels)[i],
        "Puntos": puntos,
        "Semáforo": color
    })

# DataFrame semáforo
df_semaforo = pd.DataFrame(ias_semaforo)

st.subheader("🚦 Semáforo Nutricional IAS")
st.dataframe(df_semaforo)

# Permitir descarga del semáforo
csv_semaforo = df_semaforo.to_csv(index=False).encode('utf-8')

st.download_button(
    label="📥 Descargar semáforo IAS (CSV)",
    data=csv_semaforo,
    file_name="ias_semaforo.csv",
    mime="text/csv"
)




st.subheader("🔍 Análisis de respuestas Edulcorantes")
st.dataframe(df_edulcorantes)

# ---------------------------------------
# Descargar como CSV interpretativo
# ---------------------------------------

csv_analisis = pd.concat([df_ias, df_edulcorantes], keys=['IAS', 'Edulcorantes']).to_csv(index=False).encode('utf-8')

st.download_button(
    label="📥 Descargar análisis interpretativo (CSV)",
    data=csv_analisis,
    file_name="analisis_respuestas_individual.csv",
    mime="text/csv"
)



import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# ------------------------------------
# Ejemplo: datos por grupo
# ------------------------------------
# Extrae puntos asignados por cada grupo
ias_puntos_por_pregunta = []

for pregunta, puntos in ias_preguntas.items():
    respuesta = ias_respuestas[pregunta]
    idx = opciones.index(respuesta)
    ias_puntos_por_pregunta.append(puntos[idx])

# Etiquetas resumidas
ias_labels = [
    "Cereales", "Verduras", "Frutas",
    "Lácteos", "Carnes", "Leguminosas",
    "Embutidos", "Postres", "Refrescos"
]

# ------------------------------------
# Crear gráfica de barras
# ------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
y_pos = np.arange(len(ias_labels))
ax.barh(y_pos, ias_puntos_por_pregunta, color='skyblue')
ax.set_yticks(y_pos)
ax.set_yticklabels(ias_labels)
ax.set_xlabel('Puntos asignados')
ax.set_title('Distribución de puntuación IAS por grupo')

st.pyplot(fig)

# ------------------------------------
# Guardar imagen para PDF (opcional)
# ------------------------------------
fig.savefig('ias_barras.png', bbox_inches='tight')


# ------------------------------------
# Datos por producto con edulcorante
# ------------------------------------
edulcorantes_puntos = []

for pregunta in edulcorantes_preguntas:
    respuesta = edulcorantes_respuestas[pregunta]
    idx = opciones_edulcorantes.index(respuesta)
    edulcorantes_puntos.append(puntos_edulcorantes[idx])

edulcorantes_labels = [
    "Sobres", "Bebidas light", "Yogurt light",
    "Gelatinas light", "Chicles sin azúcar",
    "Saborizantes", "Postres sin azúcar", "Cereales light"
]

# ------------------------------------
# Gráfica de barras
# ------------------------------------
fig2, ax2 = plt.subplots(figsize=(8, 5))
y_pos = np.arange(len(edulcorantes_labels))
ax2.barh(y_pos, edulcorantes_puntos, color='lightgreen')
ax2.set_yticks(y_pos)
ax2.set_yticklabels(edulcorantes_labels)
ax2.set_xlabel('Frecuencia (puntos)')
ax2.set_title('Frecuencia de consumo de edulcorantes')

st.pyplot(fig2)

# Guardar imagen para PDF (opcional)
fig2.savefig('edulcorantes_barras.png', bbox_inches='tight')


# Inserta gráfica IAS
try:
    pdf.image('ias_barras.png', w=180)  # Ajusta ancho a tu hoja A4
    pdf.ln(5)
except:
    pass  # Si no existe, no pasa nada

# Inserta gráfica Edulcorantes
try:
    pdf.image('edulcorantes_barras.png', w=180)
    pdf.ln(5)
except:
    pass



import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------
# Genera gráfico radar para IAS
# ------------------------------------------

# Puntos por grupo
ias_puntos_por_pregunta = []
for pregunta, puntos in ias_preguntas.items():
    respuesta = ias_respuestas[pregunta]
    idx = opciones.index(respuesta)
    ias_puntos_por_pregunta.append(puntos[idx])

# Etiquetas
ias_labels = [
    "Cereales", "Verduras", "Frutas",
    "Lácteos", "Carnes", "Leguminosas",
    "Embutidos", "Postres", "Refrescos"
]

# Puntos por grupo
ias_puntos_por_pregunta = []
for pregunta, puntos in ias_preguntas.items():
    respuesta = ias_respuestas[pregunta]
    idx = opciones.index(respuesta)
    ias_puntos_por_pregunta.append(puntos[idx])

# Etiquetas resumidas
ias_labels = [
    "Cereales", "Verduras", "Frutas",
    "Lácteos", "Carnes", "Leguminosas",
    "Embutidos", "Postres", "Refrescos"
]

# Radar: cerrar el círculo solo UNA VEZ
values = ias_puntos_por_pregunta + [ias_puntos_por_pregunta[0]]
num_vars = len(values)
angles = np.linspace(0, 2 * np.pi, num_vars)

# Plot
fig_radar, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='skyblue', alpha=0.4)
ax.plot(angles, values, color='blue', linewidth=2)

ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(ias_labels)
ax.set_title('Perfil de consumo IAS (Radar)', size=14)

st.pyplot(fig_radar)
fig_radar.savefig('ias_radar.png', bbox_inches='tight')




from fpdf import FPDF
from io import BytesIO
import datetime

#def generar_pdf(datos, ias_respuestas, edulcorantes_respuestas, ias_analisis, edulcorantes_analisis):
def generar_pdf(datos, ias_respuestas, edulcorantes_respuestas, ias_analisis, edulcorantes_analisis, df_semaforo):

    pdf = FPDF()
    pdf.add_page()

    # -------------------------------
    # Título y fecha
    # -------------------------------
    pdf.set_font("Helvetica", 'B', 16)
    pdf.cell(0, 10, "PROYECTO: Asociación del consumo de edulcorantes no calóricos", ln=True, align="C")
    pdf.ln(5)
    pdf.set_font("Helvetica", '', 12)
    pdf.cell(0, 10, f"Fecha de llenado: {datetime.date.today().strftime('%d/%m/%Y')}", ln=True, align="C")
    pdf.ln(10)

    # -------------------------------
    # Datos sociodemográficos y clínicos
    # -------------------------------
    pdf.set_font("Helvetica", 'B', 14)
    pdf.cell(0, 10, "Datos sociodemográficos y clínicos", ln=True)
    pdf.set_font("Helvetica", '', 11)

    for key, value in datos.items():
        if not key.startswith("IAS_") and not key.startswith("EDULCORANTES_") and not key.startswith("Puntuación"):
            pdf.set_font("Helvetica", 'B', 11)
            pdf.write(5, f"{key}: ")
            pdf.set_font("Helvetica", '', 11)
            pdf.write(5, f"{value}\n")
    pdf.ln(5)

    # -------------------------------
    # Respuestas IAS
    # -------------------------------
    pdf.set_font("Helvetica", 'B', 14)
    pdf.cell(0, 10, "Cuestionario: Índice de Alimentación Saludable (IAS)", ln=True)

    for pregunta, respuesta in ias_respuestas.items():
        pdf.set_font("Helvetica", 'B', 11)
        pdf.write(5, f"{pregunta}: ")
        pdf.set_font("Helvetica", '', 11)
        pdf.write(5, f"{respuesta}\n")

    pdf.ln(2)
    pdf.set_font("Helvetica", '', 11)
    pdf.cell(0, 10, f"Puntuación total IAS: {datos['Puntuación IAS']}", ln=True)
    pdf.ln(5)

    # ✅ Inserta gráfica IAS guardada
    try:
        pdf.image('ias_barras.png', w=120)
        pdf.ln(5)
    except Exception as e:
        print("No se pudo insertar IAS:", e)

    # ✅ Inserta radar IAS
    #try:
    #    pdf.image('ias_radar.png', w=120)
    #    pdf.ln(5)
    #except Exception as e:
    #    print("No se pudo insertar radar IAS:", e)

    # ✅ Inserta radar IAS centrado
    try:
        radar_w = 120  # ancho de la imagen en mm (ajusta según tu gráfica)
        page_width = pdf.w - 2 * pdf.l_margin  # ancho disponible menos márgenes

        #   Calcular posición X para centrar
        x_center = (page_width - radar_w) / 2 + pdf.l_margin

        pdf.image('ias_radar.png', x=x_center, w=radar_w)
        pdf.ln(5)
    except Exception as e:
        print("No se pudo insertar radar IAS:", e)


    
    # -------------------------------
    # Análisis interpretativo IAS
    # -------------------------------
    pdf.set_font("Helvetica", 'B', 13)
    pdf.cell(0, 10, "Análisis interpretativo IAS", ln=True)
    pdf.set_font("Helvetica", '', 10)
    for item in ias_analisis:
        pdf.set_font("Helvetica", 'B', 10)
        pdf.write(5, f"{item['Pregunta']}: ")
        pdf.set_font("Helvetica", '', 10)
        pdf.write(5, f"{item['Análisis']} Recomendación: {item['Recomendación']}\n")
    pdf.ln(5)

    # -------------------------------
    # 🚦 Semáforo Nutricional IAS
    # -------------------------------
    pdf.set_font("Helvetica", 'B', 13)
    pdf.cell(0, 10, "Semáforo Nutricional IAS", ln=True)
    pdf.set_font("Helvetica", '', 11)


    for index, row in df_semaforo.iterrows():
        grupo = row["Grupo"]
        puntos = row["Puntos"]

        # Desglosa color y nivel
        semaforo_parts = row["Semáforo"].split(" ")
        color = semaforo_parts[0].replace("🟢", "Verde").replace("🟡", "Amarillo").replace("🔴", "Rojo")
        nivel = semaforo_parts[1] if len(semaforo_parts) > 1 else ""

        pdf.write(5, f"{grupo}: {puntos} puntos | Color: {color} | Nivel: {nivel}\n")

    
    
    # -------------------------------
    # Respuestas Edulcorantes
    # -------------------------------
    pdf.set_font("Helvetica", 'B', 14)
    pdf.cell(0, 10, "Cuestionario: Frecuencia de Edulcorantes No Calóricos", ln=True)

    for pregunta, respuesta in edulcorantes_respuestas.items():
        pdf.set_font("Helvetica", 'B', 11)
        pdf.write(5, f"{pregunta}: ")
        pdf.set_font("Helvetica", '', 11)
        pdf.write(5, f"{respuesta}\n")

    pdf.ln(2)
    pdf.set_font("Helvetica", '', 11)
    pdf.cell(0, 10, f"Puntuación total Edulcorantes: {datos['Puntuación Edulcorantes']} de 24", ln=True)
    pdf.ln(5)

    # ✅ Inserta gráfica Edulcorantes guardada
    try:
        pdf.image('edulcorantes_barras.png', w=120)
        pdf.ln(5)
    except Exception as e:
        print("No se pudo insertar Edulcorantes:", e)

    # -------------------------------
    # Análisis interpretativo Edulcorantes
    # -------------------------------
    pdf.set_font("Helvetica", 'B', 13)
    pdf.cell(0, 10, "Análisis interpretativo Edulcorantes", ln=True)
    pdf.set_font("Helvetica", '', 10)
    for item in edulcorantes_analisis:
        pdf.set_font("Helvetica", 'B', 10)
        pdf.write(5, f"{item['Pregunta']}: ")
        pdf.set_font("Helvetica", '', 10)
        pdf.write(5, f"{item['Análisis']} Recomendación: {item['Recomendación']}\n")
    pdf.ln(10)

    # -------------------------------
    # Pie de página
    # -------------------------------
    pdf.set_font("Helvetica", 'I', 9)
    pdf.multi_cell(0, 6, "Este documento forma parte del proyecto de investigación.\n"
                         "Firma del responsable: ____________________________")

    # -------------------------------
    # Salida PDF en memoria
    # -------------------------------
    pdf_bytes = pdf.output(dest='S').encode('latin-1')
    buffer = BytesIO(pdf_bytes)
    return buffer


# ------------------------------------
# Llamada para generar y descargar PDF
# ------------------------------------
#pdf_file = generar_pdf(datos, ias_respuestas, edulcorantes_respuestas)

#st.download_button(
#    label="📄 Descargar ficha PDF de respuestas",
#    data=pdf_file,
#    file_name="respuestas_cuestionario.pdf",
#    mime="application/pdf"
#)




# 🚦 Genera PDF con análisis interpretativo incluido
#pdf_file = generar_pdf(datos, ias_respuestas, edulcorantes_respuestas, ias_analisis, edulcorantes_analisis)
pdf_file = generar_pdf(
    datos,
    ias_respuestas,
    edulcorantes_respuestas,
    ias_analisis,
    edulcorantes_analisis,
    df_semaforo  # 👈 Nuevo argumento
)



st.download_button(
    label="📄 Descargar ficha PDF con análisis",
    data=pdf_file,
    file_name="respuestas_cuestionario.pdf",
    mime="application/pdf"
)
