import pandas as pd

# ======= CARGA DE ARCHIVOS =======
df_athletes = pd.read_csv('./datos/olympic_athletes.csv')
df_hosts = pd.read_csv('./datos/olympic_hosts.csv')
df_medals = pd.read_csv('./datos/olympic_medals.csv')
df_results = pd.read_csv('./datos/olympic_results.csv')

# ======= ANALISIS DE DATOS =======
def spacer():
    print("\n\n")
    print("===============================================")
    print("\n\n")


# Hacemos una función para mostrar información básica de cada DataFrame
def analizar_dataset(df, nombre):
    print(f"====== Dataset: {nombre} ======")
    print("Primeras rows:")
    display(df.head())

    spacer()

    print(f"\nInformación básica del DataFrame: {nombre}")
    df.info()

    spacer()

    print("\nDescripción estadística:")
    display(df.describe(include='all'))

    spacer()

    print("\nValores nulos por columna:")
    display(df.isnull().sum())

    spacer()

    print("\nRegistros duplicados:")
    display(df.duplicated().sum())

    spacer()

    print("\nColumnas:")
    for col in df.columns:
        print(col)

    spacer()


# Ejecutamos la función por cada uno de los datasets
analizar_dataset(df_athletes, 'Atletas')
analizar_dataset(df_hosts, 'Hosts')
analizar_dataset(df_medals, 'Medallas')
analizar_dataset(df_results, 'Resultados')

# ======= MERGEO DE DATOS =======

# Merge de los DataFrames usando la columna 'athlete_url'
df_athletes_medals = pd.merge(df_medals, df_athletes, on='athlete_url', how='left')
# Eliminamos columnas repetidas
df_athletes_medals.drop(columns=['athlete_full_name_y'], inplace=True)
df_athletes_medals.rename(columns={'athlete_full_name_x': 'athlete_full_name'}, inplace=True)
df_athletes_medals.head()

# ======= LIMPIEZA DE DATOS =======

# Función para limpiar datos
def limpiar_datos(df):
    # Eliminamos filas con valores nulos
    df.dropna(inplace=True)
    # Llenamos valores nulos con 0 (o cualquier otro valor)
    df.fillna(0, inplace=True)

    return df

# Limpiamos todos los Dataframes y los guardamos en unos nuevos
df_athletes_medals_clean = limpiar_datos(df_athletes_medals)
df_hosts_clean = limpiar_datos(df_hosts)
df_results_clean = limpiar_datos(df_results)

# Guardamos los DataFrames limpios en otra carpeta
df_athletes_medals_clean.to_csv('./datos_clean/olympic_athletes_medals.csv', index=False)
df_hosts_clean.to_csv('./datos_clean/olympic_hosts.csv', index=False)
df_results_clean.to_csv('./datos_clean/olympic_results.csv', index=False)


