from flask import Flask,render_template,redirect,request,send_file
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def getdata():
    name = request.form['name']
    email = request.form['email']
    contact_number = request.form['contact_number']
    message = request.form['message']
        # Write form data to a CSV file
    with open("forms.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name,email,contact_number,message])
    return "<h1>Thank You \n Data submitten successfully</h1>"
        
    #     # Redirect the user to the homepage after form submission
    # return "Thanks to you"

@app.route('/lectures') 
def lectures():
    return render_template('lectures.html')

@app.route('/responses')
def download_csv():
    # Specify the path to your CSV file
    csv_path = 'forms.csv'
    
    # Send the file as an attachment
    return send_file(csv_path, as_attachment=True)

@app.route('/clear')
def download_csv():
    with open("forms.csv", mode='w', newline='') as file:
        pass
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
