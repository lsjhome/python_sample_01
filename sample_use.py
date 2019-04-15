from utils.sample import CountCharacter

if __name__ == '__main__':

    cc = CountCharacter(input("Input words: "))
    n_count = cc.count(input("Input a character: "))
    print (n_count)
