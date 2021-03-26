# Calculadora

## Especificaciones

- La interfaz gráfica debe constar de:
  - Un `textbox` para poder ingresar valores y mostrar el resultado final.
  - Botones para operar con `suma`, `resta`, `multiplicación` y `división`.
  - Botones con los números del `0` al `9` mas un `.` para escribir decimales. 
  - Un botón de `igual` para ejecutar las operaciones.
- La calculadora debe dejar introducir valores en un `textbox` solo a través de los botones y debe limpiarse después de elegir un operador.
- El resultado de la operación debe mostrarse solamente cuando se oprima el `igual`. 

## Orientación

- Consideren acumular todo lo que se ingrese en el `textbox` en un `string`.
- Recuerden el orden de operadores. Separen todo primero en términos por operadores `+` y `-` y luego dentro de cada uno resuelvan los `x` y `/`.
- Recuerden convertir los valores expresados como `string` en `float` o `int`. 
- El método `.Split()` puede resultarles útil. Ejemplo:

```c#
string phrase = "Este es un ejemplo de .Split().";
string[] words = phrase.Split(' ');

foreach (var word in words) {
    System.Console.WriteLine($"<{word}>");
}
```
Resultado:
```
<Este>
<es>
<un>
<ejemplo>
<de>
<.Split().>
```

## Como entregar

Creen un `README.md` con este contenido:

```markdown
# Calculadora

Alumno: Nombre y Apellido
Curso: Curso
Materia: Representación Visual y Frontal de Datos
```

Luego en la terminal corran:

```
git init
git add .
git commit -m "Initial commit"
git checkout -b rvfd/2021/c#/calculadora
git push https://github.com/trq20/USERNAME.git rvfd/2021/c#/calculadora
```
