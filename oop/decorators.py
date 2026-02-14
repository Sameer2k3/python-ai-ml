# In Python, a decorator is basically a function that modifies the behavior of another function (or method) without changing its code directly.

def greet(fx):
    def mfx():
        print("good morning")              #first runs this
        fx()                                         #fx runs here 
        print("thanks for using the function")       #last runs this
    return mfx   #mfx is called

@greet   #greet named decorator is being applied on the hello function
def hello():
    print("hello , how are you")

hello()   #hello function is being called out


# in line 3, fx ki jagah humne hello function by line 10 and 11 ko bheja fir hamne ek naya function banaya mfx jisme phle good morinin print hoga then hello funtion run hoga then thanks for using prin t hoga then last me mfx call hoga