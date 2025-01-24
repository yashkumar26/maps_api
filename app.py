from flask import Flask, render_template_string
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    file_path = "logs/distance_log.csv"
    if os.path.isfile(file_path):
        df = pd.read_csv(file_path)
        table_html = df.to_html(classes='table', index=False, header=True)
    else:
        table_html = "<p>No data available.</p>"

    html_template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Distance Log</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container">
            <h1 class="mt-4">Distance Log</h1>
            {{ table_html|safe }}
        </div>
    </body>
    </html>
    '''

    return render_template_string(html_template, table_html=table_html)

if __name__ == '__main__':
    app.run(debug=True)
