# 🛰️ AstroBot — Discord Bot & Control Panel

<div align="center">

![AstroBot Logo](asbotlogo.ico)

**Un potente bot de Discord multifunción acompañado de un Panel de Control de escritorio moderno, visual y fácil de usar.**

[![Release](https://img.shields.io/github/v/release/AstroSoftwareMoon/AstroSoftware-Panel-Control-Bot-Discord?color=7C5CFF&label=Descargar%20Última%20Versión)](https://github.com/AstroSoftwareMoon/AstroSoftware-Panel-Control-Bot-Discord/releases)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![discord.py](https://img.shields.io/badge/discord.py-2.0%2B-blueviolet.svg)](https://github.com/Rapptz/discord.py)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-brightgreen.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()

[Descargar para Windows / Linux](https://github.com/AstroSoftwareMoon/AstroSoftware-Panel-Control-Bot-Discord/releases) • [Servidor de Soporte](https://discord.gg/eBszxvAuhN) • [Reportar Error](https://github.com/AstroSoftwareMoon/AstroSoftware-Panel-Control-Bot-Discord/issues)

</div>

---

## 🌟 Características Principales

- 🌐 **Soporte Multi-idioma en Vivo (i18n):**
  - Cambia instantáneamente entre **Español 🇪🇸**, **Inglés 🇬🇧** e **Italiano 🇮🇹** tanto en la aplicación como en las respuestas del bot en Discord.
- ⚡ **100% Slash Commands (`/`):**
  - Modernizado por completo. Todos los comandos usan el sistema nativo de Discord con autocompletado y validación.
- 🎛️ **Panel de Control Gráfico Moderno:**
  - Diseñado con tema oscuro profesional y elegante.
  - Inicia y detén el bot con un solo clic.
  - Estadísticas en vivo: monitoreo de Servidores, Usuarios, Latencia, Uptime, CPU y Memoria RAM del host.
- 🧩 **Gestor de Comandos Dinámico:**
  - Apaga o enciende comandos individuales en tiempo real sin necesidad de reiniciar el bot ni la app.
- 📝 **Consola de Registros (Logs):**
  - Visor en vivo con opción de exportar el historial a archivos `.txt`.

---

## 💻 Comandos Incluidos

| Categoría | Comandos | Descripción |
| :--- | :--- | :--- |
| **📊 Información** | `/serverinfo`, `/botinfo`, `/ping`, `/userinfo` | Estadísticas detalladas de tu servidor, del bot y de los usuarios con Embeds. |
| **🛡️ Moderación** | `/warn`, `/kick`, `/mute`, `/unmute`, `/ban`, `/unban`, `/clear` | Herramientas esenciales de moderación con registros automáticos y duraciones. |
| **🎮 Diversión** | `/8ball`, `/coinflip`, `/dice`, `/cat` | Bola 8 mágica, cara o cruz, tirada de dados (d20, 2d6...) y fotos de gatitos. |
| **🛠️ Utilidades** | `/avatar`, `/soporte`, `/sponsor` | Visualizador de avatares en HD, enlaces de soporte y comunidad oficial. |

---

## 🚀 Descarga e Instalación

### 📦 Opción 1: Ejecutables directos (Recomendada)
No necesitas tener Python instalado.
1. Ve a la sección de **[Releases / Lanzamientos](https://github.com/AstroSoftwareMoon/AstroSoftware-Panel-Control-Bot-Discord/releases)**.
2. Descarga el archivo comprimido según tu sistema:
   - **Windows:** `AstroBot-Windows.zip` (descomprime y ejecuta `AstroBot.exe`).
   - **Linux:** `AstroBot-Linux.zip` (descomprime y ejecuta el binario `./AstroBot`).
3. Ingresa el **Token** de tu bot en la pestaña **Configuración** y pulsa **Iniciar Bot**.

---

### 🐍 Opción 2: Ejecutar desde el código fuente

Si prefieres ejecutarlo manualmente con Python:

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/AstroSoftwareMoon/AstroSoftware-Panel-Control-Bot-Discord.git
   cd AstroSoftware-Panel-Control-Bot-Discord
   ```

2. **Instala las dependencias necesarias:**
   ```bash
   pip install customtkinter discord.py psutil requests
   ```

3. **Inicia la aplicación:**
   ```bash
   python astrobot.py
   ```

---

## ⚙️ Configuración Inicial del Bot en Discord

Para que tu bot funcione con todas sus funciones:
1. Ve al [Portal de Desarrolladores de Discord](https://discord.com/developers/applications).
2. Crea tu aplicación y ve a la sección **Bot**.
3. Activa los siguientes **Privileged Gateway Intents**:
   - **Presence Intent**
   - **Server Members Intent**
   - **Message Content Intent**
4. Copia tu **Token** y pégalo en la pestaña **Configuración** de AstroBot.
5. Copia tu **Client ID** para poder invitar al bot fácilmente desde el panel.

---

## 🤝 Soporte y Comunidad

¿Necesitas ayuda para configurarlo o quieres reportar un problema?
- Únete a nuestra comunidad oficial en Discord: [**AstroSoftware & Asociados**](https://discord.gg/eBszxvAuhN)

---

<div align="center">
Desarrollado con ❤️ por <b>AstroSoftware</b>.
</div>
