# Watcher version para rasperry con pi cam

Esta versión del publicador de watcher hace uso de picam para tomar las fotos.

Estos nodos son los que se ejecutaran dentro de las raspberry pi

## Como compilar y ejecutar los nodos:

### Crear espacio de trabajo 

Crea una carpeta para hospedar el espacio de trabajo para estos nodos: 

````bash
mkdir -vp  ~/solar-brain/src
cd ~/solar-brain/src
# Clonar el espacio de trabajo a la carpeta src
git clone <repository_url> .
````

#### Instalar requerimientos de python

Hemos encontrado problemas a la hora de usar ros2 y ambientes virtuales de python, por lo que recomendamos realizar la instalación a nivel del python de usuario. 

```bash
pip install -r requirements.txt
```

#### Instalar redis

Es necesario contar con una  instancia de redis corriendo  en el entorno donde se ejecuten los nodos.

```
sudo apt install redis-server
```

Para ver si la instancia se encuentra corriendo ejecute:

```
redis-cli
> PING
```

Si la instancia se encuentra corriendo se recibirá un `PONG` en caso contrario ejecute:

```
redis-server
```

#### Compilar nodos

```baash
# Sourcea ros
source source /opt/ros/<ros_version>/setup.bash

colcon build --packages-select solar_interfaces
colcon build --symlink-install --packages-select solar_tools
colcon build --symlink-install --packages-select watcher
```

#### Ejecutar los nodos:

```
# Sourcea ros
ros2 run watcher watcher_pub
```

En otra terminal:

```
# Sourcea ros
ros2 run watcher server_img_delivery
```

## Arquitectura de la solución
![](/arquitectura.png)