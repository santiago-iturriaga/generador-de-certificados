# generador-de-certificados
Generador en masa de certificados en pdf

----

## Requerimientos:
Para el funcionamiento del script debe tener instalado:
* inkscape

## Instrucciones
#### Plantilla svg
`plantilla.svg` es la plantilla del certificado, ella contiene las siguientes variables que no deben ser modificadas en el svg:

* `Nombre_Participante`
* `Rol_Participante`

#### Lista de participantes
`participantes.csv` es un archivo de texto plano que contiene la tabla de participantes y sus datos separados por punto y coma (;). El formato es el siguiente:

```
Fulano de Tal;Organizador
Zutano de Tal;Autor
#comentarios inician con numeral
Mengano de Tal;Chair
```
Donde, la primera columna va el(los) nombre(s) y apellido(s) y en la segunda su rol.

