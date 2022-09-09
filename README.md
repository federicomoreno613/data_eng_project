# data_eng_project

Para instalar el mismo enviroment (Dado que no estamos usando docker que soluciona todo este quilombo)

pip install -r requirements.txt (en la carpeta donde esta el txt)

Tener en cuenta que tengo python 3.8 por tema de versionado.

Crear un docker que instalar requirements.txt y correr el script

Ejemplo de Dockefile

hacer markdown de python code

```python
FROM python:3.8
WORKDIR /automatization
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```