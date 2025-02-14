import os
from pathlib import Path


list_of_files = [
    "QAWithPDF/__init__.py",
    "QAWithPDF/data_ingestion.py",
    "QAWithPDF/embedding.py",
    "QAWithPDF/model_api.py",
    "Experiments/experiment.ipynb",
    "StreamlitApp.py",
    "logger.py",
    "exception.py",
    "setup.py"
]

for filePath in list_of_files:
    filePath = Path(filePath)
    filedir , filename = os.path.split(filePath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
       


    if(not os.path.exists(filePath)) or (os.path.getsize(filePath) == 0):
        with open(filePath, 'w') as f:
            pass
       

   