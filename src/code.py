#

import pandas as pd

df = pd.DataFrame([[1090, 464], [2328, 1062], [1456, 630]], 
                  columns=['chr11: 11347700-11367700', 'chr11: 40185800-40195800'], 
                  index=['8cell', 'epiblast', 'icm'])

df

# Таблица для дуплицирования

df = pd.DataFrame([['18.31%'], ['2.92%'], ['9.08%']], 
                  columns=['Процент дуплицированных чтений'], 
                  index=['8cell', 'epiblast', 'icm'])

df

# Построение гистограмм

import matplotlib.pyplot as plt

df_6473 = pd.read_csv("s_SRR5836473_1_bismark_bt2_pe.deduplicated.bedGraph", delimiter='\t', skiprows=1, header=None)
df_4222 = pd.read_csv("s_SRR3824222_1_bismark_bt2_pe.deduplicated.bedGraph", delimiter='\t', skiprows=1, header=None)
df_6475 = pd.read_csv("s_SRR5836475_1_bismark_bt2_pe.deduplicated.bedGraph", delimiter='\t', skiprows=1, header=None)

plt.title('8 cell')
df_6473[3].hist(bins=100)
plt.legend()

plt.title('epiblast')
df_4222[3].hist(bins=100)
plt.legend()

plt.title('icm')
df_6475[3].hist(bins=100)
plt.legend