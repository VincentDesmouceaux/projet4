"""
Module pour la gestion de l'exportation des rapports.

Ce module contient la classe ExportManager qui permet d'exporter des rapports
au format texte et HTML.
"""

import sys
from io import StringIO
from pathlib import Path


class ExportManager:
    """
    Classe responsable de l'exportation des rapports.

    Cette classe gère l'exportation des rapports au format texte et HTML, 
    en les sauvegardant dans un répertoire spécifié.
    """

    def __init__(self, export_dir='src/rapports'):
        """
        Initialise le gestionnaire d'exportation.

        Args:
            export_dir (str): Le chemin du répertoire d'exportation. Par défaut 'src/rapports'.
        """
        self.export_dir = Path(export_dir)
        self.export_dir.mkdir(exist_ok=True)  # Crée le répertoire d'exportation s'il n'existe pas

    def export_report(self, filename, display_function, data):
        """
        Exporte un rapport au format texte.

        Args:
            filename (str): Le nom du fichier de rapport.
            display_function (function): La fonction utilisée pour générer le contenu du rapport.
            data (any): Les données à passer à la fonction de génération de rapport.
        """
        report_path = self.export_dir / filename
        with report_path.open('w', encoding='utf-8') as file:
            # Redirige la sortie standard vers le fichier pour capturer le rapport
            original_stdout = sys.stdout
            sys.stdout = file
            display_function(data)
            sys.stdout = original_stdout
        print(f"Rapport sauvegardé sous {report_path}")

    def export_report_html(self, filename, display_function, data):
        """
        Exporte un rapport au format HTML.

        Args:
            filename (str): Le nom du fichier de rapport.
            display_function (function): La fonction utilisée pour générer le contenu du rapport.
            data (any): Les données à passer à la fonction de génération de rapport.
        """
        report_path = self.export_dir / filename

        # Capture la sortie de la fonction de génération de rapport
        captured_output = StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output
        display_function(data)
        sys.stdout = original_stdout
        report_content = captured_output.getvalue()

        # Crée un rapport HTML formaté en utilisant un template
        html_content = f"""
        <html>
        <head>
            <title>Rapport</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1 {{ color: #333; }}
                pre {{ background-color: #f4f4f4; padding: 10px; border-radius: 5px; }}
            </style>
        </head>
        <body>
            <h1>Rapport</h1>
            <pre>{report_content}</pre>
        </body>
        </html>
        """

        # Écrit le contenu HTML dans le fichier
        with report_path.open('w', encoding='utf-8') as file:
            file.write(html_content)

        print(f"Rapport HTML sauvegardé sous {report_path}")
