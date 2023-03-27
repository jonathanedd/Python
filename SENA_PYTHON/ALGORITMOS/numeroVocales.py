def vocals(phrase):
    count=0
    for i in phrase:
        if i in "aeiouAEIOU":
            count =+ 1
            print(count)

phrase = str(input("Escriba una frase o palabra"))
vocals(phrase)