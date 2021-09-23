## Datos

### Cosntantes del programa 

- Telegram chat id: `1000113940`
- Puerto para el socket: `8080`
- Tamaño del header del socket: `16` bytes.
- IP del servidor: consultar en el momento.
- Red para conectar el ESP-32: consultar en el momento.
- Token del bot de Telegram: `from credentials import token` 

### Conexiones

- ST7789
  - `SCK`: GPIO 18
  - `MOSI/SDA`: GPIO 19
  - `RESET`: GPIO 23
  - `DC`: GPIO 22

- ADC
  - `POT1`: GPIO 36
  - `POT2`: GPIO 39

## Documentacion

### Micropython

- Micropython para [ESP32](https://docs.micropython.org/en/latest/esp32/quickref.html)
- Micropython [socket](https://docs.micropython.org/en/latest/library/socket.html)
- Micropython [network](https://docs.micropython.org/en/latest/library/network.html)
- Micropython [machine](https://docs.micropython.org/en/latest/library/machine.html)
- Repo de Micropython en [GitHub](https://github.com/micropython/micropython)

### APIs

- Python [requests](https://realpython.com/python-requests/) (`urequests` en Micropython)
- Python [json](https://www.w3schools.com/python/python_json.asp)
- API de [Telegram](https://core.telegram.org/bots/api)
- API de [Pokemon](https://pokeapi.co/docs/v2)

## Socket

El servidor debe recibir un `id` entre 1 y 898 y posteriormente envia los datos. Previo a cada paquete, envia uno de 16 bytes conteniendo el largo del paquete siguiente. 

El primer paquete con informacion relevante, es un `json` como este:

```json
{
  "id" : 365,
  "name" : "Walrein",
  "types" : ["ice", "water"],
  "sprite_url" : "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/365.png",
  "width" : 96,
  "height" : 96
}
```

Donde `width` y `height` son el ancho y altura en pixeles. Posterior a eso, el servidor manda las filas de pixeles de esta manera:

```
{
  "row" : [
    ..., 
    (90, 139, 197), 
    (57, 115, 172), 
    (57, 115, 172),  
    ...
  ]
}
```

Donde cada elemento de la lista es una tupla de valores rgb. El servidor va a enviar paquetes de una fila a la vez (paquete con el largo primero y paquete de fila luego).
