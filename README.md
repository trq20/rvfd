# Especificionaciones

Usando la libreria de `ST7789`, crear un programa que:

- Grafique un semicírculo, centrado en el display, de radio 90. Puede ser el semicírculo izquierdo o superior.
- A partir de una lectura del ADC, se debe graficar una aguja con una posicion proporcional al valor del ADC.

Luego, armar un `README.md` con lo siguiente:

```markdown
# Indicador - upython

Alumno: Apellido y nombre
Curso: Curso
Materia: Representación Visual y Frontal de Datos
```

## Consideraciones

- Tienen un `indicador.py` con una plantilla de código para empezar a trabajar.
- Van a necesitar las funciones `sin` y `cos` para poder obtener los valores para graficar la linea.
- Pueden importar `math` para poder usar `sin`, `cos` y `pi`.
- Las funciones `sin` y `cos` trabajan con radianes, no con grados.
- Tiene la función `pixel` para pintar un pixel. Sus argumentos son: `x`, `y`, `color`. Ejemplo:

```python
tft.pixel(120, 120, st7789.YELLOW)  # Pixel amarillo en el centro del display
```

- Recuerden que tiene el método `line` para graficar lineas. Sus argumentos son: `x0`, `y0`, `x1`, `y1`, `color`. Ejemplo: 

```python
tft.line(0, 0, 120, 120, st7789.YELLOW) # Linea amarilla con origen en el extremo 
                                        # superior izquierdo y fin en el centro
```

## Como entregar

Poner el `README.md` y el `indicador.py` en una carpeta, abran una terminal y escriban:

```
git init
git add README.md indicador.py
git commit -m "Initial commit"
git checkout -b rvfd/2021/upython/indicador
git push https://github.com/trq20/USERNAME.git rvfd/2021/upython/indicador
```

Recuerden cambiar `USERNAME` por su nombre de usuario en GitHub. Pueden verificar si la entrega se hizo visitando el repositorio en `https://github.com/trq20/USERNAME/tree/rvfd/2021/upython/indicador`.
