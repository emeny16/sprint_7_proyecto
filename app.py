import streamlit as st
import pandas as pd
import plotly.graph_objects as go

car_data = pd.read_csv('vehicles_us.csv')

# Grafico de dispersion
disp_button = st.button('Relación entre odómetro y precio')

if disp_button:

    st.write('Creación de un grafico de dispersión')

    fig_2 = go.Figure(
        data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

    fig_2.update_layout(
        title_text='Relación entre odómetro y precio de vehículos a la venta')

    st.plotly_chart(fig_2, use_container_width=True)

st.markdown('#### Relación entre odómetro y marca')

# casilla de verificación
ford = st.checkbox('Ford')
toyota = st.checkbox('Toyota')
chevrolet = st.checkbox('Chevrolet')

fig = go.Figure()

if ford:
    fig.add_trace(
        go.Histogram(
            x=car_data[car_data['model'].str.contains(
                'ford', case=False, na=False)]['odometer'],
            name='Ford',
            opacity=0.7
        )
    )

if toyota:
    fig.add_trace(
        go.Histogram(
            x=car_data[car_data['model'].str.contains(
                'toyota', case=False, na=False)]['odometer'],
            name='Toyota',
            opacity=0.7
        )
    )

if chevrolet:
    fig.add_trace(
        go.Histogram(
            x=car_data[car_data['model'].str.contains(
                'chevrolet', case=False, na=False)]['odometer'],
            name='Chevrolet',
            opacity=0.7
        )
    )

fig.update_layout(
    title='Comparación de odómetros',
    barmode='overlay'
)

st.plotly_chart(fig, use_container_width=True)


st.markdown('#### Popularidad de colores en vehículos')

# casilla de verificación 2
fig_3 = go.Figure()

colores = car_data['paint_color'].dropna().unique()

for color in colores:
    if st.checkbox(color):
        fig_3.add_trace(
            go.Histogram(
                x=car_data[
                    car_data['paint_color'] == color
                ]['odometer'],
                name=color,
                opacity=0.7
            )
        )

if len(fig_3.data) > 0:
    st.plotly_chart(fig_3, use_container_width=True)
