# Convertidor de Chats de WhatsApp a Markdown (para Notion)

Este script de Python automatiza la conversión de un archivo de exportación de chat de WhatsApp a formato Markdown (`.md`), estructurándolo por fechas y manteniendo las referencias a las imágenes y archivos multimedia organizados para su uso en Notion.

---

## 📂 Estructura del Proyecto

Asegúrate de que tu directorio de trabajo tenga la siguiente estructura antes de ejecutar el script:

```text
📁 tu-proyecto/
│
├── 📜 whatsapp_a_md_limpio.py          # Script principal de conversión
├── 📄 Chat de WhatsApp con Grupo...txt  # Tu exportación de WhatsApp
├── 📁 docs/                            # Carpeta con las imágenes/multimedia exportados
└── 📄 README.md                        # Este manual de instrucciones
```

El archivo de texto (`.txt`) y los documentos multimedia se deben extraer del teléfono móvil. Para ello, entra en el grupo que quieras exportar, pulsa en los tres puntitos de la parte superior, ve a Más > Exportar chat y selecciona Incluir archivos.

---

## ⚙️ Instrucciones de Ejecución

1. Coloca los archivos: Asegúrate de tener el .txt de WhatsApp en la raíz del proyecto y todas las imágenes dentro de la carpeta docs.

2. Ejecuta el script: Abre tu terminal en la carpeta y escribe el siguiente comando:
`python whatsapp_a_md_limpio.py`

3. Obtén el resultado: Se generará el archivo exportacion_chat.md con los mensajes en línea fluida ([Hora] **Emisor:** Mensaje/Imagen) para evitar que Notion rompa los bloques visuales.

---

## 📌 Importar la carpeta completa como espacio de trabajo (La forma oficial de Notion)

En lugar de crear una página en blanco y arrastrar o importar solo el archivo .md suelto:

1. Comprime tu carpeta contenedora (la que tiene dentro el archivo .md y la carpeta docs) en un archivo .zip.

2. Ve a Notion, haz clic en Import (Importar) en el menú lateral izquierdo.

3. Selecciona Markdown & CSV y elige el archivo .zip completo.

4. Al importar el .zip entero, Notion procesa la estructura de carpetas local y vincula correctamente las imágenes de la carpeta docs a su base de datos interna.