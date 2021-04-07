# Arrays

## Consigna

Escribir un programa en `C` y `Python` que:
- Cargue por consola un array de 10 elementos.

```
Ingrese el elemento 0: 123
Ingrese el elemento 1: 222
...
```

- Me permita elegir un elemento del array que quiera imprimir.

```
Ingrese un numero de elemento (0-9): 1
El elemento 1 es 222
```

- Encuentre, de todo el array, cual es el elemento mas chico y el mas grande junto con su posición en el array.

```
El elemento mas grande es el 12345 en la posición 7
El elemento mas chico es el -543 en la posición 2
```

## Como probar el codigo

### C

Corran en la terminal:

```
gcc -o arrays arrays.c
```

Para compilar y para ejecutar escriben:

```
arrays
```

### Python

Corran en la terminal:

```
python arrays.py
```

## Como entregar

Armen un `README.md` con lo siguiente:

```markdown
# Arrays

Alumno: Apellido y nombre
Curso: Curso
Materia: Representación Visual y Frontal de Datos
```

Pongan el `README.md` el `arrays.c` y `arrays.py` en una carpeta y corran en la terminal:

```
git init
git add README.md arrays.c arrays.py
git commit -m "Initial commit"
git checkout -b rvfd/2021/repaso/arrays
git push https://github.com/trq20/USERNAME.git rvfd/2021/repaso/arrays
```

Con `USERNAME` siendo el nombre de usuario de ustedes en GitHub.