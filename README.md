# Pytse
**Pytse** (Tribunal Supremo de Elecciones) es un api wrapper para Python 3.7 (o versiones mas nuevas) que te permite interactuar con la pagina web **[Servicios electorales](https://servicioselectorales.tse.go.cr/chc/)** del Tribunal.

## Documentacion / Ayuda
Podes encontrar ayuda **[aca](https://pytsecr.readthedocs.io/)**
## Ejemplo:
```python
>>> from pytsecr import tseclient
>>> tse = tseclient()
>>> res = tse.consulta_nombres('Carlos','Alvarado', 'Quesada',limite=5) # 5 resultados, lista de datos basicos
>>> carlos =tse.consulta_cedula(res[1]['cedula']) # Objeto "pytsecr.Persona"
>>> print(f'{carlos.nombre_completo} tiene {carlos.edad_str}')
"Carlos Andres Alvarado Quesada tiene 42 aos"
>>> print(carlos.datos_raw)
{'fecha_de_nacimiento_str': '14/01/1980', 'fecha_de_nacimiento': datetime.date(1980, 1, 14), 'edad': 42, 'edad_str': '42 años', 'nombre': 'Carlos Andres', 'apellido': 'Alvarado', 'segundo_apellido': 'Quesada', 'nombre_completo': 'Carlos Andres Alvarado Quesada', 'cedula': '110600078', 'padres_rawdata': {'padre': {'nombre': 'Alejandro Alvarado Induni', 'cedula': '0'}, 'madre': {'nombre': 'Adelia Quesada Alvarado', 'cedula': '0'}}, 'cc': None, 'sexo': 'masculino', 'ha_muerto': False, 'marginal': False, 'empadronado': True, 'fallecio': False, 'lugar_de_nacimiento': 'URUCA CENTRAL SAN JOSE', 'nacionalidad': 'Costarricense', 'conocido_como': None}
```
## Instalar pytse (beta)

Pytse esta disponible en PyPi (o eso creo)

```console
python3 -m pip intall pytsecr
```

O incluirlo directamente en tu aplicacion:

```console
mkdir miapp
cd miapp
git clone https://github.com/pgbito/pytsecr . 
python3 example.py
```


