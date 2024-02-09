"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    #
    # Inserte su código aquí
    #
    df_buffer = {"cluster": [],
         "cantidad_de_palabras_clave": [],
         "porcentaje_de_palabras_clave": [],
         "principales_palabras_clave": []
        }

    with open("clusters_report.txt", "r") as file:
        no_title_file = file.readlines()[4:]

        main_keywords = str()
        for line in no_title_file:
            cluster_num = line[3:5].strip()
            keyword_num = line[9:12].strip()
            keyword_pct = line[25:31].strip().rstrip(" %").replace(",", ".")
            main_keywords += line[41:]

            if cluster_num.isdigit():
                df_buffer["cluster"].append(int(cluster_num))

            if keyword_num.isdigit():
                df_buffer["cantidad_de_palabras_clave"].append(int(keyword_num))

            if keyword_pct.replace(".","").isdigit():
                df_buffer["porcentaje_de_palabras_clave"].append(float(keyword_pct))

            if line.strip().endswith(".") or line.strip().endswith("control"):  # Las palabras clave terminan en este caso en "." o en "control"

                main_keywords = main_keywords.replace(".", "")
                main_keywords = main_keywords.replace("\n", " ")

                for i in range(5, 1, -1):                                                         # Los espacios más grandes son de 5.
                    main_keywords = main_keywords.replace(" " * i, " ")

                df_buffer["principales_palabras_clave"].append(main_keywords.strip())
                main_keywords = str()

    df = pd.DataFrame(df_buffer)

    return df

# print(ingest_data())

