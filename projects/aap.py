# pip install flask
from flask import Flask, render_template, url_for , request
import joblib
model=joblib.load(r"C:\Users\ASUS\OneDrive\Desktop\Internship 2june\projects\model.lb")

app=Flask(__name__)  ## flask object


@app.route('/') # decorator 
def index():
    return render_template('index.html')   

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        brand_name=request.form['brand_name']
        owner=int(request.form['owner'])
        age=int(request.form['age'])
        power=int(request.form['power'])
        kms_driven=int(request.form['kms_driven'])

        bike_number= {'TVS': 0,
                    'Royal Enfield': 1,
                    'Triumph': 2,
                    'Yamaha': 3,
                    'Honda': 4,
                    'Hero': 5,
                    'Bajaj': 6,
                    'Suzuki': 7,
                    'Benelli': 8,
                    'KTM': 9,
                    'Mahindra': 10,
                    'Kawasaki': 11,
                    'Ducati': 12,
                    'Hyosung': 13,
                    'Harley-Davidson': 14,
                    'Jawa': 15,
                    'BMW': 16,
                    'Indian': 17,
                    'Rajdoot': 18,
                    'LML': 19,
                    'Yezdi': 20,
                    'MV': 21,
                    'Ideal': 22}
        brand_name_encoding =bike_number[brand_name]

        lst =[[owner,brand_name_encoding, kms_driven,age,power]]
        pred=model.predict(lst)
        pred=pred[0]
        pred=round(pred, 2)
        return render_template('project.html', prediction= str(pred))

if __name__=='__main__':
    app.run(debug=True)