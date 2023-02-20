def check_rythms(frase):
    check_values = list("аяуюоеёэиы")
    frase = frase.split()
    coun = vowels(frase[0], check_values)
    for i in frase:
        if vowels(i, check_values) != coun:
            print("Парам пам-пам")
            exit()
        else:
            continue
    return "Пам парам"


def vowels(string, check_values):
    coun = 0
    for i in list(string):
        if i in check_values:
            coun += 1
    return coun


print(check_rythms(input()))
