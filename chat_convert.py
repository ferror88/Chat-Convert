import re

def convertir_whatsapp_a_md(ruta_txt, ruta_md, carpeta_docs="docs", nombre_grupo="Grupo de vídeos"):
    try:
        with open(ruta_txt, 'r', encoding='utf-8') as f:
            whatsapp_text = f.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_txt}'. Asegúrate de que está en la misma carpeta.")
        return

    lines = whatsapp_text.strip().split('\n')
    
    months_es = {
        "1": "enero", "2": "febrero", "3": "marzo", "4": "abril", "5": "mayo", "6": "junio",
        "7": "julio", "8": "agosto", "9": "septiembre", "10": "octubre", "11": "noviembre", "12": "diciembre"
    }
    
    from datetime import datetime
    ahora = datetime.now()
    export_date = f"{ahora.day} de {months_es[str(ahora.month)]} de {ahora.year} a las {ahora.strftime('%H:%M')}"

    md_lines = [
        f"# Exportación de chat de WhatsApp: {nombre_grupo}",
        f"Fecha de exportación: {export_date}",
        ""
    ]

    current_date_str = ""
    pattern = re.compile(r'^[‎‏]?(\d{1,2})/(\d{1,2})/(\d{2,4}),\s+(\d{2}:\d{2})\s+-\s+(.*)$')

    for line in lines:
        match = pattern.match(line)
        if match:
            day, month_num, year_raw, time_str, content = match.groups()
            
            month = months_es.get(month_num, month_num)
            year_full = "20" + year_raw if len(year_raw) == 2 else year_raw
            
            formatted_date = f"{day} de {month} de {year_full}"
            
            if formatted_date != current_date_str:
                current_date_str = formatted_date
                md_lines.append("")
                md_lines.append("---")
                md_lines.append("")
                md_lines.append(f"## {formatted_date}")
                md_lines.append("")
                
            content = content.replace('\u200e', '').strip()
                
            if ":" in content:
                sender, msg = content.split(":", 1)
                sender = sender.strip()
                msg = msg.strip()
                
                if "(archivo adjunto)" in msg or msg.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif', '.mp4', '.opus')):
                    nombre_archivo = msg.replace("(archivo adjunto)", "").strip()
                    md_lines.append(f"[{time_str}] **{sender}:** ![{nombre_archivo}]({carpeta_docs}/{nombre_archivo})")
                else:
                    md_lines.append(f"[{time_str}] **{sender}:** {msg}")
            else:
                md_lines.append(f"[{time_str}] {content}")

    with open(ruta_md, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))
    print(f"¡Archivo '{ruta_md}' generado apuntando correctamente a la carpeta '{carpeta_docs}'!")

if __name__ == "__main__":
    convertir_whatsapp_a_md("Chat de WhatsApp con Grupo.txt", "exportacion_chat.md", carpeta_docs="docs")