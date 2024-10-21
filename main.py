import numpy as np
import matplotlib.pyplot as plt
from datetime import date
from datetime import timedelta
import streamlit as st
from streamlit_timeline import st_timeline

st.set_page_config(layout="wide")


labels = [
    "Propuesta. \nProyecto de Fortalecimiento\n Familiar Empresarial",
    "Arranca el proyecto\n con CEDEM",
    "Retiro Estratégico\n presencial",
    "Retiro Estratégico\n presencial", #
    "Retiro Estratégico\n presencial",###
    "Reunió virtual\n Familia Mini",
    "Family Healing. \nGonzalo Zubieta",
    "Retiro Estratégico\n presencial",##
    "DECV \nGrupo Apolo",
    "Reunión de\n seguimiento\n Familia Mini",
    "Consejo Estratégico\n Grupo Apolo",
    "DECV\n GEA Capital",
]

items3 =[
    {"id": 1, "content": "Propuesta. Proyecto de Fortalecimiento Familiar Empresarial", "start": str(date(2023, 4, 25).ctime()), "actividades": ["Objetivo General: Acompañar a los hermanos Ayleen, Jorge y Juan Mini en la revisión de su sistema de gobierno como grupo familiar, para asegurar que continue por sus mejores caminos de armonía y crecimiento de valor.", 
    "Objetivos específicos:", " - Dialogar con los hermanos Mini, su mamá y ejecutivos clave para conocer su visión de crecimiento, sus retos y oportunidades y sus inquietudes como grupo familiar.",
    " - Efectuar un diagnóstico de cómo se está manejando hoy, y cómo puede mejorarse, la Dueñez Compartida y la Gestión del Valor.",
    " - Apoyarlos en la actualización de sus remuneraciones como gestores familiares",
    " - Acompañarlos en la definición de posibles ajustes a su sistema de gobierno, construyendo caminos de gobernabilidad cara a la incorporación de la tercera generación"
    ]},
    {"id": 2, "content": "Arranca el proyecto con CEDEM", "start": str(date(2023,8,16).ctime()), "actividades": [""]},
    {"id": 3, "content": "Retiro Estratégico presencial", "start": str(date(2023,11,6).ctime()), "actividades": [
        "Proyecto Family Healing. Buscar al asesor ideal para el healing",
        "Consejo Estratégico Grupo Apolo. Identificar lista de posibles candidatos",
        "Los hermanos están de acuerdo en compartir la Creación de Valor con socios y colaboradores",
        "Completar la estructura de Directores en Apolo. Buscar gente estrella",
        "Divisón Markets en GEA se convierte en proyecto de venture"
    ]},
    {"id": 4, "content": "Retiro Estratégico presencial", "start": str(date(2024,1,15).ctime()), "actividades": [
        "Arrancan con el Proecto de Internacionalización. Jorge verá el terreno Miami",
        "Surjen discrepancias respecto a la forma de Gobierno de la holding (% para cambios, dividendos, condiciones para entrar a la empresa y puestos)",
        "Cambio en la estructura y tiempos de las reuniones del Consejo de administración (junta directiva) y directores"
    ]},
    {"id": 5, "content": "Retiro Estratégico presencial", "start": str(date(2024,2,21).ctime()), "actividades": [
        "GEA Capital. Buscar empresas para crecerlas y vender. Buscar oportunidades en banking (idea de banca digital)",
        "Proyecto de fortalecimiento de Auditoría",
        "CEDEM. Preocupa el tema de alta de foco en ambos grupos",
        "Objetivo del Consejo Estratégico de Apolo - Internacionalización"
    ]},
    {"id": 6, "content": "Reunió virtual con la familia Mini", "start": str(date(2024,3,20).ctime()), "actividades": [
        "GEA Capita. Se acepta Visión  Estratégica de buscar una empresa grande donde gobierne la familia",
        "Se toma decisión de buscar salir de top bikes cuanto antes",
        "Family Healing. Se toma decisión de avanzar con Gonzalo Zubieta"
    ]},
    {"id": 7, "content": "Family Healing. Gonzalo Zubieta", "start": str(date(2024,5,9).ctime()), "actividades": [
        "Sesión Familia Mini con Gonzalo Zubieta"
    ]},
    {"id": 8, "content": "Retiro Estratégico presencial", "start": str(date(2024,5,15).ctime()), "actividades": [
        "Se mostró una dinámica diferente (efecto de la sesión con Gonzalo Zubieta)",
        "GEA Capita. Saavy le empieza a ir bien, se podría vender a finales 2024",
        "Oferta de compra para Top Bikes (Klos y competencia en el Salvador). Se retira Mauricio Grajeda de la empresa",
        "Sesión de Onboarding del Consejo Estratégico de Grupo Apolo. Definición de estructura"
    ]},
    {"id": 9, "content": "DECV Grupo Apolo", "start": str(date(2024,6,26).ctime()), "actividades": [
        "Directivos agobiados, se agregará estructura para liberar a algunos directores",
        "Poblema de enfoque en Grupo Apolo",
    ]},
    {"id": 10, "content": "Reunión de seguimiento con los hermanos.", "start": str(date(2024,7,18).ctime()), "actividades": [
        "Family Healing", "Conclusiones del DECV de Grupo Apolo", "programación del DECV de GEA Capital"
    ]},
    {"id": 11, "content": "Consejo Estratégico de Grupo Apolo.", "start": str(date(2024,8,20).ctime()), "actividades": [
        "Primera Sesión"
    ]},
    {"id": 12, "content": "DECV GEA Capital", "start": str(date(2024,8,22).ctime()), "actividades": [
        ""
    ]},
]

# Step 2
dates2 = [date(2023, 4, 25), date(2023,8,16), date(2023,11,6), date(2024,1,15), 
         date(2024,2,21), date(2024,3,20), date(2024,5,9), date(2024,5,15), date(2024,6,26), date(2024,7,18), date(2024,8,20), date(2024,8,22)]

dates = [date(2023, 4, 25), date(2023,8,16), date(2023,11,6), date(2024,1,15), 
         date(2024,2,21), date(2024,3,20), date(2024,5,9), date(2024,5,15), date(2024,6,26), date(2024,7,18), date(2024,8,20), date(2024,8,22)]

min_date = date(np.min(dates).year, np.min(dates).month -1 , np.min(dates).day)
max_date = date(np.max(dates).year, np.max(dates).month +3, np.max(dates).day - 20)
 
# labels with associated dates
labels = ['{0:%d %b %Y}:\n{1}'.format(d, l) for l, d in zip (labels, dates)]


# Step 3
fig, ax = plt.subplots(figsize=(15, 4), constrained_layout=True)
_ = ax.set_ylim(-2, 1.75)
_ = ax.set_xlim(min_date, max_date)
_ = ax.axhline(0, xmin=0.05, xmax=0.95, c='deeppink', zorder=1)
_ = ax.autoscale_view()
 
_ = ax.scatter(dates, np.zeros(len(dates)), s=120, c='palevioletred', zorder=2)
_ = ax.scatter(dates, np.zeros(len(dates)), s=30, c='darkmagenta', zorder=3)

# Step 4
label_offsets = np.zeros(len(dates))
label_offsets[::2] = 0.35
label_offsets[1::2] = -0.7
for i, (l, d) in enumerate(zip(labels, dates)):
    _ = ax.text(d, label_offsets[i], l, ha='center', fontfamily='serif', fontweight='bold', color='royalblue',fontsize=8)

# Step 5
stems = np.zeros(len(dates))
stems[::2] = 0.3
stems[1::2] = -0.3   
markerline, stemline, baseline = ax.stem(dates, stems) #, use_line_collection=True
_ = plt.setp(markerline, marker=',', color='darkmagenta')
_ = plt.setp(stemline, color='darkmagenta')

# Step 6
# hide lines around chart
for spine in ["left", "top", "right", "bottom"]:
    _ = ax.spines[spine].set_visible(False)
 
# hide tick labels
_ = ax.set_xticks([])
_ = ax.set_yticks([])
 
_ = ax.set_title('Grupo Mini', fontweight="bold", fontfamily='serif', fontsize=16, 
                 color='royalblue')



st.write(fig)

timeline = st_timeline(items3, groups=[], options={}, height="300px")

if timeline:
    st.subheader(timeline["content"])
    st.write(timeline["start"])

    for i in timeline["actividades"]:
        st.write(i)