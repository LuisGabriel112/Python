import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivo_problemas_graficos\\pedos.csv")

#creando el grafico

sns.lineplot(x="fecha",y="pedos",data=df)

#marcando el highlight

plt.plot('01-05',45,'o')

#mostrando el grafico

plt.show()


