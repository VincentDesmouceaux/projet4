import sys
from io import StringIO
from pathlib import Path


class ExportManager:
    def __init__(self, export_dir='src/rapports'):
        self.export_dir = Path(export_dir)
        self.export_dir.mkdir(exist_ok=True)

    def export_report(self, filename, display_function, data):
        report_path = self.export_dir / filename
        with report_path.open('w', encoding='utf-8') as file:
            original_stdout = sys.stdout
            sys.stdout = file
            display_function(data)
            sys.stdout = original_stdout
        print(f"Rapport sauvegardé sous {report_path}")

    def export_report_html(self, filename, display_function, data):
        report_path = self.export_dir / filename

        # Capture the output of the display_function
        captured_output = StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output
        display_function(data)
        sys.stdout = original_stdout
        report_content = captured_output.getvalue()

        # Create a formatted HTML report using a template
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

        # Write the HTML content to the file
        with report_path.open('w', encoding='utf-8') as file:
            file.write(html_content)

        print(f"Rapport HTML sauvegardé sous {report_path}")
