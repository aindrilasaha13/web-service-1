from flask import Flask, send_file
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.get("/")
def send():

    x = [1,2,3,4,5]
    y = [1,4,9,16,25]
    
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
    app.run(debug=True,port=5001)