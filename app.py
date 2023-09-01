from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    data2=[{'tenor': ''}, {'tenor': 6}, {'tenor': 12}, {'tenor': 18}, {'tenor': 24}, {'tenor': 30}, {'tenor': 36}]
    return render_template('endUsermokas.html', data=data2)

@app.route('/gfg', methods=['GET', 'POST'])
def endUserMokas():
    data= pd.read_csv("data/skema.csv", delimiter='|')
    data2=[{'tenor': ''}, {'tenor': 6}, {'tenor': 12}, {'tenor': 18}, {'tenor': 24}, {'tenor': 30}, {'tenor': 36}]
    if request.method == 'POST':
        tenor = request.form.get("waktu")
        pinjam = request.form.get("pinjam")
        tenor1 = int(tenor)
        pinjam1 = int(pinjam.replace(".",""))
        pinjam11= mw.rupiah_format(pinjam1)
        pokok = round(pinjam1/tenor1,2)
        pokok1 = mw.rupiah_format(pokok)
        angs = data[(data['Tenor'] == tenor1) & (data['Pinjam']==pinjam1)].index
        try:
            angs2 = data['Angsuran'].iloc[angs].values[0]
            angs22 = mw.rupiah_format(angs2)
            bunga = angs2-pokok
            bunga1 = mw.rupiah_format(bunga)
            totalAngs = angs2*tenor1
            totalAngs1 = mw.rupiah_format(totalAngs)
            return render_template('doneMuncul.html', datakons={'tenor':tenor ,'pinjam': pinjam11, 'pokok':pokok1, 'angs':angs22, 'bunga':bunga1, 'totalAngs':totalAngs1})
        except:
            return render_template('doneNmuncl.html', error_text={'err1':'Nilai Angsuran Tidak Ditemukan', 'err2':'Silahkan coba lagi.'})
    return render_template('endUsermokas.html', data=data2)

@app.route('/benelli')
def benelli():
    return render_template('Benelli.html')
    
if __name__ == '__main__':
    import pandas as pd
    from modules import moduleWeb as mw
    app.run(debug=True)
