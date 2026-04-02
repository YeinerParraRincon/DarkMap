<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=🗺️%20DarkMap&fontSize=60&fontAlignY=38&desc=Port%20Scanner%20%7C%20Ethical%20Hacking%20Tool&descAlignY=58&fontColor=ffffff&animation=fadeIn"/>

</div>

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Networking](https://img.shields.io/badge/Networking-TCP-blue?style=flat-square)
![Multithreading](https://img.shields.io/badge/Threads-100+-green?style=flat-square)
![Security](https://img.shields.io/badge/Cybersecurity-Ethical-red?style=flat-square)
![CLI](https://img.shields.io/badge/Interface-CLI-black?style=flat-square)

</div>

---

> ⚠️ **AVISO LEGAL:** DarkMap es una herramienta desarrollada **únicamente con fines educativos**. No escanees sistemas sin autorización. El mal uso puede ser ilegal.

---

## 🧠 ¿Qué es DarkMap?

**DarkMap** es un **port scanner TCP** desarrollado en Python que permite analizar puertos abiertos en una IP o dominio utilizando **multithreading** para mayor velocidad.

Es ideal para:

- Aprender fundamentos de redes y sockets  
- Practicar hacking ético  
- Entender escaneo de puertos  
- Laboratorios de ciberseguridad  

---

## ⚡ Características

| Feature | Descripción |
|---|---|
| 🔍 Escaneo TCP | Detecta puertos abiertos |
| ⚡ Multithreading | Usa `ThreadPoolExecutor` |
| 🌐 Soporte dominio | Convierte dominios a IP |
| 🖥️ CLI simple | Uso con `-i` |
| 🎨 Banner personalizado | Estilo hacking |

---

## 🛠️ Instalación

```bash
git clone https://github.com/tuusuario/DarkMap.git
cd DarkMap
python3 darkmap.py -i 127.0.0.1

🚀 Uso
Escanear IP
python darkmap.py -i 192.168.1.1
Escanear dominio
python darkmap.py -i google.com
📋 Ejemplo de salida
  ██████╗  █████╗ ██████╗ ██╗  ██╗███╗   ███╗ ...

  [ DarkMap — Port Scanner ]

[+] Puerto 22 ABIERTO
[+] Puerto 80 ABIERTO
[+] Puerto 443 ABIERTO
⚙️ Funcionamiento

DarkMap utiliza:

socket → conexión TCP
ThreadPoolExecutor → ejecución paralela
argparse → argumentos CLI

Cada puerto se escanea en paralelo, lo que hace el proceso mucho más rápido.

📂 Estructura del proyecto
DarkMap/
├── darkmap.py
└── README.md
🚀 Futuras mejoras
🔎 Detección de servicios (HTTP, SSH, FTP)
📁 Exportar resultados
🎯 Rangos personalizados (-p 1-1000)
📊 Tiempo de escaneo
🧠 Banner grabbing
👤 Autor

Yeiner Parra Rincón
🎓 SENA — ADSO
🇨🇴 Colombia

<div align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=100&section=footer&animation=fadeIn"/> </div> ```