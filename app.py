from flask import Flask, send_file, request
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.get("/")
def send():

    N = int(request.args.get("N"))
    x = list(range(1,N+1))
    y = [i*i for i in range(1,N+1)]
    
    plt.title("squares")
    plt.plot(x, y, color='red')

    plt.xlabel('numbers',fontsize=10)
    plt.ylabel("squares",fontsize=10)
    plt.xticks(fontsize = 10)
    plt.yticks(fontsize = 10)
    
    img = "static\\plotted_squares.jpg"
    plt.savefig(img)
    return send_file(img,as_attachment=True,mimetype='image/jpg') 

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True,port=5001)