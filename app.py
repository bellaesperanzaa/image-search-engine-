from flask import Flask,render_template, request,url_for
import random

app = Flask(__name__)



@app.route('/gifs')
def gifs():
    myGifs = [
        "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMG85aTI2a2NkcjhobHhhcmE5MTlvbGIyZmpmNHRvMjkxM3Nsc3dxcCZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/wJ3RSWBFeWH2jt1Jgt/200.webp"
        "https://media2.giphy.com/media/UO5elnTqo4vSg/200.webp?cid=82a1493b6t123rhg8h5tvorhv0jpa7vyge63ecj6xp0i8rhm&ep=v1_gifs_trending&rid=200.webp&ct=g"
        "https://media4.giphy.com/media/lMsT2f47tDxFMYdJMC/giphy.webp?cid=82a1493bwjssy1lwpdeo65hwt2148sxg7zc4b03vnekm4w5y&ep=v1_gifs_trending&rid=giphy.webp&ct=g"
        "https://media1.giphy.com/media/hqFNEMVji3fzuLUuBw/200.webp"
        "https://media0.giphy.com/media/4acdDr4Cl39JoNrcQ7/200w.webp"
    ]
    randomGif = random.choice(myGifs)
    return render_template('gifs.html', random=randomGif, randomBool=False, myGifs=myGifs)


@app.route('/input', methods=['GET','POST'])
def input():
    imgData = {
        "dog": ["https://media2.giphy.com/media/oebOcslmnSXMQ/giphy.webp?cid=790b7611w7g68l1s4jyreutkb9osktgxitqzicvlyf4nhbq8&ep=v1_gifs_search&rid=giphy.webp&ct=g",
               "https://media1.giphy.com/media/WLbtNNR5TKJBS/giphy.webp?cid=ecf05e474a1be2tqhy79mfvgkokvjj6z76jbtbguwnjmcyig&ep=v1_gifs_search&rid=giphy.webp&ct=g",
               "https://media2.giphy.com/media/11FOb5AeCLT8oo/giphy.webp?cid=ecf05e47hs570lhfpx1i4hvnl4fbi7w01km65ychm67lcxlo&ep=v1_gifs_search&rid=giphy.webp&ct=g",
               "https://media4.giphy.com/media/tDE6WlYEJGuze/giphy.webp?cid=ecf05e47tmqdv7o42orbrbhrdvd4pkzp1nlfp7wpiozykve5&ep=v1_gifs_search&rid=giphy.webp&ct=g"]
    }
    if request.method =='POST':
        query = request.form['query']
        if query not in imgData:
            return "No data found for " + query
        return render_template('input.html', imgData=imgData[query])
    
    return render_template('input.html', url=url_for('input'))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=500, debug=True)
    