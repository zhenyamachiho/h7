def pooh(list):
    list = [sum(i in 'уеыаоэяию' for i in j) for j in list]
    if len(set(list)) == 1:
        return "Парам пам-пам"
    return "Пам парам"


song = input().split()
print(pooh(song))
