import csv
from pathlib import Path
import pandas as pd
from flask import *

app = Flask(__name__)

@app.route('/')
def showData():
    # File Path
    path = Path(__file__).parent / "report_data.csv"

    # read csv
    uploaded_df = pd.read_csv(path, index_col=0)

    # Converting to html Table
    uploaded_df_html = uploaded_df.to_html()

    return render_template('show_csv_data.html', data_var=uploaded_df_html)

if __name__ == '__main__':
    app.run(debug=True)