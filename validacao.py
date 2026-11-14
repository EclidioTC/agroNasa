import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carrega os dados da NASA
df = pd.read_csv('POWER_Point_Daily_20230101_20261113_026d03S_032d35E_LST.csv', skiprows=10)
df.replace(-999.0, np.nan, inplace=True)

# Cria uma coluna de data simulada baseada no Ano e DOY (Dia do Ano)
df['Data'] = pd.to_datetime(df['YEAR'].astype(str) + '-' + df['DOY'].astype(str), format='%Y-%j')

# Configura o gráfico de validação para o júri
plt.figure(figsize=(10, 5))
plt.plot(df['Data'], df['PRECTOTCORR'], label='Precipitação (mm/dia)', color='blue', alpha=0.6)
plt.axhline(y=8.0, color='red', linestyle='--', label='Limite de Alerta de Cheia')

plt.title('Validação do Modelo com Dados da NASA (Maputo 2023-2026)')
plt.xlabel('Data')
plt.ylabel('Precipitação (mm/dia)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Guarda o gráfico para usar no relatório/apresentação
plt.savefig('validacao_nasa.png')
print("Gráfico de validação gerado com sucesso!")