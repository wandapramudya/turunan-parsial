import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.set_page_config(layout="wide")
st.title("Visualisasi Fungsi Biaya Produksi")
st.markdown("### Fungsi: C(x, y) = 0.5x² + 0.8y² + 0.6xy + 3x + 2y + 10")

# Definisi fungsi biaya
def C(x, y):
    return 0.5 * x**2 + 0.8 * y**2 + 0.6 * x * y + 3 * x + 2 * y + 10

# Slider input dari user
col1, col2 = st.columns(2)

with col1:
    x_min = st.slider("Nilai minimum x (keripik singkong)", 0, 20, 0)
    x_max = st.slider("Nilai maksimum x", x_min + 1, 30, 10)
    
with col2:
    y_min = st.slider("Nilai minimum y (keripik kentang)", 0, 20, 0)
    y_max = st.slider("Nilai maksimum y", y_min + 1, 30, 10)

# Buat grid dan evaluasi fungsi
x = np.linspace(x_min, x_max, 100)
y = np.linspace(y_min, y_max, 100)
X, Y = np.meshgrid(x, y)
Z = C(X, Y)

# Plot 3D
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
ax.set_title('Grafik 3D Fungsi Biaya Produksi')
ax.set_xlabel('Keripik Singkong (x) [100 kg]')
ax.set_ylabel('Keripik Kentang (y) [100 kg]')
ax.set_zlabel('Biaya (juta rupiah)')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

st.pyplot(fig)
