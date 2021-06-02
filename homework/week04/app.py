from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework

## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')

## 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    # API를 만들어 보자
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_number_receive = request.form['phone_number_give']

    # mongoDB에 데이터 넣기
    order = {'name': name_receive, 'count': count_receive, 'address': address_receive, 'phone': phone_number_receive}
    db.orders.insert_one(order)
    return jsonify({'result': 'success'})

## 주문 목록보기(GET) API
@app.route('/order', methods=['GET'])
def view_orders():
    # API를 만들어 보자
    # return jsonify({'result': 'success', 'orders': orders})
    orders = list(db.orders.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)