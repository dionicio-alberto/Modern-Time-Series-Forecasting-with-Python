import os
from pathlib import Path
import csv

data_download_message = """
These are the necessary files in the folder structure the code expects.
```
data
├── london_smart_meters
│   ├── hhblock_dataset
│   │   ├── hhblock_dataset
│   │       ├── block_0.csv
│   │       ├── block_1.csv
│   │       ├── ...
│   │       ├── block_109.csv
│── acorn_details.csv
├── informations_households.csv
├── uk_bank_holidays.csv
├── weather_daily_darksky.csv
├── weather_hourly_darksky.csv
```
"""

def check_downloaded_data():
    root = Path("data/london_smart_meters")
    assert root.exists(), f"no esta la carpeta london"

    chck_files = ['acorn_details.csv',
    'hhblock_dataset',
    'informations_households.csv',
    'uk_bank_holidays.csv',
    'weather_daily_darksky.csv',
    'weather_hourly_darksky.csv']

    dir_files = os.listdir(root)
    assert all([f in dir_files for f in chck_files]), f"no estan los archivos csv"
    hhblock_root = root/"hhblock_dataset"/"hhblock_dataset"
    assert hhblock_root.exists(), f"carpeta hhblock"
    assert all([(hhblock_root/f"block_{i}.csv").exists() for i in range(110)]), f"{data_download_message}"
    print("#"*25+" All data downloaded correctly! "+"#"*25)
    
def create_csv_files(directory, num_files):
    # Asegúrate de que el directorio exista o créalo si no existe
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Crear archivos block_0.csv hasta block_N.csv
    for i in range(num_files):
        filename = os.path.join(directory, f"block_{i}.csv")
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Puedes escribir datos en el archivo CSV si es necesario
            # Por ejemplo: writer.writerow(["Columna1", "Columna2", "Columna3"])
        print(f"Archivo {filename} creado.")

    print("Archivos creados exitosamente.")    

if __name__=="__main__":
    #root = Path("data/london_smart_meters")
    #archivos100 = root.joinpath('hhblock_dataset','hhblock_dataset')
    #num_files = 110
    #create_csv_files(archivos100, num_files)
    check_downloaded_data()