app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Hello"
    
    
@app.route('/test/<xxx>')
def check_value(xxx):
    if xxx == "hello":
        return "helli"
    else:
        return f"Tu as envoyé : {xxx}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render impose un port
    app.run(host="0.0.0.0", port=port)
Add comment