# código de geração do gráfico 

grafico_linha = sns.lineplot(data=df,x='dia', y='venda')
plt.title('PREÇO DIÁRIO DA GASOLINA')
plt.show(grafico_linha)