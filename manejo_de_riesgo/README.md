<h1>
  Manejo de Riesgo : Asignacion de Activos 
</h1>
<h3>Soporte y aporte personal sobre mi desarrolo en proyecto privado GE-Bots</h3>
En finanzas, la asignación de activos se refiere a la estrategia de distribuir inversiones en diversas clases de activos,
como acciones, bonos, bienes raíces y equivalentes de efectivo, con el objetivo de lograr un perfil específico de riesgo-recompensa
basado en los objetivos financieros de un individuo, su tolerancia al riesgo y su horizonte temporal. La justificación detrás de
la asignación de activos se fundamenta en la teoría moderna de carteras, que sugiere que la distribución de activos es un determinante significativo del rendimiento de la inversión.

Siguiendo el flujo de la implementación para el armado de cartera y reporte general :
![image](https://github.com/Pana-Onnti/manejo_de_riesgo/assets/97043308/329f8a23-999c-425e-b2ca-df8906020506)

<ul>
<li>1)Descargar datos de algun proveedor, en este caso de la folder [data_procesing] ; -> yfinance -> (class YFinanceDataFetcher)
. usando yfinance </li>
  
<li>2)Crear portfolio de algun tipo de folder [factory]; -> port_factory ->(class PortfolioOptimizer)
. usando riskfolio </li>
<li>3)Generar reporte, o generar algun tipo de analisis con capacidad de ser comunicado, ubicado en folder [analizer] ; -> port_analizer_qs ;-> generate_report(daily_returns):
. usando quantstats</li>
</ul>
Siguiendo esta lógica de modularización donde para cada subfunción; descargar,crear,reportar.
El objetivo de esto es la organización del código y tener mas separada las distintas funciones del código, para su mejor reutilización y refactorizacion .

En el main instanciamos las clases de los módulos y generamos el reporte.
El reporte visual a través de streamlit consume desde main y se encarga del mismo.

<h5>Se trata de seguir los principios clean code, SOLID como así también snake_case para funciones y variables como así también camelCase para las clases</h5>
