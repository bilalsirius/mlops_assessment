import time
a = "a"
print("a")
def init():
    global a
    time.sleep(10)
    a = "hello"
    print(a)

def inference(model_inputs:dict) -> dict:
    global a
    b = a + " world"
    print(b)

    return {"greeting": b}.update(model_inputs)
