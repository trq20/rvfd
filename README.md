# Especificionaciones

Usando la libreria de `ST7789`, crear un programa que:

- Grafique un círculo, centrado en el display, de radio 90.
- Cada un segundo grafique una linea con origen en el centro del display y longitud igual al radio.
- En 60 segundos, la linea debe recorrer una vuelta completa.
- La linea debe arrancar formando un angulo de 90 grados con el eje x.

Luego, armar un `README.md` con lo siguiente:

```markdown
# Reloj - upython

Alumno: Apellido y nombre
Curso: Curso
Materia: Representación Visual y Frontal de Datos
```

## Consideraciones

- Tienen un `reloj.py` con una plantilla de código para empezar a trabajar.
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

Poner el `README.md` y el `reloj.py` en una carpeta, abran una terminal y escriban:

```
git init
git add README.md reloj.py
git commit -m "Initial commit"
git checkout -b rvfd/2021/upython/reloj
git push https://github.com/trq20/USERNAME.git rvfd/2021/upython/reloj
```

Recuerden cambiar `USERNAME` por su nombre de usuario en GitHub. Pueden verificar si la entrega se hizo visitando el repositorio en `https://github.com/trq20/USERNAME/tree/rvfd/2021/upython/reloj`.
