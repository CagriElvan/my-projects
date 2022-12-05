from flask import Flask

app = Flask(__name__)

@app.route('/')     # Anasayfa demek.
def hello():
    return "Hello World from Flask!!!"

@app.route('/second')   # second ile 2. sayfayı dekore ettik.
def second():
    return 'En büyük Fenerbahçe!!!!'

@app.route('/third/subthird')   # 3. sayfanın bir altsayfası
def third():
    return 'This is the subpage of third page'

@app.route('/forth/<string:id>')        # 4. metinde slashtan sonra ki kısım "numarayı ID olarak çekiyor".
def forth(id):
    return f'Id number of this page is {id}'        # Bu sayfanın ID numarası budur.




if __name__ == '__main__':
    app.run(debug=True)             # Hiçbirşey yazmazsak default = 5000 portunda çalışır.