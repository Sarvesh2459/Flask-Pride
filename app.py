from flask import *  
import random
app = Flask(__name__)
import binascii as B
import pride as P
# import run as R
 
@app.route('/')  
def home ():  
    return render_template("index.html")  
 
@app.route('/test')
def test():
    return render_template("test.html")

# name="0000000000000000"
# adult=""
# seat_list=[]
# total_amount=""
# arr="00000000000000000000000000000000"

# global name #key
# global arr #plaintext
# global encrypt_text
# global decrypt_text
@app.route('/login')  
def login():  
    return render_template("login.html")



@app.route('/encrypt')  
def encrypt():  
    return render_template("train1.html",encrypt=encrypt_text)
 
@app.route('/decrypt')  
def decrypt():  
    return render_template("train2.html",decrypt=decrypt_text)
 

#after typing to and from info
@app.route('/validate', methods = ["POST"])  
def validate():  
    if request.method == 'POST':  
        global name #key
        global arr #plaintext
        global encrypt_text
        global decrypt_text
  
        name=request.form['plaintext']
        arr=request.form['key_p']
        val1 = arr
        arr1 = bytes(val1, 'utf-8')

        val2 = name
        arr2 = bytes(val2, 'utf-8')

        print(arr1)
        print(arr2)
      

        key1        = B.unhexlify(arr1)
        plain1      = B.unhexlify(arr2)
        cipher1     = P.Pride(key1)
        encrypted1  = cipher1.encrypt(plain1)
        # print(P.b2s(B.hexlify(encrypted1)))  # b2s so it works w/ python 2 and 3
        encrypt_text= P.b2s(B.hexlify(encrypted1))
        decrypted1  = cipher1.decrypt(encrypted1)
        # print(P.b2s(B.hexlify(decrypted1)))
        decrypt_text=P.b2s(B.hexlify(decrypted1))
        print(decrypt_text)
        return redirect(url_for("encrypt"))  
    return redirect(url_for("fail"))


@app.route('/validate2', methods = ["POST"])  
def validate2():  
    if request.method == 'POST':  
        global name #key
        global arr #plaintext
        global encrypt_text
        global decrypt_text
        name=request.form['encryptext']
        arr=request.form['key_e']
        val1 = arr
        arr1 = bytes(val1, 'utf-8')

        val2 = name
        arr2 = bytes(val2, 'utf-8')

        print(arr1)
        print(arr2)
      

        key1        = B.unhexlify(arr1)
        plain1      = B.unhexlify(arr2)
        cipher1     = P.Pride(key1)
        # encrypted1  = cipher1.encrypt(plain1)
        # # print(P.b2s(B.hexlify(encrypted1)))  # b2s so it works w/ python 2 and 3
        # encrypt_text= P.b2s(B.hexlify(encrypted1))
        decrypted1  = cipher1.decrypt(plain1)
        # print(P.b2s(B.hexlify(decrypted1)))
        decrypt_text=P.b2s(B.hexlify(decrypted1))
        print(decrypt_text)
        return redirect(url_for("decrypt"))  
    return redirect(url_for("fail"))


#for booking
@app.route('/booking', methods = ["POST"])  
def booking():  
    if request.method == 'POST':
        return redirect(url_for("payment"))  
    return redirect(url_for("fail"))

#for payments
@app.route('/payment_option', methods = ["POST"])  
def payment_option():  
    if request.method == 'POST':  
        return redirect(url_for("congrats"))  
    return redirect(url_for("fail"))
 
@app.route('/fail')  
def fail():  
    return "no train available"
  
if __name__ == '__main__':  
    app.run(debug = True) 