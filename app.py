from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

# Load your FMP API Key
FMP_API_KEY = os.getenv("FMP_API_KEY", "UwbsK5XWR0U2yaV0732fg2MSGz8b2HBR")

@app.route("/stock", methods=["GET"])
def get_stock_data():
    ticker = request.args.get("ticker")
    if not ticker:
        return jsonify({"error": "Please provide a ticker symbol."}), 400

    url = f"https://financialmodelingprep.com/api/v3/quote/{ticker}?apikey={FMP_API_KEY}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch data from FMP."}), 500
    
    data = response.json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
