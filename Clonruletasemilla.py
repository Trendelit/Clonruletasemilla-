import streamlit as st import random

st.set_page_config(page_title="Clonador de Semilla - Simulador", layout="centered")

st.title("🔐 Simulador de Clonación de Semilla de Ruleta") st.markdown("Este simulador imita cómo un atacante podría intentar descubrir la semilla de una ruleta electrónica.")

Clase de RNG simple para simular una ruleta

class RNGSimulador: def init(self, semilla): self.random = random.Random(semilla)

def generar_numeros(self, cantidad=20):
    return [self.random.randint(0, 36) for _ in range(cantidad)]

entrada = st.text_input("Ingresá una secuencia de entre 3 y 7 números separados por espacio:", "2 25 33 30 31") rango_max = st.slider("Máximo de semillas a probar:", min_value=1000, max_value=500000, value=50000, step=1000)

if entrada: try: observados = list(map(int, entrada.strip().split()))

if not (3 <= len(observados) <= 7):
        st.warning("Ingresá entre 3 y 7 números para la simulación.")
    else:
        semilla_encontrada = None
        secuencia_simulada = []

        with st.spinner("Buscando coincidencia de semilla..."):
            for semilla in range(rango_max):
                sim = RNGSimulador(semilla)
                numeros = sim.generar_numeros(len(observados))
                if numeros == observados:
                    semilla_encontrada = semilla
                    secuencia_simulada = sim.generar_numeros(20)
                    break

        if semilla_encontrada is not None:
            st.success(f"¡Semilla encontrada!: {semilla_encontrada}")
            st.write("**Próximos 20 números simulados por el atacante:**")
            st.code(" ".join(map(str, secuencia_simulada)))
        else:
            st.error("No se encontró una semilla coincidente en el rango probado.")
except ValueError:
    st.error("Ingresá solo números válidos separados por espacios.")

