from flask import Flask, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__)

# 读取 CSV 文件
def load_data():
    # 假设 CSV 文件名为 data.csv，且与 app.py 在同一目录下
    data = pd.read_csv('Web/selected_stocks.csv')
    return data

# 主页路由
@app.route('/')
def index():
    return render_template('index.html')

# 数据接口路由
@app.route('/data')
def data():
    df = load_data()
    # 将数据转换为 JSON 格式
    data_json = df.to_dict(orient='records')
    return jsonify(data_json)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
