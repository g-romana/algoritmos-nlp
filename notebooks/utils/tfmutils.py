import datetime
import shutil
import os 



def guardar_modelo(modelo='best_model_state.bin', ruta_guardado='../resultados/modelos/'):
    """
    Guarda el modelo en la ruta especificada.

    Args:
        modelo: modelo a guardar.
        ruta_guardado: ruta donde se guardará el modelo.
    """
    # Crear la carpeta si no existe
    carpeta_guardado = os.path.dirname(ruta_guardado)
    if not os.path.exists(carpeta_guardado):
        os.makedirs(carpeta_guardado)

    # Generar el nombre del archivo con la fecha y hora actual
    fecha_actual = datetime.datetime.now().strftime(r"%Y-%m-%d_%H-%M-%S")
    nombre_archivo = f"{fecha_actual}_bert_model_state_amazon_reviews_es.bin"

    
    # Unir la ruta de la carpeta con el nombre del archivo
    ruta_archivo = os.path.join(ruta_guardado, nombre_archivo)
    shutil.move(modelo, ruta_archivo)
    print(f"modelo {modelo}\n guardado en {ruta_archivo}")

def guardar_metadata(BATCH_SIZE, EPOCHS, LEARNING_RATE, PRE_TRAINED_MODEL_NAME, tipo, idioma, train_acc, val_acc, fin):
    ruta_guardado = os.path.basename('../resultados/notas/')
    metadata = {
        "BATCH_SIZE": [BATCH_SIZE],
        "EPOCHS": [EPOCHS],
        "LEARNING_RATE": [LEARNING_RATE],
        "PRE_TRAINED_MODEL_NAME": [PRE_TRAINED_MODEL_NAME],
        "tipo": [tipo],
        "idioma": [idioma],
        "train_acc": [train_acc],
        "val_acc": [val_acc],
        "tiempo_seg":[fin],
    }
    df = pd.DataFrame(metadata)
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = f"{fecha_actual}_metadata.csv"
    ruta_archivo = os.path.join(ruta_guardado, nombre_archivo)
    df.to_csv(ruta_archivo, index=False)
    print(f"csv {nombre_archivo}\n guardado en {ruta_archivo}")