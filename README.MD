<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=🗺️%20DarkMap&fontSize=60&fontAlignY=38&desc=Port%20Scanner%20%7C%20Ethical%20Hacking%20Tool&descAlignY=58&fontColor=ffffff&animation=fadeIn"/>

</div>

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=flat-square&logo=kalilinux&logoColor=white)
![Networking](https://img.shields.io/badge/Networking-TCP-blue?style=flat-square)
![Multithreading](https://img.shields.io/badge/Threads-100+-green?style=flat-square)
![Security](https://img.shields.io/badge/Cybersecurity-Ethical-red?style=flat-square)
![CLI](https://img.shields.io/badge/Interface-CLI-black?style=flat-square)
![Educativo](https://img.shields.io/badge/Uso-Solo_Educativo-orange?style=flat-square)

</div>

---

> ⚠️ **AVISO LEGAL:** DarkMap es una herramienta desarrollada **únicamente con fines educativos** y de aprendizaje en redes y ciberseguridad. **No escanees sistemas sin autorización explícita.** El uso indebido puede ser ilegal en tu país. El autor no se hace responsable del mal uso.

---

## 🧠 ¿Qué es DarkMap?

**DarkMap** es un **port scanner TCP** desarrollado en Python para Kali Linux que permite analizar qué puertos tiene abiertos una IP o dominio, utilizando **multithreading** para mayor velocidad. Similar a como funciona `nmap` a nivel básico, pero construido desde cero con Python puro.

Es ideal para:
- Aprender fundamentos de redes y sockets TCP/IP
- Practicar hacking ético en entornos de laboratorio
- Entender cómo funciona el escaneo de puertos internamente
- Laboratorios de ciberseguridad y CTFs

---

## ⚡ Características

| Feature | Descripción |
|---|---|
| 🔍 Escaneo TCP | Detecta puertos abiertos mediante conexión directa |
| ⚡ Multithreading | Usa `ThreadPoolExecutor` con 100+ hilos paralelos |
| 🌐 Soporte dominio | Convierte automáticamente dominios a IP con `socket.gethostbyname()` |
| 🖥️ CLI completo | Modo interactivo + flag `-i` para IP/dominio |
| 🎨 Interfaz visual | Banner ASCII, colores ANSI, resultados en tiempo real |
| ⏱️ Tiempo de escaneo | Muestra cuánto tardó el escaneo completo |
| 📋 Resumen final | Total de puertos abiertos encontrados |

---

## 🛠️ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/YeinerParraRincon/DarkMap.git

# Entrar al directorio
cd DarkMap

# No requiere dependencias externas — solo Python 3 estándar
python3 darkmap.py
```

> DarkMap usa únicamente librerías nativas de Python: `socket`, `threading`, `argparse`. No necesitas instalar nada.

---

## 🚀 Uso

### Modo interactivo
```bash
python3 darkmap.py
```

### Escanear una IP directamente
```bash
python3 darkmap.py -i 192.168.1.1
```

### Escanear un dominio
```bash
python3 darkmap.py -i google.com
```

### Escanear tu propia máquina (localhost)
```bash
python3 darkmap.py -i 127.0.0.1
```

### Ver ayuda
```bash
python3 darkmap.py --help
```

---

## 📋 Ejemplo de salida

```
  ██████╗  █████╗ ██████╗ ██╗  ██╗███╗   ███╗  █████╗ ██████╗
  ...

  [ DarkMap — Port Scanner | Ethical Hacking Tool ]
  by Yeiner Parra Rincón | WorldSkills 🥈 | SENA ADSO
  ⚠️  Solo para uso ético y autorizado.

[*] Host    : 192.168.1.1
[*] IP      : 192.168.1.1
[*] Puertos : 1 — 1024
[*] Hilos   : 100

[+] Puerto  22   ABIERTO   → SSH
[+] Puerto  80   ABIERTO   → HTTP
[+] Puerto  443  ABIERTO   → HTTPS

──────────────────────────────────────────
[*] Escaneo completado en 3.42s
[*] 3 puertos abiertos encontrados
```

---

## ⚙️ ¿Cómo funciona internamente?

DarkMap utiliza tres conceptos clave de Python:

**`socket`** — intenta abrir una conexión TCP al puerto objetivo. Si el servidor acepta la conexión, el puerto está abierto. Si rechaza o no responde, está cerrado o filtrado.

**`ThreadPoolExecutor`** — lanza hasta 100 hilos al mismo tiempo, cada uno revisando un puerto diferente. Sin hilos, escanear 1024 puertos de forma secuencial tomaría minutos. Con hilos paralelos tarda segundos.

**`argparse`** — permite pasar la IP directamente como argumento `-i` sin necesidad de interactuar con el menú.

---

## 📂 Estructura del proyecto

```
DarkMap/
├── darkmap.py    # Herramienta principal
└── README.md     # Este archivo
```

---

## 🔢 Puertos comunes detectados

| Puerto | Servicio |
|---|---|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 3306 | MySQL |
| 3389 | RDP |
| 8080 | HTTP alternativo |

---

## 🚀 Futuras mejoras

- [ ] 🔎 Detección de servicios por banner grabbing (HTTP, SSH, FTP)
- [ ] 📁 Exportar resultados a `.txt` o `.json`
- [ ] 🎯 Rangos de puertos personalizados (`-p 1-65535`)
- [ ] 📊 Mostrar tiempo por puerto
- [ ] 🔐 Detección de versión del servicio
- [ ] 🌐 Escaneo de múltiples IPs desde archivo

---

## 📌 Proyectos relacionados

- 👻 [DarkHash](https://github.com/YeinerParraRincon/DarkHash) — Hash Cracker educativo para Kali Linux
- 🔍 [DarkFinder](https://github.com/YeinerParraRincon/DarkFinder) — OSINT Username Finder

---

## 👤 Autor

**Yeiner Parra Rincón**
- 🏆 Subcampeón Nacional WorldSkills Colombia 2025
- 🎓 SENA — Tecnólogo ADSO
- 📍 La Dorada, Caldas, Colombia 🇨🇴

[![GitHub](https://img.shields.io/badge/GitHub-YeinerParraRincon-181717?style=flat-square&logo=github)](https://github.com/YeinerParraRincon)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-yeinerparrarincon-0077B5?style=flat-square&logo=linkedin)](https://linkedin.com/in/yeinerparrarincon)

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=100&section=footer&animation=fadeIn"/>
</div>