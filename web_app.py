from flask import Flask, render_template,request, jsonify
from scraper import run_scraper

app = Flask(__name__)



@app.route('/')
def index():
    # You can pass dynamic options to the dropdown if needed
    mensa_options = ["Wilhelmstraße", "Morgenstelle", "Prinz Karl"]
    date_options = ["2024-10-24","2024-10-25","2024-10-26"]


    return render_template('index.html', options=mensa_options, dates=date_options)

@app.route('/submit', methods=['POST'])
def display_res():

    # get option result
    selected_option = request.form.get('dropdown')
    selected_date = request.form.get("date")

    # Ensure both dropdowns are selected
    if not selected_option or not selected_date:
        return "Please select both an option and a date!", 400

    # get scraper results (dataframe)
    scraper_res = run_scraper(selected_option,selected_date)

    # Convert the dataframe to HTML
    df_html = scraper_res.to_html(classes='dataframe', header="true", index=False)


    # Render the template and pass the dataframe HTML to it
   # return render_template('result.html', selected_option=selected_option, table=df_html)
    return render_template('result.html', table=df_html, selected_option=selected_option, selected_date=selected_date)


if __name__ == '__main__':
    app.run(debug=True)


