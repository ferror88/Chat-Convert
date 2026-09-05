import re
from datetime import datetime

def convertir_whatsapp_a_md(ruta_txt, ruta_md, nombre_grupo="Grupo de vídeos"):
    with open(ruta_txt, 'r', encoding='utf-8') as f:
        whatsapp_text = f.read()

    lines = whatsapp_text.strip().split('\n')
    
    export_date = datetime.now().strftime("%d de %B de %Y a las %H:%M")

    md_lines = [
        f"# Exportación de chat de WhatsApp: {nombre_grupo}",
        f"Fecha de exportación: {export_date}",
        ""
    ]

    current_date_str = ""
    # Patrón estándar de WhatsApp: "D/M/YY, HH:MM - Emisor: Mensaje"
    pattern = re.compile(r'^(\d{1,2}/\d{1,2}/\d{2,4}),\s+(\d{2}:\d{2})\s+-\s+(.*)$')

    months_es = {
        "1": "enero", "2": "febrero", "3": "marzo", "4": "abril", "5": "mayo", "6": "junio",
        "7": "julio", "8": "agosto", "9": "septiembre", "10": "octubre", "11": "noviembre", "12": "diciembre"
    }

    for line in lines:
        match = pattern.match(line)
        if match:
            date_raw, time_str, content = match.groups()
            parts = date_raw.split('/')
            day = parts[0]
            month = months_es.get(parts[1], parts[1])
            year_full = "20" + parts[2] if len(parts[2]) == 2 else parts[2]
            
            formatted_date = f"{day} de {month} de {year_full}"
            
            if formatted_date != current_date_str:
                current_date_str = formatted_date
                md_lines.append("")
                md_lines.append("---")
                md_lines.append("")
                md_lines.append(f"## {formatted_date}")
                md_lines.append("")
                
            if ":" in content:
                sender, msg = content.split(":", 1)
                sender = sender.strip()
                msg = msg.strip()
                md_lines.append(f"[{time_str}] **{sender}:** {msg}")
            else:
                md_lines.append(f"[{time_str}] {content}")

    with open(ruta_md, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))
    print(f"¡Archivo '{ruta_md}' generado con éxito a partir de '{ruta_txt}'!")

if __name__ == "__main__":
    # Coloca aquí el nombre de tu archivo .txt de WhatsApp
    convertir_whatsapp_a_md("Chat de WhatsApp con Grupo.txt", "exportacion_chat.md")