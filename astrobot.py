import os
import sqlite3
import json
import sys
import subprocess
import random
from datetime import datetime, timedelta
import asyncio
import logging
import platform
from typing import Optional, Union
import threading
import queue
import tkinter as tk
from tkinter import messagebox, filedialog
import time
import webbrowser


# ============================================================
# LOCALES EMBEBIDOS (fuente de verdad)
# ============================================================
DEFAULT_LOCALES = {
    "es": {
        "footer": "🚀 AstroSoftware | Patrocinado por: {name}",
        "value_na": "N/D", "none": "Ninguno", "yes": "Sí ✅", "no": "No ❌",
        "generic_error": "❌ Ocurrió un error inesperado.",
        "uptime_starting": "Iniciando...",
        "footer_requested_by": "Solicitado por {name}",
        "sidebar_title": "🛰️  AstroBot", "sidebar_subtitle": "Panel de Control",
        "nav_dashboard": "🏠   Panel de Control", "nav_settings": "⚙️   Configuración",
        "nav_commands": "🧩   Comandos", "nav_logs": "📜   Registros", "nav_about": "ℹ️   Acerca de",
        "title_dashboard_full": "🌌 Panel de Control",
        "desc_dashboard": "Gestiona la conexión, supervisa el estado y controla tu bot en tiempo real.",
        "btn_start_bot": "🚀 Iniciar Bot", "btn_stop_bot": "🛑 Detener Bot",
        "btn_invite": "🔗 Invitar Bot", "btn_support": "❓ Soporte",
        "stat_servers": "Servidores", "stat_users": "Usuarios", "stat_latency": "Latencia",
        "stat_uptime": "Uptime", "stat_cpu": "CPU (Host)", "stat_ram": "RAM (Host)",
        "recent_activity": "📜 Actividad Reciente",
        "status_connected": "🟢  Conectado", "status_stopped": "●  Detenido",
        "status_starting": "Iniciando...", "status_stopping": "Deteniendo...",
        "status_error": "🔴  Error",
        "title_settings_full": "⚙️ Configuración del Bot",
        "desc_settings": "Ajusta las credenciales, la promoción y la presencia del bot.",
        "sec_credentials": "🔑 Credenciales del Bot",
        "lbl_token": "Token del Bot:", "lbl_client_id": "Client ID (para invitación):",
        "desc_client_id": "El Client ID se usa solo para generar el enlace de invitación del bot.",
        "sec_promo": "📣 Promoción",
        "lbl_promo_link": "Link de Promoción:", "lbl_promo_name": "Nombre Promocional:",
        "lbl_language": "🌐 Idioma / Language / Lingua",
        "sec_presence": "🎮 Presencia (Estado del Bot)",
        "lbl_act_type": "Tipo de Actividad:", "lbl_act_text": "Texto de Actividad:",
        "btn_save_settings": "💾 Guardar Cambios",
        "settings_saved_msg": "Configuración guardada correctamente.",
        "title_commands": "🧩 Gestor de Comandos",
        "desc_commands": "Activa o desactiva comandos individualmente sin reiniciar el bot.",
        "placeholder_search": "🔍  Buscar comando...",
        "btn_save_commands": "💾 Guardar Comandos",
        "commands_saved_msg": "Comandos actualizados.",
        "cat_general_name": "📊 Información", "cat_moderation_name": "🛡️ Moderación",
        "cat_fun_name": "🎮 Diversión", "cat_utility_name": "🛠️ Utilidades",
        "title_logs": "📜 Registros Completos", "btn_export": "💾 Exportar",
        "btn_clear_view": "🧹 Limpiar Vista",
        "logs_exported_msg": "Registros exportados correctamente a:\n",
        "logs_export_err": "No se pudo exportar el registro: ",
        "about_title": "🛰️ AstroBot Control Panel", "about_version": "Versión",
        "about_dev": "Desarrollado por",
        "about_desc": "Panel de control profesional para gestionar tu bot de Discord con comandos rápidos, modernos y visuales en tiempo real.",
        "btn_support_server": "❓ Servidor de Soporte", "btn_view_logs": "📁 Ver Logs en Disco",
        "about_rights": "Todos los derechos reservados",
        "err_token_empty": "Debes ingresar el Token del Bot en Configuración.",
        "cmd_disabled": "❌ Este comando ha sido desactivado por el administrador.",
        "help_title": "🛸 Menú de Ayuda de AstroBot 🚀",
        "help_desc": "¡Hola! Soy **AstroBot**, tu copiloto para gestionar el servidor. 🌌\nUsa el **menú desplegable** de abajo para explorar cada categoría de comandos.\n\n🔤 **Prefijo actual:** `/`\n✅ **Comandos disponibles:** `{n}`",
        "help_cmds_available": "comando(s) disponible(s)",
        "help_footer": "💡 Usa el menú de abajo para navegar",
        "help_cat_footer": "⬅️ Vuelve al inicio con el menú de abajo",
        "help_empty_title": "😴 Nada por aquí",
        "help_empty_desc": "No hay comandos disponibles en esta categoría (o están desactivados).",
        "help_no_desc": "Sin descripción disponible.",
        "help_placeholder": "🔎  Elige una categoría de comandos...",
        "help_opt_home": "🏠 Inicio", "help_opt_home_desc": "Vuelve al menú principal de ayuda",
        "help_btn_invite": "Añadir a mi servidor", "help_btn_support": "Soporte",
        "cat_general_desc": "Datos y estadísticas del servidor, el bot y los usuarios.",
        "cat_moderation_desc": "Herramientas para mantener el orden en tu servidor.",
        "cat_fun_desc": "Minijuegos y comandos de ocio para pasar el rato.",
        "cat_utility_desc": "Avatares, patrocinio y ayuda adicional.",
        "mod_default_reason": "No especificada",
        "mod_dm_title": "{title} en el servidor '{guild}'",
        "welcome_title": "🎉 ¡Nuevo Astronauta en la Misión! 🚀",
        "welcome_desc": "¡Bienvenido {mention} a **{guild}**! 🌟",
        "welcome_member_count": "Miembro #{count}",
        "welcome_default_footer": "¡Explora la galaxia con nosotros!",
        "cmd_serverinfo_title": "🖥️ Servidor: {name}",
        "cmd_serverinfo_owner": "👑 Propietario", "cmd_serverinfo_members": "👥 Miembros",
        "cmd_serverinfo_creation": "📅 Creación", "cmd_serverinfo_channels": "📊 Canales",
        "cmd_serverinfo_roles": "📜 Roles", "cmd_serverinfo_content": "🎨 Contenido",
        "cmd_botinfo_title": "🤖 AstroBot (v{ver})",
        "cmd_botinfo_desc": "Bot multifunción por **{author}**.",
        "cmd_botinfo_uptime": "⏳ Uptime", "cmd_botinfo_latency": "📡 Latencia",
        "cmd_botinfo_servers": "🌐 Servidores", "cmd_botinfo_users": "👥 Usuarios",
        "cmd_botinfo_footer": "© {year} | PID: {pid}",
        "cmd_ping_calculating": "📡 Calculando latencia...",
        "cmd_ping_pong": "🏓 ¡Pong!", "cmd_ping_response": "⚡ Respuesta",
        "cmd_ping_api": "🌐 API", "cmd_ping_stable": "¡Conexión estable!",
        "cmd_support_title": "🔧 Servidor de Soporte",
        "cmd_support_desc": "¡Únete a nuestro servidor!\n\n➡️ [Haz clic aquí]({link}) ⬅️",
        "cmd_support_footer": "¡Te esperamos!",
        "cmd_userinfo_title": "{status} Usuario: {name}",
        "cmd_userinfo_desc": "**ID:** `{id}` | **Mención:** {mention}",
        "cmd_userinfo_username": "🏷️ Usuario", "cmd_userinfo_isbot": "🤖 Bot?",
        "cmd_userinfo_created": "📅 Cuenta", "cmd_userinfo_joined": "📥 Se unió",
        "cmd_userinfo_roles": "📜 Roles ({n})",
        "cmd_avatar_title": "🖼️ Avatar de {name}",
        "avatar_direct_link": "[Enlace]({url})",
        "sponsor_title": "✨ AstroSoftware ✨",
        "sponsor_desc": "¡Únete a nuestra comunidad!",
        "sponsor_links_field": "🔗 Enlaces", "sponsor_join": "Únete",
        "sponsor_join_btn": "¡Unirse!",
        "8ball_title": "🎱 La Bola 8 Dice...", "8ball_answer": "Respuesta:",
        "coinflip_title": "🪙 Moneda", "coinflip_result": "¡**{r}**!",
        "coinflip_heads": "Cara", "coinflip_tails": "Cruz",
    },
    "en": {
        "footer": "🚀 AstroSoftware | Sponsored by: {name}",
        "value_na": "N/A", "none": "None", "yes": "Yes ✅", "no": "No ❌",
        "generic_error": "❌ An unexpected error occurred.",
        "uptime_starting": "Starting...",
        "footer_requested_by": "Requested by {name}",
        "sidebar_title": "🛰️  AstroBot", "sidebar_subtitle": "Control Panel",
        "nav_dashboard": "🏠   Dashboard", "nav_settings": "⚙️   Settings",
        "nav_commands": "🧩   Commands", "nav_logs": "📜   Logs", "nav_about": "ℹ️   About",
        "title_dashboard_full": "🌌 Dashboard",
        "desc_dashboard": "Manage the connection, monitor status and control your bot in real time.",
        "btn_start_bot": "🚀 Start Bot", "btn_stop_bot": "🛑 Stop Bot",
        "btn_invite": "🔗 Invite Bot", "btn_support": "❓ Support",
        "stat_servers": "Servers", "stat_users": "Users", "stat_latency": "Latency",
        "stat_uptime": "Uptime", "stat_cpu": "CPU (Host)", "stat_ram": "RAM (Host)",
        "recent_activity": "📜 Recent Activity",
        "status_connected": "🟢  Connected", "status_stopped": "●  Stopped",
        "status_starting": "Starting...", "status_stopping": "Stopping...",
        "status_error": "🔴  Error",
        "title_settings_full": "⚙️ Bot Settings",
        "desc_settings": "Adjust credentials, promotion and bot presence.",
        "sec_credentials": "🔑 Bot Credentials",
        "lbl_token": "Bot Token:", "lbl_client_id": "Client ID (for invite):",
        "desc_client_id": "The Client ID is used only to generate the bot invite link.",
        "sec_promo": "📣 Promotion",
        "lbl_promo_link": "Promotion Link:", "lbl_promo_name": "Promotional Name:",
        "lbl_language": "🌐 Language / Idioma / Lingua",
        "sec_presence": "🎮 Presence (Bot Status)",
        "lbl_act_type": "Activity Type:", "lbl_act_text": "Activity Text:",
        "btn_save_settings": "💾 Save Changes",
        "settings_saved_msg": "Settings saved successfully.",
        "title_commands": "🧩 Command Manager",
        "desc_commands": "Enable or disable individual commands without restarting the bot.",
        "placeholder_search": "🔍  Search command...",
        "btn_save_commands": "💾 Save Commands",
        "commands_saved_msg": "Commands updated.",
        "cat_general_name": "📊 Info", "cat_moderation_name": "🛡️ Moderation",
        "cat_fun_name": "🎮 Fun", "cat_utility_name": "🛠️ Utilities",
        "title_logs": "📜 Full Logs", "btn_export": "💾 Export",
        "btn_clear_view": "🧹 Clear View",
        "logs_exported_msg": "Logs exported successfully to:\n",
        "logs_export_err": "Could not export log: ",
        "about_title": "🛰️ AstroBot Control Panel", "about_version": "Version",
        "about_dev": "Developed by",
        "about_desc": "Professional control panel to manage your Discord bot with fast, modern, real-time visual commands.",
        "btn_support_server": "❓ Support Server", "btn_view_logs": "📁 View Logs on Disk",
        "about_rights": "All rights reserved",
        "err_token_empty": "You must enter the Bot Token in Settings.",
        "cmd_disabled": "❌ This command has been disabled by the administrator.",
        "help_title": "🛸 AstroBot Help Menu 🚀",
        "help_desc": "Hi! I'm **AstroBot**, your co-pilot to manage the server. 🌌\nUse the **dropdown** below to explore each command category.\n\n🔤 **Current prefix:** `/`\n✅ **Available commands:** `{n}`",
        "help_cmds_available": "command(s) available",
        "help_footer": "💡 Use the dropdown below to navigate",
        "help_cat_footer": "⬅️ Go back to home with the dropdown below",
        "help_empty_title": "😴 Nothing here",
        "help_empty_desc": "No commands available in this category (or they are disabled).",
        "help_no_desc": "No description available.",
        "help_placeholder": "🔎  Pick a command category...",
        "help_opt_home": "🏠 Home", "help_opt_home_desc": "Return to the main help menu",
        "help_btn_invite": "Add to my server", "help_btn_support": "Support",
        "cat_general_desc": "Data and statistics about the server, bot and users.",
        "cat_moderation_desc": "Tools to keep your server in order.",
        "cat_fun_desc": "Minigames and fun commands to pass the time.",
        "cat_utility_desc": "Avatars, sponsorship and additional help.",
        "mod_default_reason": "Not specified",
        "mod_dm_title": "{title} on server '{guild}'",
        "welcome_title": "🎉 New Astronaut on the Mission! 🚀",
        "welcome_desc": "Welcome {mention} to **{guild}**! 🌟",
        "welcome_member_count": "Member #{count}",
        "welcome_default_footer": "Explore the galaxy with us!",
        "cmd_serverinfo_title": "🖥️ Server: {name}",
        "cmd_serverinfo_owner": "👑 Owner", "cmd_serverinfo_members": "👥 Members",
        "cmd_serverinfo_creation": "📅 Created", "cmd_serverinfo_channels": "📊 Channels",
        "cmd_serverinfo_roles": "📜 Roles", "cmd_serverinfo_content": "🎨 Content",
        "cmd_botinfo_title": "🤖 AstroBot (v{ver})",
        "cmd_botinfo_desc": "Multipurpose bot by **{author}**.",
        "cmd_botinfo_uptime": "⏳ Uptime", "cmd_botinfo_latency": "📡 Latency",
        "cmd_botinfo_servers": "🌐 Servers", "cmd_botinfo_users": "👥 Users",
        "cmd_botinfo_footer": "© {year} | PID: {pid}",
        "cmd_ping_calculating": "📡 Calculating latency...",
        "cmd_ping_pong": "🏓 Pong!", "cmd_ping_response": "⚡ Response",
        "cmd_ping_api": "🌐 API", "cmd_ping_stable": "Connection looks stable!",
        "cmd_support_title": "🔧 Support Server",
        "cmd_support_desc": "Join our server!\n\n➡️ [Click here]({link}) ⬅️",
        "cmd_support_footer": "See you there!",
        "cmd_userinfo_title": "{status} User: {name}",
        "cmd_userinfo_desc": "**ID:** `{id}` | **Mention:** {mention}",
        "cmd_userinfo_username": "🏷️ Username", "cmd_userinfo_isbot": "🤖 Bot?",
        "cmd_userinfo_created": "📅 Account", "cmd_userinfo_joined": "📥 Joined",
        "cmd_userinfo_roles": "📜 Roles ({n})",
        "cmd_avatar_title": "🖼️ {name}'s Avatar",
        "avatar_direct_link": "[Link]({url})",
        "sponsor_title": "✨ AstroSoftware ✨",
        "sponsor_desc": "Join our community!",
        "sponsor_links_field": "🔗 Links", "sponsor_join": "Join",
        "sponsor_join_btn": "Join now!",
        "8ball_title": "🎱 The Magic 8-Ball Says...", "8ball_answer": "Answer:",
        "coinflip_title": "🪙 Coin Flip", "coinflip_result": "**{r}**!",
        "coinflip_heads": "Heads", "coinflip_tails": "Tails",
    },
    "it": {
        "footer": "🚀 AstroSoftware | Sponsorizzato da: {name}",
        "value_na": "N/D", "none": "Nessuno", "yes": "Sì ✅", "no": "No ❌",
        "generic_error": "❌ Si è verificato un errore imprevisto.",
        "uptime_starting": "Avvio in corso...",
        "footer_requested_by": "Richiesto da {name}",
        "sidebar_title": "🛰️  AstroBot", "sidebar_subtitle": "Pannello di Controllo",
        "nav_dashboard": "🏠   Dashboard", "nav_settings": "⚙️   Impostazioni",
        "nav_commands": "🧩   Comandi", "nav_logs": "📜   Registri", "nav_about": "ℹ️   Info",
        "title_dashboard_full": "🌌 Pannello di Controllo",
        "desc_dashboard": "Gestisci la connessione, monitora lo stato e controlla il tuo bot in tempo reale.",
        "btn_start_bot": "🚀 Avvia Bot", "btn_stop_bot": "🛑 Ferma Bot",
        "btn_invite": "🔗 Invita Bot", "btn_support": "❓ Supporto",
        "stat_servers": "Server", "stat_users": "Utenti", "stat_latency": "Latenza",
        "stat_uptime": "Uptime", "stat_cpu": "CPU (Host)", "stat_ram": "RAM (Host)",
        "recent_activity": "📜 Attività Recente",
        "status_connected": "🟢  Connesso", "status_stopped": "●  Fermo",
        "status_starting": "Avvio...", "status_stopping": "Arresto...",
        "status_error": "🔴  Errore",
        "title_settings_full": "⚙️ Impostazioni del Bot",
        "desc_settings": "Regola credenziali, promozione e presenza del bot.",
        "sec_credentials": "🔑 Credenziali del Bot",
        "lbl_token": "Token del Bot:", "lbl_client_id": "Client ID (per invito):",
        "desc_client_id": "Il Client ID viene usato solo per generare il link d'invito del bot.",
        "sec_promo": "📣 Promozione",
        "lbl_promo_link": "Link Promozionale:", "lbl_promo_name": "Nome Promozionale:",
        "lbl_language": "🌐 Lingua / Language / Idioma",
        "sec_presence": "🎮 Presenza (Stato del Bot)",
        "lbl_act_type": "Tipo di Attività:", "lbl_act_text": "Testo Attività:",
        "btn_save_settings": "💾 Salva Modifiche",
        "settings_saved_msg": "Impostazioni salvate correttamente.",
        "title_commands": "🧩 Gestore Comandi",
        "desc_commands": "Attiva o disattiva singoli comandi senza riavviare il bot.",
        "placeholder_search": "🔍  Cerca comando...",
        "btn_save_commands": "💾 Salva Comandi",
        "commands_saved_msg": "Comandi aggiornati.",
        "cat_general_name": "📊 Informazioni", "cat_moderation_name": "🛡️ Moderazione",
        "cat_fun_name": "🎮 Divertimento", "cat_utility_name": "🛠️ Utilità",
        "title_logs": "📜 Registri Completi", "btn_export": "💾 Esporta",
        "btn_clear_view": "🧹 Pulisci Vista",
        "logs_exported_msg": "Registri esportati correttamente in:\n",
        "logs_export_err": "Impossibile esportare il registro: ",
        "about_title": "🛰️ AstroBot Control Panel", "about_version": "Versione",
        "about_dev": "Sviluppato da",
        "about_desc": "Pannello di controllo professionale per gestire il tuo bot Discord.",
        "btn_support_server": "❓ Server di Supporto", "btn_view_logs": "📁 Vedi Log su Disco",
        "about_rights": "Tutti i diritti riservati",
        "err_token_empty": "Devi inserire il Token del Bot nelle Impostazioni.",
        "cmd_disabled": "❌ Questo comando è stato disattivato dall'amministratore.",
        "help_title": "🛸 Menu di Aiuto di AstroBot 🚀",
        "help_desc": "Ciao! Sono **AstroBot**.\n🔤 **Prefisso:** `/`\n✅ **Comandi disponibili:** `{n}`",
        "help_cmds_available": "comando/i disponibile/i",
        "help_footer": "💡 Usa il menu qui sotto per navigare",
        "help_cat_footer": "⬅️ Torna alla home con il menu qui sotto",
        "help_empty_title": "😴 Niente qui",
        "help_empty_desc": "Nessun comando disponibile in questa categoria.",
        "help_no_desc": "Nessuna descrizione disponibile.",
        "help_placeholder": "🔎  Scegli una categoria di comandi...",
        "help_opt_home": "🏠 Home", "help_opt_home_desc": "Torna al menu principale",
        "help_btn_invite": "Aggiungi al mio server", "help_btn_support": "Supporto",
        "cat_general_desc": "Dati e statistiche su server, bot e utenti.",
        "cat_moderation_desc": "Strumenti per mantenere l'ordine nel server.",
        "cat_fun_desc": "Minigiochi e comandi divertenti.",
        "cat_utility_desc": "Avatar, sponsorizzazione e aiuto aggiuntivo.",
        "mod_default_reason": "Non specificata",
        "mod_dm_title": "{title} nel server '{guild}'",
        "welcome_title": "🎉 Nuovo Astronauta in Missione! 🚀",
        "welcome_desc": "Benvenuto {mention} su **{guild}**! 🌟",
        "welcome_member_count": "Membro #{count}",
        "welcome_default_footer": "Esplora la galassia con noi!",
        "cmd_serverinfo_title": "🖥️ Server: {name}",
        "cmd_serverinfo_owner": "👑 Proprietario", "cmd_serverinfo_members": "👥 Membri",
        "cmd_serverinfo_creation": "📅 Creazione", "cmd_serverinfo_channels": "📊 Canali",
        "cmd_serverinfo_roles": "📜 Ruoli", "cmd_serverinfo_content": "🎨 Contenuto",
        "cmd_botinfo_title": "🤖 AstroBot (v{ver})",
        "cmd_botinfo_desc": "Bot multifunzione di **{author}**.",
        "cmd_botinfo_uptime": "⏳ Uptime", "cmd_botinfo_latency": "📡 Latenza",
        "cmd_botinfo_servers": "🌐 Server", "cmd_botinfo_users": "👥 Utenti",
        "cmd_botinfo_footer": "© {year} | PID: {pid}",
        "cmd_ping_calculating": "📡 Calcolo latenza...",
        "cmd_ping_pong": "🏓 Pong!", "cmd_ping_response": "⚡ Risposta",
        "cmd_ping_api": "🌐 API", "cmd_ping_stable": "Connessione stabile!",
        "cmd_support_title": "🔧 Server di Supporto",
        "cmd_support_desc": "Unisciti al nostro server!\n\n➡️ [Clicca qui]({link}) ⬅️",
        "cmd_support_footer": "Ti aspettiamo!",
        "cmd_userinfo_title": "{status} Utente: {name}",
        "cmd_userinfo_desc": "**ID:** `{id}` | **Menzione:** {mention}",
        "cmd_userinfo_username": "🏷️ Username", "cmd_userinfo_isbot": "🤖 Bot?",
        "cmd_userinfo_created": "📅 Account", "cmd_userinfo_joined": "📥 Iscritto",
        "cmd_userinfo_roles": "📜 Ruoli ({n})",
        "cmd_avatar_title": "🖼️ Avatar di {name}",
        "avatar_direct_link": "[Link]({url})",
        "sponsor_title": "✨ AstroSoftware ✨",
        "sponsor_desc": "Unisciti alla nostra community!",
        "sponsor_links_field": "🔗 Link", "sponsor_join": "Unisciti",
        "sponsor_join_btn": "Iscriviti ora!",
        "8ball_title": "🎱 La Palla Magica 8 Dice...", "8ball_answer": "Risposta:",
        "coinflip_title": "🪙 Lancio Moneta", "coinflip_result": "**{r}**!",
        "coinflip_heads": "Testa", "coinflip_tails": "Croce",
    },
}


def ensure_locales_exist():
    """
    Crea/actualiza los archivos de locales en disco.
    Si al archivo del disco le faltan claves de los embebidos, lo actualiza (merge).
    Si el archivo no existe, lo crea con los embebidos.
    Si el archivo ya está completo, no lo toca (respeta ediciones manuales).
    """
    try:
        os.makedirs("locales", exist_ok=True)
        for lang_code, defaults in DEFAULT_LOCALES.items():
            path = os.path.join("locales", f"{lang_code}.json")
            existing = {}
            if os.path.exists(path):
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        existing = json.load(f)
                except Exception as e:
                    print(f"[Locales] Archivo '{path}' corrupto, se regenerará: {e}")
                    existing = {}

            missing = set(defaults.keys()) - set(existing.keys())
            if missing:
                merged = {**defaults, **existing}  # los del disco ganan en las claves comunes
                with open(path, "w", encoding="utf-8") as f:
                    json.dump(merged, f, indent=2, ensure_ascii=False)
                if existing:
                    print(f"[Locales] '{path}' actualizado con {len(missing)} claves nuevas.")
                else:
                    print(f"[Locales] '{path}' creado ({len(merged)} claves).")
    except Exception as e:
        print(f"[Locales] Error en ensure_locales_exist: {e}")


class LanguageManager:
    def __init__(self):
        self.locales = {}
        self.current_lang = "es"

    def load_language(self, lang_code="es"):
        """
        Carga el idioma haciendo merge:
          1. Parte de los locales EMBEBIDOS (garantiza todas las claves).
          2. Sobrescribe con lo que haya en disco (respeta ediciones manuales).
        """
        self.current_lang = lang_code
        base = dict(DEFAULT_LOCALES.get(lang_code, {}))

        file_path = os.path.join("locales", f"{lang_code}.json")
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    disk = json.load(f)
                base.update(disk)
            except Exception as e:
                print(f"[Locales] Error cargando '{lang_code}': {e}")

        self.locales = base
        print(f"[Locales] Idioma cargado: '{lang_code}' ({len(base)} claves)")

    def get(self, key, default=None):
        if default is None:
            default = key
        return self.locales.get(key, default)


lang_manager = LanguageManager()


def tr(key, default=None):
    return lang_manager.get(key, default)


try:
    import customtkinter
    import discord
    from discord.ext import commands, tasks
    import psutil
    import requests
    try:
        import nacl
    except ImportError:
        nacl = None
except ImportError as e:
    module_name = e.name
    print(f"\n--- ¡ERROR FATAL: FALTA LIBRERÍA '{module_name}'! ---")
    print(f"Ejecuta: python -m pip install --upgrade customtkinter discord.py psutil requests PyNaCl\n")
    try:
        root = tk.Tk(); root.withdraw()
        messagebox.showerror("Error Fatal", f"Falta la librería '{module_name}'. Instálala con pip.")
        root.destroy()
    except tk.TclError:
        pass
    sys.exit(1)


log_queue = queue.Queue()
log_level_gui = logging.INFO


class QueueHandler(logging.Handler):
    def __init__(self, log_queue_ref):
        super().__init__()
        self.log_queue = log_queue_ref

    def emit(self, record):
        self.log_queue.put(self.format(record))


logger = logging.getLogger("AstroBotGUI_CTk_Themed_V3")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)

log_dir = "logs"
if not os.path.exists(log_dir):
    try:
        os.makedirs(log_dir)
    except OSError:
        log_dir = "."
log_file_path = os.path.join(log_dir, "astrobot_themed_gui_v3.log")
file_handler = logging.FileHandler(log_file_path, encoding='utf-8')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

gui_handler = QueueHandler(log_queue)
gui_handler.setFormatter(formatter)
gui_handler.setLevel(log_level_gui)
logger.addHandler(gui_handler)

if nacl is None:
    logger.warning("PyNaCl no está instalado. Funcionalidad de VOZ no disponible.")

__version__ = "1.8.4"
__author__ = "UnoDeTusSecretos (AstroSoftware)"
__year__ = datetime.now().year


CONFIG_FILE = "config.json"
DEFAULT_CONFIG = {
    "token": "",
    "spam_link": "https://discord.gg/eBszxvAuhN",
    "spam_name": "AstroSoftware y Asociados",
    "activity_type": "playing",
    "activity_name": "AstroBot V3",
    "disabled_commands": [],
    "spam_channel_id": None,
    "client_id": "",
    "language": "es"
}


def load_config():
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        return DEFAULT_CONFIG
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return DEFAULT_CONFIG


def save_config(config):
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)


# === ORDEN IMPORTANTE ===
ensure_locales_exist()
config_data = load_config()
lang_manager.load_language(config_data.get('language', 'es'))


def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id TEXT PRIMARY KEY, xp INTEGER DEFAULT 0, level INTEGER DEFAULT 1,
                    balance INTEGER DEFAULT 0, last_daily TEXT)''')
    conn.commit()
    conn.close()


init_db()


def get_user_db(user_id):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE user_id = ?", (str(user_id),))
    row = c.fetchone()
    if not row:
        c.execute("INSERT INTO users (user_id) VALUES (?)", (str(user_id),))
        conn.commit()
        row = (str(user_id), 0, 1, 0, None)
    conn.close()
    return row


def update_user_db(user_id, xp=None, level=None, balance=None, last_daily=None):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    if xp is not None: c.execute("UPDATE users SET xp = ? WHERE user_id = ?", (xp, str(user_id)))
    if level is not None: c.execute("UPDATE users SET level = ? WHERE user_id = ?", (level, str(user_id)))
    if balance is not None: c.execute("UPDATE users SET balance = ? WHERE user_id = ?", (balance, str(user_id)))
    if last_daily is not None: c.execute("UPDATE users SET last_daily = ? WHERE user_id = ?", (last_daily, str(user_id)))
    conn.commit()
    conn.close()


def build_footer():
    return tr("footer", "🚀 AstroSoftware | Patrocinado por: {name}").format(
        name=config_data.get('spam_name', 'Astro'))


class AdvancedAstroBot:

    def __init__(self, token: str):
        if not token:
            raise ValueError("El token del bot no puede estar vacío.")
        self.token = token
        self.running = False
        self._shutdown_event = asyncio.Event()
        self.start_time: Optional[datetime] = None
        self.bot_loop: Optional[asyncio.AbstractEventLoop] = None
        self.command_counter = 0

        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.guilds = True
        intents.bans = True

        self.bot = commands.Bot(command_prefix="!@#$%^&*IMPOSSIBLE", intents=intents, help_command=None)

        self._setup_events()
        self._setup_general_commands()
        self._setup_moderation_commands()
        self._setup_fun_commands()
        self._setup_utility_commands()
        self._setup_sponsor_commands()
        self._setup_help_command()
        logger.info(f"Instancia de AdvancedAstroBot v{__version__} creada.")

    def log(self, message: str, level: str = "info"):
        getattr(logger, level.lower(), logger.info)(message)

    def get_uptime(self) -> str:
        if not self.start_time:
            return tr("uptime_starting", "Iniciando...")
        delta = datetime.utcnow() - self.start_time
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        parts = []
        if days > 0: parts.append(f"{days}d")
        if hours > 0: parts.append(f"{hours}h")
        if minutes > 0: parts.append(f"{minutes}m")
        if seconds >= 0: parts.append(f"{seconds}s")
        return " ".join(parts) or "< 1s"

    def _setup_events(self):

        @self.bot.check
        async def global_command_check(ctx):
            if ctx.command and ctx.command.name in config_data.get("disabled_commands", []):
                await ctx.send(tr("cmd_disabled", "❌ Comando desactivado."), ephemeral=True)
                return False
            return True

        @self.bot.event
        async def on_ready():
            # ✅ FIX: guardar el event loop para poder detener el bot después
            try:
                self.bot_loop = asyncio.get_running_loop()
                self.log(f"Event loop capturado OK.")
            except RuntimeError as e:
                self.log(f"No se pudo obtener el event loop: {e}", level="error")

            self.start_time = datetime.utcnow()
            try:
                synced = await self.bot.tree.sync()
                self.log(f'Sincronizados {len(synced)} slash commands globales.')
            except Exception as e:
                self.log(f'Error al sincronizar: {e}', level="error")

            self.log(f'🚀 Bot conectado como {self.bot.user.name} ({self.bot.user.id})')
            self.log(f'Activo en {len(self.bot.guilds)} servidores.')
            self.running = True
            self._shutdown_event.clear()
            if not self.change_status_task.is_running():
                try:
                    self.change_status_task.start()
                    self.log("Tarea de cambio de estado iniciada.")
                except RuntimeError:
                    pass

        @self.bot.event
        async def on_member_join(member: discord.Member):
            self.log(f"Nuevo miembro: {member.name} en {member.guild.name}")
            try:
                welcome_channel = member.guild.system_channel
                if not welcome_channel:
                    potential = [ch for ch in member.guild.text_channels
                                 if 'bienvenida' in ch.name.lower() or 'welcome' in ch.name.lower()]
                    if potential: welcome_channel = potential[0]
                if welcome_channel and welcome_channel.permissions_for(member.guild.me).send_messages:
                    embed = discord.Embed(
                        title=tr("welcome_title", "🎉 ¡Bienvenido!"),
                        description=tr("welcome_desc", "¡Bienvenido {mention} a **{guild}**!").format(
                            mention=member.mention, guild=member.guild.name),
                        color=discord.Color.cyan())
                    if member.display_avatar:
                        embed.set_thumbnail(url=member.display_avatar.url)
                    try:
                        embed.set_footer(text=build_footer() + " | " + tr("welcome_member_count", "Miembro #{count}").format(count=member.guild.member_count))
                    except Exception:
                        embed.set_footer(text=build_footer())
                    embed.timestamp = datetime.utcnow()
                    await welcome_channel.send(embed=embed)
            except Exception as e:
                self.log(f"Error en on_member_join: {e}", level="error")

        @self.bot.event
        async def on_command_completion(ctx):
            self.command_counter += 1
            if self.command_counter >= 10:
                self.command_counter = 0
                try:
                    embed = discord.Embed(
                        title=tr("spam_auto_title", "🚀 ¡Servidor Patrocinado!"),
                        description=tr("spam_auto_desc", "Únete a nuestra comunidad."),
                        color=discord.Color.magenta())
                    embed.add_field(
                        name=tr("spam_auto_field", "Enlace"),
                        value=f"[{tr('spam_auto_click', 'Clic aquí')}]({config_data.get('spam_link', '')})")
                    embed.set_footer(text=build_footer())
                    await ctx.channel.send(embed=embed)
                except Exception as e:
                    self.log(f"Error en spam automático: {e}")

        @self.bot.event
        async def on_command_error(ctx, error):
            if isinstance(error, commands.CommandNotFound): return
            if isinstance(error, commands.CheckFailure):
                await ctx.send(tr("err_check_fail", "🚫 Sin requisitos."), delete_after=10); return
            if isinstance(error, commands.CommandOnCooldown):
                await ctx.send(tr("err_cooldown", "⏳ Enfriamiento: {s:.1f}s.").format(s=error.retry_after), delete_after=7); return
            if isinstance(error, commands.CommandInvokeError):
                logger.exception("Error interno:", exc_info=error.original)
                await ctx.send(tr("err_invoke", "🔧 Error interno."), delete_after=10)
            else:
                logger.exception("Error no controlado:", exc_info=error)
                await ctx.send(tr("err_unknown", "🔧 Error inesperado."), delete_after=10)

    def _setup_help_command(self):

        CATEGORY_META = {
            "general": {"emoji": "📊", "color": discord.Color.from_rgb(79, 193, 255),
                        "cmds": ['serverinfo', 'botinfo', 'ping', 'userinfo']},
            "moderation": {"emoji": "🛡️", "color": discord.Color.from_rgb(231, 76, 60),
                           "cmds": ['warn', 'kick', 'mute', 'unmute', 'ban', 'unban', 'clear']},
            "fun": {"emoji": "🎮", "color": discord.Color.from_rgb(241, 196, 15),
                    "cmds": ['8ball', 'coinflip', 'dice', 'cat']},
            "utility": {"emoji": "🛠️", "color": discord.Color.from_rgb(124, 92, 255),
                        "cmds": ['avatar', 'sponsor', 'soporte', 'help']},
        }

        COMMAND_EMOJIS = {
            'serverinfo': '🖥️', 'botinfo': '🤖', 'ping': '🏓', 'userinfo': '👤',
            'warn': '⚠️', 'kick': '👢', 'mute': '🔇', 'unmute': '🔊', 'ban': '🔨',
            'unban': '🔓', 'clear': '🧹', '8ball': '🎱', 'coinflip': '🪙',
            'dice': '🎲', 'cat': '🐱', 'avatar': '🖼️', 'sponsor': '✨',
            'soporte': '❓', 'help': '📖',
        }

        def cat_name(key): return tr(f"cat_{key}_name", key)
        def cat_desc(key): return tr(f"cat_{key}_desc", "")

        bot_ref = self.bot

        def build_home_embed():
            disabled = config_data.get("disabled_commands", [])
            total = sum(1 for m in CATEGORY_META.values() for c in m.get("cmds", []) if c not in disabled)
            embed = discord.Embed(
                title=tr("help_title", "🛸 Ayuda 🚀"),
                description=tr("help_desc", "Prefijo `/` — Comandos: `{n}`").format(n=total),
                color=discord.Color.from_rgb(65, 105, 225))
            if bot_ref.user and bot_ref.user.display_avatar:
                embed.set_thumbnail(url=bot_ref.user.display_avatar.url)
            for key, meta in CATEGORY_META.items():
                cnt = sum(1 for c in meta.get("cmds", []) if c not in disabled)
                embed.add_field(
                    name=f"{meta['emoji']}  {cat_name(key)}",
                    value=f"{cat_desc(key)}\n`{cnt}` {tr('help_cmds_available', 'comando(s)')}",
                    inline=False)
            embed.set_footer(text=build_footer() + " | " + tr("help_footer", "Usa el menú"))
            embed.timestamp = datetime.utcnow()
            return embed

        def build_category_embed(cat_key):
            meta = CATEGORY_META[cat_key]
            disabled = config_data.get("disabled_commands", [])
            names = [c for c in meta.get("cmds", []) if c not in disabled]
            embed = discord.Embed(
                title=f"{meta['emoji']}  {cat_name(cat_key)}",
                description=f"*{cat_desc(cat_key)}*",
                color=meta["color"])
            if bot_ref.user and bot_ref.user.display_avatar:
                embed.set_thumbnail(url=bot_ref.user.display_avatar.url)
            if not names:
                embed.add_field(name=tr("help_empty_title", "Nada"), value=tr("help_empty_desc", "Sin comandos"), inline=False)
            for cname in names:
                cmd = bot_ref.get_command(cname)
                if cmd:
                    icon = COMMAND_EMOJIS.get(cname, "▫️")
                    fallback = cmd.short_doc or cmd.help or tr("help_no_desc", "Sin descripción")
                    desc = tr(f"cmd_{cname}_desc", fallback)
                    embed.add_field(name=f"{icon}  `/{cmd.name}`", value=desc, inline=False)
            embed.set_footer(text=build_footer())
            embed.timestamp = datetime.utcnow()
            return embed

        class HelpSelect(discord.ui.Select):
            def __init__(self):
                options = [discord.SelectOption(
                    label=tr("help_opt_home", "🏠 Inicio"), value="__home__",
                    description=tr("help_opt_home_desc", "Menú"), emoji="🏠"
                )] + [discord.SelectOption(
                    label=cat_name(k), value=k, description=cat_desc(k)[:100], emoji=m["emoji"]
                ) for k, m in CATEGORY_META.items()]
                super().__init__(placeholder=tr("help_placeholder", "🔎 Elige categoría..."),
                                 min_values=1, max_values=1, options=options)

            async def callback(self, interaction):
                v = self.values[0]
                e = build_home_embed() if v == "__home__" else build_category_embed(v)
                await interaction.response.edit_message(embed=e)

        class HelpView(discord.ui.View):
            def __init__(self, invite_link):
                super().__init__(timeout=120)
                self.add_item(HelpSelect())
                if invite_link:
                    self.add_item(discord.ui.Button(label=tr("help_btn_invite", "Añadir"),
                                                    emoji="➕", style=discord.ButtonStyle.link, url=invite_link))
                support = os.getenv("SUPPORT_SERVER_INVITE", "https://discord.gg/eBszxvAuhN")
                self.add_item(discord.ui.Button(label=tr("help_btn_support", "Soporte"),
                                                emoji="❓", style=discord.ButtonStyle.link, url=support))

        @self.bot.hybrid_command(name='help', aliases=['ayuda', 'h'],
                                 help="Menú de ayuda.", short_doc="Menú de ayuda.")
        async def help_command(ctx):
            cid = config_data.get("client_id") or (self.bot.user.id if self.bot.user else None)
            invite = (f"https://discord.com/api/oauth2/authorize?client_id={cid}"
                      f"&permissions=8&scope=bot%20applications.commands") if cid else None
            await ctx.send(embed=build_home_embed(), view=HelpView(invite))

    def _setup_general_commands(self):

        @self.bot.hybrid_command(name='serverinfo', help="Info servidor.", short_doc="Info servidor.")
        @commands.guild_only()
        async def serverinfo(ctx):
            g = ctx.guild
            embed = discord.Embed(
                title=tr("cmd_serverinfo_title", "🖥️ Servidor: {name}").format(name=g.name),
                description=f"🆔 `{g.id}`",
                color=discord.Color.blue())
            if g.icon: embed.set_thumbnail(url=g.icon.url)
            embed.add_field(name=tr("cmd_serverinfo_owner", "👑 Propietario"),
                            value=g.owner.mention if g.owner else "N/D", inline=True)
            embed.add_field(name=tr("cmd_serverinfo_members", "👥 Miembros"),
                            value=str(g.member_count or "N/D"), inline=True)
            embed.add_field(name=tr("cmd_serverinfo_creation", "📅 Creación"),
                            value=discord.utils.format_dt(g.created_at, style='R'), inline=False)
            embed.add_field(name=tr("cmd_serverinfo_channels", "📊 Canales"),
                            value=f"T:{len(g.text_channels)} V:{len(g.voice_channels)} C:{len(g.categories)}", inline=True)
            embed.add_field(name=tr("cmd_serverinfo_roles", "📜 Roles"), value=str(len(g.roles)), inline=True)
            embed.add_field(name=tr("cmd_serverinfo_content", "🎨 Contenido"),
                            value=f"E:{len(g.emojis)} S:{len(g.stickers)}", inline=True)
            embed.set_footer(text=build_footer() + " | " + tr("footer_requested_by", "Por {name}").format(name=ctx.author.display_name))
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)

        @self.bot.hybrid_command(name='botinfo', help="Info bot.", short_doc="Info bot.")
        async def botinfo(ctx):
            try:
                p = psutil.Process(os.getpid())
                cpu = psutil.cpu_percent(interval=0.1)
                rss = p.memory_info().rss / (1024 * 1024)
                rp = p.memory_percent()
                th = p.num_threads()
            except Exception:
                cpu, rss, rp, th = ("N/D",) * 4
            embed = discord.Embed(
                title=tr("cmd_botinfo_title", "🤖 AstroBot (v{ver})").format(ver=__version__),
                description=tr("cmd_botinfo_desc", "Por **{author}**.").format(author=__author__),
                color=discord.Color.green())
            if self.bot.user and self.bot.user.display_avatar:
                embed.set_thumbnail(url=self.bot.user.display_avatar.url)
            embed.add_field(name="🐍 Python", value=f"`{platform.python_version()}`", inline=True)
            embed.add_field(name="📚 discord.py", value=f"`{discord.__version__}`", inline=True)
            embed.add_field(name=tr("cmd_botinfo_uptime", "⏳ Uptime"), value=self.get_uptime(), inline=True)
            embed.add_field(name=tr("cmd_botinfo_latency", "📡 Latencia"), value=f"{round(self.bot.latency * 1000)} ms", inline=True)
            embed.add_field(name="📊 CPU", value=f"{cpu}%", inline=True)
            embed.add_field(name="💾 RAM", value=f"{rss:.1f} MB ({rp:.1f}%)", inline=True)
            embed.add_field(name="🧵 Hilos", value=str(th), inline=True)
            embed.add_field(name=tr("cmd_botinfo_servers", "🌐 Servidores"), value=str(len(self.bot.guilds)), inline=True)
            try:
                uc = sum(g.member_count for g in self.bot.guilds if g.member_count)
            except Exception:
                uc = "N/D"
            embed.add_field(name=tr("cmd_botinfo_users", "👥 Usuarios"), value=str(uc), inline=True)
            embed.set_footer(text=build_footer() + " | " + tr("cmd_botinfo_footer", "© {year} | PID: {pid}").format(year=__year__, pid=os.getpid()))
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)

        @self.bot.hybrid_command(name='ping', help="Latencia.", short_doc="Latencia.")
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def ping(ctx):
            t0 = time.monotonic()
            msg = await ctx.send(tr("cmd_ping_calculating", "📡 Calculando..."))
            t1 = time.monotonic()
            rl = round((t1 - t0) * 1000)
            al = round(self.bot.latency * 1000)
            embed = discord.Embed(title=tr("cmd_ping_pong", "🏓 ¡Pong!"), color=discord.Color.blurple())
            embed.add_field(name=tr("cmd_ping_response", "⚡ Respuesta"), value=f"`{rl} ms`", inline=True)
            embed.add_field(name=tr("cmd_ping_api", "🌐 API"), value=f"`{al} ms`", inline=True)
            embed.set_footer(text=build_footer() + " | " + tr("cmd_ping_stable", "Estable!"))
            await msg.edit(content=None, embed=embed)

        @self.bot.hybrid_command(name='soporte', help="Soporte.", short_doc="Soporte.")
        async def soporte(ctx):
            link = os.getenv("SUPPORT_SERVER_INVITE", "https://discord.gg/eBszxvAuhN")
            embed = discord.Embed(
                title=tr("cmd_support_title", "🔧 Soporte"),
                description=tr("cmd_support_desc", "Únete: [Clic]({link})").format(link=link),
                color=discord.Color.gold())
            embed.set_footer(text=build_footer() + " | " + tr("cmd_support_footer", "¡Te esperamos!"))
            await ctx.send(embed=embed)

        @self.bot.hybrid_command(name='userinfo', aliases=['ui', 'whois'], help="Info usuario.", short_doc="Info usuario.")
        async def userinfo(ctx, *, user_resolvable: Optional[Union[discord.Member, discord.User]] = None):
            u = user_resolvable or ctx.author
            is_m = isinstance(u, discord.Member)
            status_emoji = {"online": "🟢", "idle": "🟡", "dnd": "🔴", "offline": "⚫", "invisible": "⚪"}
            st = status_emoji.get(str(u.status), "❓") if is_m else "❓"
            color = u.color if (is_m and u.color != discord.Color.default()) else discord.Color.light_grey()
            embed = discord.Embed(
                title=tr("cmd_userinfo_title", "{status} Usuario: {name}").format(status=st, name=u.display_name),
                description=tr("cmd_userinfo_desc", "**ID:** `{id}` | **Mención:** {mention}").format(id=u.id, mention=u.mention),
                color=color)
            if u.display_avatar: embed.set_thumbnail(url=u.display_avatar.url)
            embed.add_field(name=tr("cmd_userinfo_username", "🏷️ Usuario"), value=f"`{u.name}`", inline=True)
            embed.add_field(name=tr("cmd_userinfo_isbot", "🤖 Bot?"),
                            value=tr("yes", "Sí") if u.bot else tr("no", "No"), inline=True)
            embed.add_field(name=tr("cmd_userinfo_created", "📅 Cuenta"),
                            value=discord.utils.format_dt(u.created_at, style='R'), inline=False)
            if is_m:
                embed.add_field(name=tr("cmd_userinfo_joined", "📥 Se unió"),
                                value=discord.utils.format_dt(u.joined_at, style='R'), inline=False)
                roles = [r.mention for r in reversed(u.roles[1:])]
                rs = ", ".join(roles) if roles else tr("none", "Ninguno")
                if len(rs) > 1020: rs = f"{len(roles)} roles"
                embed.add_field(name=tr("cmd_userinfo_roles", "📜 Roles ({n})").format(n=len(roles)), value=rs, inline=False)
            embed.set_footer(text=build_footer() + " | " + tr("footer_requested_by", "Por {name}").format(name=ctx.author.display_name))
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)

    def _setup_moderation_commands(self):

        async def dm(member, gname, title, details, color):
            try:
                e = discord.Embed(title=tr("mod_dm_title", "{title} en '{guild}'").format(title=title, guild=gname),
                                  description=details, color=color)
                e.timestamp = datetime.utcnow()
                await member.send(embed=e)
            except Exception as ex:
                logger.warning(f"No se pudo enviar MD a {member}: {ex}")

        def h_user(ctx, m):
            if ctx.author == ctx.guild.owner: return True
            if m == ctx.guild.owner: return False
            if not ctx.author.top_role or not m.top_role: return False
            return ctx.author.top_role > m.top_role

        def h_bot(ctx, m):
            if m == ctx.guild.owner: return False
            if not ctx.guild.me.top_role or not m.top_role: return False
            return ctx.guild.me.top_role > m.top_role

        @self.bot.hybrid_command(name='warn', help="Advierte.", short_doc="Advierte.")
        @commands.has_permissions(kick_members=True)
        @commands.bot_has_permissions(send_messages=True, embed_links=True)
        @commands.guild_only()
        async def warn(ctx, member: discord.Member, *, reason: str = None):
            reason = reason or tr("mod_default_reason", "No especificada")
            if member == ctx.author:
                await ctx.send("⚠️ No puedes advertirte.", delete_after=10); return
            if member.bot:
                await ctx.send("⚠️ No a bots.", delete_after=10); return
            if not h_user(ctx, member):
                await ctx.send("⛔ Jerarquía.", delete_after=10); return
            embed = discord.Embed(
                title="⚠️ Advertencia",
                description=f"**Usuario:** {member.mention}\n**Mod:** {ctx.author.mention}\n**Razón:** {reason}",
                color=discord.Color.orange())
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)
            await dm(member, ctx.guild.name, "Advertencia", f"En **{ctx.guild.name}**.\n**Razón:** {reason}", discord.Color.orange())

        @self.bot.hybrid_command(name='kick', help="Expulsa.", short_doc="Expulsa.")
        @commands.has_permissions(kick_members=True)
        @commands.bot_has_permissions(kick_members=True, send_messages=True, embed_links=True)
        @commands.guild_only()
        async def kick(ctx, member: discord.Member, *, reason: str = None):
            reason = reason or tr("mod_default_reason", "No especificada")
            if member == ctx.author:
                await ctx.send("⚠️ No te expulsas.", delete_after=10); return
            if not h_user(ctx, member) or not h_bot(ctx, member):
                await ctx.send("⛔ Jerarquía.", delete_after=10); return
            await dm(member, ctx.guild.name, "Expulsado", f"**Razón:** {reason}", discord.Color.red())
            try:
                await member.kick(reason=f"Por {ctx.author.name}: {reason}")
                embed = discord.Embed(
                    title="👢 Expulsado",
                    description=f"**Usuario:** {member.mention}\n**Mod:** {ctx.author.mention}\n**Razón:** {reason}",
                    color=discord.Color.red())
                embed.timestamp = datetime.utcnow()
                await ctx.send(embed=embed)
            except discord.Forbidden:
                await ctx.send("❌ Sin permisos.", delete_after=10)

        @self.bot.hybrid_command(name='mute', aliases=['timeout'], help="Timeout.", short_doc="Timeout.")
        @commands.has_permissions(moderate_members=True)
        @commands.bot_has_permissions(moderate_members=True, send_messages=True, embed_links=True)
        @commands.guild_only()
        async def mute(ctx, member: discord.Member, duration_minutes: int, *, reason: str = None):
            reason = reason or tr("mod_default_reason", "No especificada")
            if member == ctx.author:
                await ctx.send("⚠️", delete_after=10); return
            if not h_user(ctx, member) or not h_bot(ctx, member):
                await ctx.send("⛔ Jerarquía.", delete_after=10); return
            if member.is_timed_out():
                await ctx.send("⚠️ Ya silenciado.", delete_after=10); return
            if duration_minutes <= 0 or duration_minutes > 40320:
                await ctx.send("❌ 1-40320 min.", delete_after=10); return
            try:
                delta = timedelta(minutes=duration_minutes)
                await member.timeout(delta, reason=f"Por {ctx.author.name}: {reason}")
                end = discord.utils.utcnow() + delta
                embed = discord.Embed(
                    title="🔇 Silenciado",
                    description=f"**Usuario:** {member.mention}\n**Duración:** {duration_minutes} min\n**Fin:** {discord.utils.format_dt(end, style='R')}\n**Razón:** {reason}",
                    color=discord.Color.dark_grey())
                embed.timestamp = datetime.utcnow()
                await ctx.send(embed=embed)
            except discord.Forbidden:
                await ctx.send("❌ Sin permisos.", delete_after=10)

        @self.bot.hybrid_command(name='unmute', aliases=['untimeout'], help="Quita timeout.", short_doc="Quita timeout.")
        @commands.has_permissions(moderate_members=True)
        @commands.bot_has_permissions(moderate_members=True, send_messages=True, embed_links=True)
        @commands.guild_only()
        async def unmute(ctx, member: discord.Member, *, reason: str = "OK"):
            if not member.is_timed_out():
                await ctx.send("✅ No está silenciado.", delete_after=10); return
            try:
                await member.timeout(None, reason=f"Por {ctx.author.name}: {reason}")
                embed = discord.Embed(title="🔊 Habla de nuevo",
                                      description=f"**Usuario:** {member.mention}\n**Mod:** {ctx.author.mention}",
                                      color=discord.Color.green())
                embed.timestamp = datetime.utcnow()
                await ctx.send(embed=embed)
            except discord.Forbidden:
                await ctx.send("❌ Sin permisos.", delete_after=10)

        @self.bot.hybrid_command(name='ban', help="Banea.", short_doc="Banea.")
        @commands.has_permissions(ban_members=True)
        @commands.bot_has_permissions(ban_members=True, send_messages=True, embed_links=True)
        @commands.guild_only()
        async def ban(ctx, user_resolvable: Union[discord.Member, discord.User],
                      delete_message_days: Optional[int] = 0, *, reason: str = None):
            reason = reason or tr("mod_default_reason", "No especificada")
            target = user_resolvable
            if isinstance(target, discord.Member):
                if target == ctx.author:
                    await ctx.send("⚠️", delete_after=10); return
                if not h_user(ctx, target) or not h_bot(ctx, target):
                    await ctx.send("⛔ Jerarquía.", delete_after=10); return
            if not (0 <= delete_message_days <= 7):
                await ctx.send("❌ 0-7 días.", delete_after=10); return
            await dm(target, ctx.guild.name, "Baneado", f"**Razón:** {reason}", discord.Color.dark_red())
            try:
                await ctx.guild.ban(target, reason=f"Por {ctx.author.name}: {reason}",
                                    delete_message_seconds=delete_message_days * 86400)
                embed = discord.Embed(title="🔨 Baneado",
                                      description=f"**Usuario:** {target.mention}\n**Mod:** {ctx.author.mention}\n**Razón:** {reason}",
                                      color=discord.Color.dark_red())
                embed.timestamp = datetime.utcnow()
                await ctx.send(embed=embed)
            except discord.Forbidden:
                await ctx.send("❌ Sin permisos.", delete_after=10)

        @self.bot.hybrid_command(name='unban', help="Desbanea.", short_doc="Desbanea.")
        @commands.has_permissions(ban_members=True)
        @commands.bot_has_permissions(ban_members=True, send_messages=True, embed_links=True)
        @commands.guild_only()
        async def unban(ctx, user_id: str, *, reason: str = "OK"):
            try:
                u = discord.Object(id=user_id)
                try:
                    b = await ctx.guild.fetch_ban(u); u = b.user
                except discord.NotFound:
                    await ctx.send(f"❌ `{user_id}` no baneado."); return
                await ctx.guild.unban(u, reason=f"Por {ctx.author.name}: {reason}")
                embed = discord.Embed(title="🔓 Desbaneado",
                                      description=f"**Usuario:** {u.mention}\n**Mod:** {ctx.author.mention}",
                                      color=discord.Color.teal())
                embed.timestamp = datetime.utcnow()
                await ctx.send(embed=embed)
            except discord.Forbidden:
                await ctx.send("❌ Sin permisos.", delete_after=10)

        @self.bot.hybrid_command(name='clear', aliases=['purge'], help="Borra.", short_doc="Borra max 100.")
        @commands.has_permissions(manage_messages=True)
        @commands.bot_has_permissions(manage_messages=True, read_message_history=True, send_messages=True)
        @commands.guild_only()
        async def clear(ctx, amount: int, member_filter: Optional[discord.Member] = None):
            if amount <= 0:
                await ctx.send("❌ >0.", delete_after=10); return
            limit = min(amount, 100)
            try:
                await ctx.message.delete()
            except Exception:
                pass
            try:
                if member_filter:
                    deleted = await ctx.channel.purge(limit=limit, check=lambda m: m.author == member_filter)
                else:
                    deleted = await ctx.channel.purge(limit=limit)
                await ctx.send(f"🗑️ `{len(deleted)}` borrados.", delete_after=5)
            except discord.Forbidden:
                await ctx.send("❌ Sin permisos.", delete_after=10)

    def _setup_fun_commands(self):

        @self.bot.hybrid_command(name='8ball', aliases=['bola8'], help="Bola 8.", short_doc="Bola 8.")
        @commands.cooldown(1, 3, commands.BucketType.user)
        async def eight_ball(ctx, *, question: str):
            if len(question) < 5 or not question.endswith("?"):
                await ctx.send("🤔 Necesita `?`.", delete_after=10); return
            responses = tr("8ball_responses", None) or [
                "🟢 Sí.", "🟢 Sin duda.", "🟢 Definitivamente.", "🟢 Probable.",
                "🟡 Pregunta de nuevo.", "🟡 No puedo ahora.",
                "🔴 No.", "🔴 Muy dudoso."]
            chosen = random.choice(responses)
            color = discord.Color.greyple()
            if chosen.startswith("🟢"): color = discord.Color.green()
            elif chosen.startswith("🟡"): color = discord.Color.gold()
            elif chosen.startswith("🔴"): color = discord.Color.red()
            embed = discord.Embed(title=tr("8ball_title", "🎱 Bola 8"), color=color)
            embed.add_field(name=ctx.author.display_name, value=question, inline=False)
            embed.add_field(name=tr("8ball_answer", "Respuesta:"), value=chosen[2:], inline=False)
            await ctx.send(embed=embed)

        @self.bot.hybrid_command(name='coinflip', aliases=['moneda', 'flip'], help="Moneda.", short_doc="Moneda.")
        @commands.cooldown(1, 2, commands.BucketType.user)
        async def coinflip(ctx):
            heads = tr("coinflip_heads", "Cara")
            r = random.choice([heads, tr("coinflip_tails", "Cruz")])
            color = discord.Color.gold() if r == heads else discord.Color.dark_grey()
            embed = discord.Embed(
                title=tr("coinflip_title", "🪙 Moneda"),
                description=tr("coinflip_result", "¡**{r}**!").format(r=r),
                color=color)
            await ctx.send(embed=embed)

        @self.bot.hybrid_command(name='dice', aliases=['dado', 'roll'], help="Dados.", short_doc="Dados.")
        @commands.cooldown(1, 2, commands.BucketType.user)
        async def dice(ctx, dice_notation: str = "1d6"):
            try:
                nd_s, ns_s = dice_notation.lower().split('d')
                nd = int(nd_s) if nd_s else 1
                ns = int(ns_s)
                if not (1 <= nd <= 25) or not (2 <= ns <= 1000):
                    await ctx.send("❌ 1-25 dados, 2-1000 caras.", delete_after=10); return
                rolls = [random.randint(1, ns) for _ in range(nd)]
                embed = discord.Embed(title=f"🎲 {nd}d{ns}", description=f"**Suma:** {sum(rolls)}", color=discord.Color.red())
                if 1 < nd <= 15:
                    embed.add_field(name="Resultados", value=", ".join(map(str, rolls))[:1000], inline=False)
                await ctx.send(embed=embed)
            except (ValueError, IndexError):
                await ctx.send("❌ Formato `NdS`.", delete_after=10)

        @self.bot.hybrid_command(name='cat', aliases=['gato', 'meow'], help="Gato.", short_doc="Gato.")
        @commands.cooldown(1, 4, commands.BucketType.channel)
        async def cat(ctx):
            try:
                async with ctx.typing():
                    r = await asyncio.get_event_loop().run_in_executor(
                        None, lambda: requests.get('https://api.thecatapi.com/v1/images/search', timeout=10))
                    r.raise_for_status()
                    data = r.json()
                if data and isinstance(data, list) and data[0].get('url'):
                    embed = discord.Embed(title="🐱 ¡Miau!", color=discord.Color.random())
                    embed.set_image(url=data[0]['url'])
                    embed.set_footer(text=build_footer())
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("😿 Sin imagen.", delete_after=10)
            except Exception as e:
                await ctx.send(f"❌ Error: {e}", delete_after=10)

    def _setup_utility_commands(self):

        @self.bot.hybrid_command(name='avatar', aliases=['av', 'pfp'], help="Avatar.", short_doc="Avatar.")
        async def avatar(ctx, *, user_resolvable: Optional[Union[discord.Member, discord.User]] = None):
            u = user_resolvable or ctx.author
            if not u.display_avatar:
                await ctx.send("Sin avatar."); return
            url = u.display_avatar.with_size(1024).url
            color = u.color if (isinstance(u, discord.Member) and u.color != discord.Color.default()) else discord.Color.blurple()
            embed = discord.Embed(
                title=tr("cmd_avatar_title", "🖼️ Avatar de {name}").format(name=u.display_name),
                color=color)
            embed.set_image(url=url)
            embed.description = tr("avatar_direct_link", "[Enlace]({url})").format(url=url)
            await ctx.send(embed=embed)

    @tasks.loop(minutes=10)
    async def change_status_task(self):
        await self.bot.wait_until_ready()
        try:
            t = config_data.get("activity_type", "playing").lower()
            n = config_data.get("activity_name", "AstroBot V3")
            at = discord.ActivityType.playing
            if t == "watching": at = discord.ActivityType.watching
            elif t == "listening": at = discord.ActivityType.listening
            elif t == "competing": at = discord.ActivityType.competing
            await self.bot.change_presence(activity=discord.Activity(type=at, name=n), status=discord.Status.online)
        except Exception as e:
            self.log(f"Error cambiando estado: {e}", level="error")

    def _setup_sponsor_commands(self):
        @self.bot.hybrid_command(name='sponsor', aliases=['astro', 'premium'], help="Sponsor.")
        async def sponsor(ctx):
            embed = discord.Embed(
                title=tr("sponsor_title", "✨ AstroSoftware ✨"),
                description=tr("sponsor_desc", "¡Únete!"),
                color=discord.Color.gold())
            embed.add_field(name=tr("sponsor_links_field", "🔗 Enlaces"),
                            value=f"[{tr('sponsor_join', 'Únete')}]({config_data.get('spam_link', '')})")
            embed.set_footer(text=build_footer())
            if ctx.guild and ctx.guild.icon:
                embed.set_thumbnail(url=ctx.guild.icon.url)
            try:
                view = discord.ui.View()
                view.add_item(discord.ui.Button(label=tr("sponsor_join_btn", "¡Unirse!"),
                                                url=config_data.get('spam_link', ''),
                                                style=discord.ButtonStyle.link, emoji="🚀"))
                await ctx.send(embed=embed, view=view)
            except Exception:
                await ctx.send(embed=embed)

    def run(self):
        try:
            self.bot.run(self.token, log_handler=None)
        except Exception as e:
            self.log(f"Error crítico al ejecutar el bot: {e}", level="critical")

    async def stop_bot_async(self):
        self.running = False
        if self.change_status_task.is_running():
            self.change_status_task.cancel()
        await self.bot.close()
        self.log("Bot desconectado correctamente.", level="info")


class BotGUI(customtkinter.CTk):
    ACCENT = "#7C5CFF"; ACCENT_HOVER = "#6647E0"
    SUCCESS = "#2ECC71"; SUCCESS_HOVER = "#27AE60"
    DANGER = "#E74C3C"; DANGER_HOVER = "#C0392B"
    WARNING = "#F1C40F"; INFO = "#4FC1FF"; INFO_HOVER = "#3AA8DE"
    MUTED = "#5A5D70"; CARD_BG = "#1E1F29"
    SIDEBAR_BG = "#15161E"; TEXT_MUTED = "#9A9DB0"

    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        self.config = load_config()
        self.bot_instance: Optional[AdvancedAstroBot] = None
        self.bot_thread: Optional[threading.Thread] = None
        self.command_switches = {}
        self.cmd_rows = []
        self._nav_buttons = {}
        self.pages = {}

        self.bot_token_var = tk.StringVar(value=self.config.get("token", ""))
        self.spam_link_var = tk.StringVar(value=self.config.get("spam_link", ""))
        self.spam_name_var = tk.StringVar(value=self.config.get("spam_name", ""))
        self.act_type_var = tk.StringVar(value=self.config.get("activity_type", "playing"))
        self.act_name_var = tk.StringVar(value=self.config.get("activity_name", "AstroBot V3"))
        self.client_id_var = tk.StringVar(value=self.config.get("client_id", ""))
        self.language_var = tk.StringVar(value=self.config.get("language", "es"))
        self.cmd_search_var = tk.StringVar()

        self._update_window_title()
        self.geometry("1150x760")
        self.minsize(1000, 640)
        self.configure(fg_color="#0E0F16")
        if os.path.exists("asbotlogo.ico"):
            try:
                self.iconbitmap("asbotlogo.ico")
            except Exception:
                pass

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._build_sidebar()
        self._build_main_area()

        self._build_dashboard_page()
        self._build_settings_page()
        self._build_commands_page()
        self._build_logs_page()
        self._build_about_page()

        self.show_page("dashboard")
        self.check_log_queue_periodically()
        self.refresh_stats_loop()
        self.protocol("WM_DELETE_WINDOW", self.on_closing_application)

    def _update_window_title(self):
        sub = tr("sidebar_subtitle", "Panel de Control")
        self.title(f"AstroSoftware · {sub} AstroBot v{__version__}")

    def _build_sidebar(self):
        self.sidebar_frame = customtkinter.CTkFrame(self, width=230, corner_radius=0, fg_color=self.SIDEBAR_BG)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_propagate(False)
        self.sidebar_frame.grid_columnconfigure(0, weight=1)

        customtkinter.CTkLabel(self.sidebar_frame, text=tr("sidebar_title", "🛰️  AstroBot"),
                               font=("Segoe UI Variable", 22, "bold"), text_color=self.ACCENT
                               ).grid(row=0, column=0, padx=22, pady=(28, 2), sticky="w")

        self.sidebar_subtitle_label = customtkinter.CTkLabel(
            self.sidebar_frame, text=f"{tr('sidebar_subtitle', 'Panel')} · v{__version__}",
            font=("Segoe UI Variable", 11), text_color=self.TEXT_MUTED)
        self.sidebar_subtitle_label.grid(row=1, column=0, padx=22, pady=(0, 26), sticky="w")

        nav_items = [
            ("dashboard", tr("nav_dashboard", "🏠   Panel")),
            ("settings", tr("nav_settings", "⚙️   Configuración")),
            ("commands", tr("nav_commands", "🧩   Comandos")),
            ("logs", tr("nav_logs", "📜   Registros")),
            ("about", tr("nav_about", "ℹ️   Acerca de")),
        ]
        self._nav_buttons = {}
        for i, (key, label) in enumerate(nav_items, start=2):
            btn = customtkinter.CTkButton(
                self.sidebar_frame, text=label, anchor="w", corner_radius=8, height=42,
                fg_color="transparent", hover_color="#23243a", text_color="#D6D8E4",
                font=("Segoe UI Variable", 13), command=lambda k=key: self.show_page(k))
            btn.grid(row=i, column=0, padx=14, pady=4, sticky="ew")
            self._nav_buttons[key] = btn

        self.sidebar_frame.grid_rowconfigure(len(nav_items) + 2, weight=1)
        customtkinter.CTkLabel(self.sidebar_frame, text=f"© {__year__} AstroSoftware",
                               font=("Segoe UI Variable", 10), text_color=self.MUTED
                               ).grid(row=len(nav_items) + 3, column=0, pady=(0, 18))

    def _build_main_area(self):
        self.main_container = customtkinter.CTkFrame(self, fg_color="transparent")
        self.main_container.grid(row=0, column=1, sticky="nsew", padx=26, pady=26)
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)

    def show_page(self, key):
        for f in self.pages.values():
            f.grid_forget()
        if key in self.pages:
            self.pages[key].grid(row=0, column=0, sticky="nsew")
        for k, btn in self._nav_buttons.items():
            active = (k == key)
            btn.configure(
                fg_color=self.ACCENT if active else "transparent",
                text_color="#FFFFFF" if active else "#D6D8E4",
                hover_color=self.ACCENT_HOVER if active else "#23243a")

    def _build_dashboard_page(self):
        page = customtkinter.CTkFrame(self.main_container, fg_color="transparent")
        self.pages["dashboard"] = page
        page.grid_columnconfigure((0, 1, 2), weight=1)

        header = customtkinter.CTkFrame(page, fg_color=self.CARD_BG, corner_radius=14)
        header.grid(row=0, column=0, columnspan=3, sticky="ew", pady=(0, 18))
        header.grid_columnconfigure(0, weight=1)

        customtkinter.CTkLabel(header, text=tr("title_dashboard_full", "🌌 Panel"),
                               font=("Segoe UI Variable", 24, "bold")
                               ).grid(row=0, column=0, padx=22, pady=(18, 4), sticky="w")
        customtkinter.CTkLabel(header, text=tr("desc_dashboard", "Gestión."),
                               font=("Segoe UI Variable", 12), text_color=self.TEXT_MUTED
                               ).grid(row=1, column=0, padx=22, pady=(0, 18), sticky="w")

        is_run = bool(self.bot_instance and self.bot_instance.running)
        stxt = tr("status_connected", "🟢  Conectado") if is_run else tr("status_stopped", "●  Detenido")
        scol = self.SUCCESS if is_run else self.DANGER

        self.status_label = customtkinter.CTkLabel(header, text=stxt,
                                                   font=("Segoe UI Variable", 15, "bold"), text_color=scol)
        self.status_label.grid(row=0, column=1, rowspan=2, padx=22)

        btn_row = customtkinter.CTkFrame(page, fg_color="transparent")
        btn_row.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(0, 18))

        self.start_button = customtkinter.CTkButton(
            btn_row, text=tr("btn_start_bot", "🚀 Iniciar"), command=self.start_bot_thread,
            height=42, width=150, fg_color=self.SUCCESS, hover_color=self.SUCCESS_HOVER,
            font=("Segoe UI Variable", 13, "bold"), state="disabled" if is_run else "normal")
        self.start_button.pack(side="left", padx=(0, 10))

        self.stop_button = customtkinter.CTkButton(
            btn_row, text=tr("btn_stop_bot", "🛑 Detener"), command=self.stop_bot_thread,
            state="normal" if is_run else "disabled", height=42, width=150,
            fg_color=self.DANGER, hover_color=self.DANGER_HOVER,
            font=("Segoe UI Variable", 13, "bold"))
        self.stop_button.pack(side="left", padx=10)

        customtkinter.CTkButton(btn_row, text=tr("btn_invite", "🔗 Invitar"),
                                command=self.open_invite_link, height=42, width=150,
                                fg_color=self.INFO, hover_color=self.INFO_HOVER).pack(side="left", padx=10)
        customtkinter.CTkButton(btn_row, text=tr("btn_support", "❓ Soporte"),
                                command=lambda: webbrowser.open_new_tab("https://discord.gg/v7DqaMN9yM"),
                                height=42, width=130, fg_color="#5BC0DE", hover_color="#489FBD"
                                ).pack(side="left", padx=10)

        self.stat_labels = {}
        stats = [
            ("servers", "🌐", tr("stat_servers", "Servidores")),
            ("users", "👥", tr("stat_users", "Usuarios")),
            ("latency", "📡", tr("stat_latency", "Latencia")),
            ("uptime", "⏳", tr("stat_uptime", "Uptime")),
            ("cpu", "🧠", tr("stat_cpu", "CPU")),
            ("ram", "💾", tr("stat_ram", "RAM")),
        ]
        for i, (key, icon, label) in enumerate(stats):
            row, col = 2 + i // 3, i % 3
            card = customtkinter.CTkFrame(page, fg_color=self.CARD_BG, corner_radius=14)
            card.grid(row=row, column=col, sticky="nsew", padx=8, pady=8)
            page.grid_rowconfigure(row, weight=1)
            card.grid_columnconfigure(1, weight=1)
            customtkinter.CTkLabel(card, text=icon, font=("Segoe UI Variable", 24)
                                   ).grid(row=0, column=0, padx=(18, 10), pady=18)
            tf = customtkinter.CTkFrame(card, fg_color="transparent")
            tf.grid(row=0, column=1, sticky="w", pady=18)
            customtkinter.CTkLabel(tf, text=label, font=("Segoe UI Variable", 11),
                                   text_color=self.TEXT_MUTED).pack(anchor="w")
            vl = customtkinter.CTkLabel(tf, text="—", font=("Segoe UI Variable", 19, "bold"))
            vl.pack(anchor="w")
            self.stat_labels[key] = vl

        log_card = customtkinter.CTkFrame(page, fg_color=self.CARD_BG, corner_radius=14)
        log_card.grid(row=4, column=0, columnspan=3, sticky="nsew", pady=(10, 0))
        page.grid_rowconfigure(4, weight=2)
        customtkinter.CTkLabel(log_card, text=tr("recent_activity", "📜 Actividad"),
                               font=("Segoe UI Variable", 14, "bold")).pack(anchor="w", padx=18, pady=(14, 6))
        self.log_area = customtkinter.CTkTextbox(log_card, wrap="word", state="disabled",
                                                 font=("Cascadia Code", 12), fg_color="#101118", corner_radius=10)
        self.log_area.pack(padx=18, pady=(0, 18), fill="both", expand=True)

    def _build_settings_page(self):
        page = customtkinter.CTkScrollableFrame(self.main_container, fg_color="transparent")
        self.pages["settings"] = page

        customtkinter.CTkLabel(page, text=tr("title_settings_full", "⚙️ Configuración"),
                               font=("Segoe UI Variable", 24, "bold")).pack(anchor="w", pady=(0, 4))
        customtkinter.CTkLabel(page, text=tr("desc_settings", "Ajusta."),
                               font=("Segoe UI Variable", 12), text_color=self.TEXT_MUTED
                               ).pack(anchor="w", pady=(0, 18))

        def section(t):
            card = customtkinter.CTkFrame(page, fg_color=self.CARD_BG, corner_radius=14)
            card.pack(fill="x", pady=(0, 16))
            card.grid_columnconfigure(1, weight=1)
            customtkinter.CTkLabel(card, text=t, font=("Segoe UI Variable", 15, "bold"),
                                   text_color=self.ACCENT
                                   ).grid(row=0, column=0, columnspan=2, padx=20, pady=(16, 8), sticky="w")
            return card

        def field(card, row, label, var, show=None, width=380):
            customtkinter.CTkLabel(card, text=label, font=("Segoe UI Variable", 12)
                                   ).grid(row=row, column=0, padx=20, pady=8, sticky="w")
            customtkinter.CTkEntry(card, textvariable=var, width=width, show=show or ""
                                   ).grid(row=row, column=1, padx=20, pady=8, sticky="w")

        bot_card = section(tr("sec_credentials", "🔑 Credenciales"))
        field(bot_card, 1, tr("lbl_token", "Token:"), self.bot_token_var, show="*")
        field(bot_card, 2, tr("lbl_client_id", "Client ID:"), self.client_id_var, width=260)
        customtkinter.CTkLabel(bot_card, text=tr("desc_client_id", "Para invitar."),
                               font=("Segoe UI Variable", 10), text_color=self.TEXT_MUTED
                               ).grid(row=3, column=0, columnspan=2, padx=20, pady=(0, 14), sticky="w")

        promo_card = section(tr("sec_promo", "📣 Promoción"))
        field(promo_card, 1, tr("lbl_promo_link", "Link:"), self.spam_link_var)
        field(promo_card, 2, tr("lbl_promo_name", "Nombre:"), self.spam_name_var)
        customtkinter.CTkLabel(promo_card, text="", height=6).grid(row=3, column=0)

        lang_card = section(tr("lbl_language", "🌐 Idioma"))
        self.lang_option = customtkinter.CTkOptionMenu(
            lang_card, variable=self.language_var, values=["es", "en", "it"],
            fg_color=self.ACCENT, button_color=self.ACCENT_HOVER, button_hover_color=self.ACCENT_HOVER,
            command=self.refresh_language)
        self.lang_option.grid(row=1, column=0, padx=20, pady=8, sticky="w")

        presence_card = section(tr("sec_presence", "🎮 Presencia"))
        customtkinter.CTkLabel(presence_card, text=tr("lbl_act_type", "Tipo:"),
                               font=("Segoe UI Variable", 12)
                               ).grid(row=1, column=0, padx=20, pady=8, sticky="w")
        customtkinter.CTkOptionMenu(presence_card, variable=self.act_type_var,
                                    values=["playing", "watching", "listening", "competing"],
                                    fg_color=self.ACCENT, button_color=self.ACCENT_HOVER,
                                    button_hover_color=self.ACCENT_HOVER
                                    ).grid(row=1, column=1, padx=20, pady=8, sticky="w")
        field(presence_card, 2, tr("lbl_act_text", "Texto:"), self.act_name_var)
        customtkinter.CTkLabel(presence_card, text="", height=6).grid(row=3, column=0)

        customtkinter.CTkButton(page, text=tr("btn_save_settings", "💾 Guardar"),
                                command=self.save_settings, height=44, width=220,
                                fg_color=self.SUCCESS, hover_color=self.SUCCESS_HOVER,
                                font=("Segoe UI Variable", 13, "bold")).pack(pady=12)

    def _build_commands_page(self):
        page = customtkinter.CTkFrame(self.main_container, fg_color="transparent")
        self.pages["commands"] = page
        page.grid_columnconfigure(0, weight=1)
        page.grid_rowconfigure(3, weight=1)

        customtkinter.CTkLabel(page, text=tr("title_commands", "🧩 Comandos"),
                               font=("Segoe UI Variable", 24, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 4))
        customtkinter.CTkLabel(page, text=tr("desc_commands", "Activa/desactiva."),
                               font=("Segoe UI Variable", 12), text_color=self.TEXT_MUTED
                               ).grid(row=1, column=0, sticky="w", pady=(0, 14))

        customtkinter.CTkEntry(page, placeholder_text=tr("placeholder_search", "🔍 Buscar..."),
                               textvariable=self.cmd_search_var, width=320, height=36
                               ).grid(row=2, column=0, sticky="w", pady=(0, 12))
        self.cmd_search_var.trace_add("write", lambda *_: self._filter_commands())

        scroll = customtkinter.CTkScrollableFrame(page, fg_color=self.CARD_BG, corner_radius=14)
        scroll.grid(row=3, column=0, sticky="nsew")

        categories = {
            tr("cat_general_name", "📊 Info"): ['serverinfo', 'botinfo', 'ping', 'userinfo'],
            tr("cat_moderation_name", "🛡️ Mod"): ['warn', 'kick', 'mute', 'unmute', 'ban', 'unban', 'clear'],
            tr("cat_fun_name", "🎮 Fun"): ['8ball', 'coinflip', 'dice', 'cat'],
            tr("cat_utility_name", "🛠️ Utils"): ['avatar', 'sponsor', 'soporte'],
        }
        disabled = self.config.get("disabled_commands", [])
        row_i = 0
        self.cmd_rows = []
        for cat, cmds in categories.items():
            customtkinter.CTkLabel(scroll, text=cat, font=("Segoe UI Variable", 13, "bold"),
                                   text_color=self.ACCENT
                                   ).grid(row=row_i, column=0, columnspan=2, sticky="w", padx=16, pady=(16, 6))
            row_i += 1
            for idx, cmd in enumerate(cmds):
                var = tk.StringVar(value="off" if cmd in disabled else "on")
                sw = customtkinter.CTkSwitch(scroll, text=cmd, variable=var, onvalue="on",
                                             offvalue="off", progress_color=self.SUCCESS)
                sw.grid(row=row_i + idx // 2, column=idx % 2, padx=28, pady=6, sticky="w")
                self.command_switches[cmd] = var
                self.cmd_rows.append((cmd, sw))
            row_i += (len(cmds) + 1) // 2

        customtkinter.CTkButton(page, text=tr("btn_save_commands", "💾 Guardar"),
                                command=self.save_commands, height=42, width=220,
                                fg_color=self.SUCCESS, hover_color=self.SUCCESS_HOVER
                                ).grid(row=4, column=0, pady=14, sticky="w")

    def _filter_commands(self):
        q = self.cmd_search_var.get().lower().strip()
        for cmd, w in self.cmd_rows:
            (w.grid() if q in cmd.lower() else w.grid_remove())

    def _build_logs_page(self):
        page = customtkinter.CTkFrame(self.main_container, fg_color="transparent")
        self.pages["logs"] = page
        page.grid_columnconfigure(0, weight=1)
        page.grid_rowconfigure(1, weight=1)

        tb = customtkinter.CTkFrame(page, fg_color="transparent")
        tb.grid(row=0, column=0, sticky="ew", pady=(0, 12))
        customtkinter.CTkLabel(tb, text=tr("title_logs", "📜 Registros"),
                               font=("Segoe UI Variable", 24, "bold")).pack(side="left")
        customtkinter.CTkButton(tb, text=tr("btn_export", "💾 Exportar"), width=110,
                                command=self.export_logs, fg_color=self.INFO, hover_color=self.INFO_HOVER
                                ).pack(side="right", padx=(8, 0))
        customtkinter.CTkButton(tb, text=tr("btn_clear_view", "🧹 Limpiar"), width=130,
                                command=self.clear_logs_view, fg_color=self.MUTED).pack(side="right", padx=(8, 0))

        self.full_log_area = customtkinter.CTkTextbox(page, wrap="word", state="disabled",
                                                      font=("Cascadia Code", 12),
                                                      fg_color=self.CARD_BG, corner_radius=12)
        self.full_log_area.grid(row=1, column=0, sticky="nsew")

    def clear_logs_view(self):
        for w in (getattr(self, 'log_area', None), getattr(self, 'full_log_area', None)):
            if w and w.winfo_exists():
                w.configure(state="normal"); w.delete("1.0", "end"); w.configure(state="disabled")

    def export_logs(self):
        p = filedialog.asksaveasfilename(defaultextension=".txt",
                                         filetypes=[("Texto", "*.txt"), ("Todos", "*.*")],
                                         initialfile="astrobot_export.log")
        if not p: return
        try:
            with open(p, "w", encoding="utf-8") as f:
                f.write(self.full_log_area.get("1.0", "end"))
            messagebox.showinfo("OK", f"{tr('logs_exported_msg', 'Exportado: ')}{p}")
        except Exception as e:
            messagebox.showerror("Error", f"{tr('logs_export_err', 'Error: ')}{e}")

    def _build_about_page(self):
        page = customtkinter.CTkFrame(self.main_container, fg_color="transparent")
        self.pages["about"] = page
        card = customtkinter.CTkFrame(page, fg_color=self.CARD_BG, corner_radius=16)
        card.pack(fill="both", expand=True)

        customtkinter.CTkLabel(card, text=tr("about_title", "🛰️ AstroBot"),
                               font=("Segoe UI Variable", 28, "bold"), text_color=self.ACCENT
                               ).pack(pady=(40, 4))
        customtkinter.CTkLabel(card, text=f"{tr('about_version', 'Versión')} {__version__}",
                               font=("Segoe UI Variable", 14)).pack()
        customtkinter.CTkLabel(card, text=f"{tr('about_dev', 'Por')} {__author__}",
                               font=("Segoe UI Variable", 12), text_color=self.TEXT_MUTED
                               ).pack(pady=(4, 24))
        customtkinter.CTkLabel(card, text=tr("about_desc", "Panel profesional."),
                               font=("Segoe UI Variable", 12), wraplength=560, justify="center"
                               ).pack(pady=(0, 24), padx=40)

        bf = customtkinter.CTkFrame(card, fg_color="transparent")
        bf.pack(pady=6)
        customtkinter.CTkButton(bf, text=tr("btn_support_server", "❓ Soporte"), width=190,
                                command=lambda: webbrowser.open_new_tab("https://discord.gg/v7DqaMN9yM"),
                                fg_color=self.INFO, hover_color=self.INFO_HOVER).grid(row=0, column=0, padx=8)
        customtkinter.CTkButton(bf, text=tr("btn_view_logs", "📁 Ver Logs"), width=190,
                                command=self.open_logs_folder, fg_color=self.MUTED).grid(row=0, column=1, padx=8)

        customtkinter.CTkLabel(card, text=f"© {__year__} AstroSoftware — {tr('about_rights', 'Derechos reservados')}",
                               font=("Segoe UI Variable", 10), text_color=self.MUTED).pack(side="bottom", pady=22)

    def open_logs_folder(self):
        p = os.path.abspath(log_dir)
        try:
            if platform.system() == "Windows": os.startfile(p)
            elif platform.system() == "Darwin": subprocess.Popen(["open", p])
            else: subprocess.Popen(["xdg-open", p])
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir: {e}")

    def open_invite_link(self):
        cid = self.client_id_var.get().strip()
        if not cid:
            messagebox.showwarning("Client ID", tr("desc_client_id", "Necesario."))
            self.show_page("settings"); return
        webbrowser.open_new_tab(
            f"https://discord.com/api/oauth2/authorize?client_id={cid}"
            f"&permissions=8&scope=bot%20applications.commands")

    def refresh_stats_loop(self):
        self._update_stats()
        self.after(3000, self.refresh_stats_loop)

    def _update_stats(self):
        b = self.bot_instance.bot if (self.bot_instance and self.bot_instance.bot) else None
        if b and self.bot_instance.running:
            try:
                gc = len(b.guilds)
                try: uc = sum(g.member_count for g in b.guilds if g.member_count)
                except Exception: uc = "N/D"
                lat = f"{round(b.latency * 1000)} ms" if b.latency else "N/D"
                if "servers" in self.stat_labels and self.stat_labels["servers"].winfo_exists():
                    self.stat_labels["servers"].configure(text=str(gc))
                    self.stat_labels["users"].configure(text=str(uc))
                    self.stat_labels["latency"].configure(text=lat)
                    self.stat_labels["uptime"].configure(text=self.bot_instance.get_uptime())
            except Exception: pass
        else:
            for k in ("servers", "users", "latency", "uptime"):
                if k in self.stat_labels and self.stat_labels[k].winfo_exists():
                    self.stat_labels[k].configure(text="—")
        try:
            if "cpu" in self.stat_labels and self.stat_labels["cpu"].winfo_exists():
                self.stat_labels["cpu"].configure(text=f"{psutil.cpu_percent(interval=None)}%")
            if "ram" in self.stat_labels and self.stat_labels["ram"].winfo_exists():
                self.stat_labels["ram"].configure(text=f"{psutil.virtual_memory().percent}%")
        except Exception: pass

    def refresh_language(self, new_lang):
        """Cambia el idioma del GUI Y del bot, y reconstruye las páginas."""
        print(f"[GUI] Cambiando idioma a '{new_lang}'...")
        self.config["language"] = new_lang
        lang_manager.load_language(new_lang)
        save_config(self.config)
        global config_data
        config_data = self.config

        # Guardar página actual
        current_page = "settings"
        for name, p in self.pages.items():
            try:
                if p.winfo_viewable():
                    current_page = name; break
            except Exception: pass

        # Destruir páginas viejas
        for p in list(self.pages.values()):
            try: p.destroy()
            except Exception: pass
        self.pages.clear()

        # Reconstruir con nuevo idioma
        self._build_dashboard_page()
        self._build_settings_page()
        self._build_commands_page()
        self._build_logs_page()
        self._build_about_page()

        # Actualizar sidebar
        self._nav_buttons["dashboard"].configure(text=tr("nav_dashboard", "🏠   Panel"))
        self._nav_buttons["settings"].configure(text=tr("nav_settings", "⚙️   Configuración"))
        self._nav_buttons["commands"].configure(text=tr("nav_commands", "🧩   Comandos"))
        self._nav_buttons["logs"].configure(text=tr("nav_logs", "📜   Registros"))
        self._nav_buttons["about"].configure(text=tr("nav_about", "ℹ️   Acerca de"))

        if hasattr(self, 'sidebar_subtitle_label') and self.sidebar_subtitle_label.winfo_exists():
            self.sidebar_subtitle_label.configure(text=f"{tr('sidebar_subtitle', 'Panel')} · v{__version__}")

        self._update_window_title()
        self.show_page(current_page)
        print(f"[GUI] Idioma cambiado a '{new_lang}'. {len(lang_manager.locales)} claves cargadas.")

    def save_settings(self):
        self.config["token"] = self.bot_token_var.get().strip()
        self.config["client_id"] = self.client_id_var.get().strip()
        self.config["spam_link"] = self.spam_link_var.get().strip()
        self.config["spam_name"] = self.spam_name_var.get().strip()
        self.config["activity_type"] = self.act_type_var.get()
        self.config["activity_name"] = self.act_name_var.get().strip()
        self.config["language"] = self.language_var.get()
        save_config(self.config)
        lang_manager.load_language(self.config["language"])
        global config_data
        config_data = self.config
        messagebox.showinfo(tr("title_settings_full", "Config"),
                            tr("settings_saved_msg", "Guardado."))

    def save_commands(self):
        self.config['disabled_commands'] = [c for c, v in self.command_switches.items() if v.get() == "off"]
        save_config(self.config)
        global config_data
        config_data = self.config
        messagebox.showinfo(tr("title_commands", "Comandos"), tr("commands_saved_msg", "Actualizados."))

    def update_status_label(self, text, color):
        if hasattr(self, 'status_label') and self.status_label.winfo_exists():
            self.status_label.configure(text=text, text_color=color)

    def start_bot_thread(self):
        tok = self.bot_token_var.get().strip()
        if not tok:
            messagebox.showerror("Error", tr("err_token_empty", "Introduce Token."))
            self.show_page("settings"); return
        self.clear_logs_view()
        self.update_status_label(tr("status_starting", "Iniciando..."), self.WARNING)
        self.start_button.configure(state="disabled")
        self.stop_button.configure(state="normal")
        self.bot_thread = threading.Thread(target=self.bot_execution_thread_target, args=(tok,), daemon=True)
        self.bot_thread.start()
        self.after(5000, self.check_connection)

    def bot_execution_thread_target(self, token):
        try:
            self.bot_instance = AdvancedAstroBot(token)
            self.bot_instance.run()
        except Exception as e:
            logger.error(f"Error en hilo del bot: {e}")
        finally:
            try:
                self.after(0, self.handle_bot_stopped)
            except Exception:
                pass

    def check_log_queue_periodically(self):
        self.process_log_queue()
        self.after(100, self.check_log_queue_periodically)

    def process_log_queue(self):
        try:
            while True:
                msg = log_queue.get_nowait()
                for area in (getattr(self, 'log_area', None), getattr(self, 'full_log_area', None)):
                    if area and area.winfo_exists():
                        area.configure(state="normal")
                        area.insert("end", msg + "\n")
                        area.configure(state="disabled")
                        area.see("end")
        except queue.Empty: pass

    def check_connection(self):
        if self.bot_instance and self.bot_instance.running:
            self.update_status_label(tr("status_connected", "🟢  Conectado"), self.SUCCESS)
        elif self.bot_thread and self.bot_thread.is_alive():
            pass
        else:
            self.update_status_label(tr("status_error", "🔴  Error"), self.DANGER)
            self.handle_bot_stopped()

    def stop_bot_thread(self):
        if not self.bot_instance: return
        self.update_status_label(tr("status_stopping", "Deteniendo..."), self.WARNING)
        self.stop_button.configure(state="disabled")
        if self.bot_instance.bot_loop and self.bot_instance.bot_loop.is_running():
            try:
                asyncio.run_coroutine_threadsafe(
                    self.bot_instance.stop_bot_async(),
                    self.bot_instance.bot_loop)
                logger.info("Señal de parada enviada al bot.")
            except Exception as e:
                logger.error(f"Error enviando stop: {e}")
                self.handle_bot_stopped()
        else:
            logger.warning("bot_loop no disponible. Forzando cierre.")
            try: self.bot_instance.running = False
            except Exception: pass
            self.handle_bot_stopped()

    def handle_bot_stopped(self):
        self.update_status_label(tr("status_stopped", "●  Detenido"), self.DANGER)
        if hasattr(self, 'start_button') and self.start_button.winfo_exists():
            self.start_button.configure(state="normal")
        if hasattr(self, 'stop_button') and self.stop_button.winfo_exists():
            self.stop_button.configure(state="disabled")
        self.bot_instance = None

    def on_closing_application(self):
        if self.bot_thread and self.bot_thread.is_alive():
            self.stop_bot_thread()
            self.after(2000, self.destroy)
        else:
            self.destroy()


if __name__ == "__main__":
    print(f"Iniciando GUI para AstroBot v{__version__}...")
    logger.info(f"Lanzando GUI v{__version__} en {platform.system()} {platform.release()}")

    app = BotGUI()
    try:
        app.mainloop()
    except Exception as gui_error:
        logger.critical(f"Error fatal en mainloop: {gui_error}", exc_info=True)
        print(f"\n--- ERROR FATAL ---\n{gui_error}\n------------------")
        try:
            r = tk.Tk(); r.withdraw()
            messagebox.showerror("Error Crítico", f"Error: {gui_error}\nRevisa el log.")
            r.destroy()
        except Exception: pass
        input("Enter para cerrar...")

    logger.info("App cerrada.")