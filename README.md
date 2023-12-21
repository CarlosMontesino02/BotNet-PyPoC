# BotNet-PyPoC
Este proyecto es una idea que consiste en la creación de una arquitectura cliente-servidor hecha en python3  que acúta como una botnet.

# ¿Qué hace?

Tenemos dos cripts, uno para el cliente y otro para el servidor, el servidor simplemente abre un puerto y espera conexiones de los clientes, cuando un cliente se conecta, se notifica al servidor y como prueba este
manda un archivo de texto(esto se debe a que uno de los posibles usos es realizar fuerza bruta desde varios hosts, y sería posible enviar a cada host un trozo de la wordlist para que las procesen a la vez y en separado), tras
esto, se abre una shell reversa, en la que nuestro servidor puede escribir comandos que se ejecutarán en los diferentes clientes. Los comandos se muestran en la pantalla del cliente como demostración. Si queremos terminar la ejecución
ingresamos el comando "exit" para terminar la conexión con los clientes y después abortamos el programa del servidor con Ctrl+C.

# ¿Seguiré el proyecto?

Es posible que en mi tiempo libre siga el proyecto para que quede algo un poco más serio, pero esto lo he hecho simplemente por diversión/investigación, asi que no prometo nada.

# Uso

En el servidor se ejecuta: 
```sh python3 server.py ```
Y se indica un puerto elegido de forma arbitraria(obviamente que no esté en uso)

En el cliente se ejecuta:
Se debe EDITAR EL SCRIPT y establecer la variable HOST con la ip del dispositivo que está ejecutando el script server.py.

```sh python3 client.py ```
Y se especifica el mismo puerto que hemos usado antes.
