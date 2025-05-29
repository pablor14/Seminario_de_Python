import pandas as pd
import matplotlib.pyplot as plt

# 1) Ajuste o nome do arquivo, caso não seja 'data.txt'
df = pd.read_csv(
    'historiador.txt',
    delim_whitespace=True,
    comment=';',
    header=0,
    names=['HREF', 'HCALCULADA', 'QOUT', 'QIN']
)

# 2) Eixo de tempo (passo de 0,05 s)
time = df.index * 0.05

# 3) Cria figura com 3 subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

# Subplot 1: Referência (HREF) e Dinâmica (HCALCULADA)
ax1.plot(time, df['HREF'], label='HREF (Referência)')
ax1.plot(time, df['HCALCULADA'], label='h (Dinâmica)')
ax1.set_ylabel('H')
ax1.set_title('Referência vs Dinâmica do Sistema')
ax1.legend()

# Subplot 2: QOUT
ax2.plot(time, df['QOUT'])
ax2.set_ylabel('QOUT')
ax2.set_title('QOUT vs Tempo')

# Subplot 3: QIN
ax3.plot(time, df['QIN'])
ax3.set_ylabel('QIN')
ax3.set_xlabel('Tempo (s)')
ax3.set_title('QIN vs Tempo')

plt.tight_layout()
plt.show()
