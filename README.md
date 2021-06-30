## Especificaciones

- Elegir y configurar un pin analogico (cualquiera que tenga `ADC` en el pinout).
- Elegir y configurar un pin de salida de `PWM`.
- Hacer un programa que tome el valor del ADC y genere una salida de PWM con un duty cycle proporcional a la lectura. 

## Consideraciones

- Recuerden que el ADC tiene resolucion de 12 bits y el PWM es de 16 bits (4095 del ADC tiene que ser 100% de ciclo de actividad).
- El metodo `PWM.duty` trabaja en `us`.
- La frecuencia del PWM puede ser cualquiera que quieran.
- Pueden revisar la [documentacion de micropython](https://docs.micropython.org/en/latest/library/machine.html) para mas info.

## Pinout

![](esp32.png)

## Como subir

Poner el `main.py` en una carpeta, abrir una terminal y correr:

```
git init
git add main.py
git commit -m "Initial commit"
git checkout -b rvfd/2021/upython/ejemplo1
git push https://github.com/USERNAME.git rvfd/2021/upython/ejemplo1
```

Siendo `USERNAME` el nombre de usuario de ustedes.
