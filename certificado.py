#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Generador de certificados pdf usando una plantilla svg a través de inkscape
# Copyright 2016 David Hernández

# certificado.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# certificado.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with certificado.py. If not, see <http://www.gnu.org/licenses/>.

import csv
import time
import sys
import traceback
import pdfmerge
from subprocess import Popen

def generar(reemplazos,rol,nombre,contador):
    """Genera el certificado en formato pdf."""
    certsalida = "{0}-{1}".format(nombre,rol)                         #Nombre del certificado pdf final
    nombresvg = "svg_{0}.svg".format(certsalida)            #Nombre único temporal del svg modificado
    nombrepdf = "pdf_{0}.pdf".format(certsalida)            #Nombre único temporal del svg modificado

    with open('plantilla.svg', 'r') as entrada, open(nombresvg, 'w') as salida:
        for line in entrada:                            #Reemplazo de variables en el archivo svg
            for src, target in reemplazos:
                line = line.replace(src, target)
            salida.write(line)
    entrada.close()
    salida.close()

    print("{0} Generando certificado de {1} ({2})".format(contador, nombre, rol))
    x = Popen(['/usr/bin/inkscape', nombresvg, '-A', nombrepdf])  #Generación del certificado temporal.

def main():
    """Recolecta los datos y los envía a la función de generación."""
    try:
        contador = 0
        with open('participantes.csv', 'r') as listado: #Lectura de participantes
            datos = csv.reader(listado, delimiter=';')
            for row in datos:
                if row[0].startswith('#'):              #Permite comentar líneas en el archivo csv
                    continue
                nombre = row[0]                         #Columna 1 corresponden a Nombre y Apellido
                rol = row[1]                            #Columna 2 corresponde a la cédula
                reemplazos = (('Nombre_Participante',nombre), ('Rol_Participante',rol))
                contador = contador + 1                 #Contador que se agrega al nombre temporal del svg
                generar(reemplazos,rol,nombre,contador)  #Función de generación de certificados
        listado.close()
        print("\nTotal de certificados generados: {0}".format(contador))
    except KeyboardInterrupt:
        print("Interrupción por teclado.")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main()
