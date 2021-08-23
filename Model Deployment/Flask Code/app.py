from flask import Flask, render_template, request, redirect
import pickle

app = Flask(__name__, template_folder='template')
model = pickle.load(open('model_tree.pkl', 'rb'))


@app.route('/')
def index_page():
    print(model)
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict_logic():
    
    if request.method == 'POST':
        L2LoginID = float(request.form.get('L2LoginID'))
        L2Decision = float(request.form.get('L2Decision'))
        L2_Op_Time = float(request.form.get('L2_Op_Time'))
    #print(L2LoginID,L2Decision,L2_Op_Time)
    #print([[L2LoginID,L2Decision,L2_Op_Time]])
    pred_name = model.predict([[L2LoginID,L2Decision,L2_Op_Time]]).tolist()[0]
    if  pred_name == 'Excellent':
        pred = 'Nice Excellent Operator'
    else:
        pred = 'It is'
    return render_template('index.html', prediction=pred, pred_name=pred_name)

if __name__ == "__main__":
    app.run(debug=True)