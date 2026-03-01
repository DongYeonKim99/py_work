print("------------------------------")
def persona(width=11, height=21):
    print("함수디폴드값없음, width=", width, "height=", height)

def personb(width=4, height=3):
    print("함수디폴드값없음, width=", width, "height=", height)

persona(10, 20)
persona()
personb()

persona(10,)
