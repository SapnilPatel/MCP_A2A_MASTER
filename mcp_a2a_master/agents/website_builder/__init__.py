

class wesite_builder:
    """
    Simple website builder agent that can create a basic webpages.
    """

    def __init__(self):
        pass

    def build_website(self, description: str) -> str:
        """
        Builds a simple HTML page based on the provided description.
        """
        html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>My Simple Website</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1 {{ color: #333; }}
                p {{ font-size: 18px; }}
            </style>
        </head>
        <body>
            <h1>Welcome to My Website</h1>
            <p>{description}</p>
        </body>
        </html>
        """
        return html_template