# Previos a compilación LaTex

Sigue los siguientes pasos para compilar el documento incluyendo el código del Jupyter Notebook.

1. Ejecuta los siguientes comandos para moverte al directorio documentation: `cd documentation`, elimina los archivos anteriores si existen `rm -r notebook_images/ notebook_content.tex`

2. Ejecuta pandoc para convertir el notebook a latex: `pandoc ../Notebook.ipynb -t latex --listings --extract-media=notebook_images -o notebook_content.tex`. Asegurate de tener instalado pandoc, puedes instalarlo con `sudo apt install pandoc`.

3. Agrega a `notebook_content.tex` el comando mágico `% !TeX root = Reporte.tex` al principio del archivo. Esto ayudará a que el editor de latex sepa que el documento principal es `Reporte.tex` y no intente compiar `notebook_content.tex` saltando un error.

4. Compila normalmente usando `pdflatex Reporte.tex`.
