my_list=list()
my_list=['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print("Данные на входе:")
print(my_list)
print("Добавляем кавычки:")
def convert_list_in_str (dataset: list) ->list:
# добавлем кавычки через одну

    my_list2=list()
    for num_s in range(len(dataset)):
        try:
            simbol=int(dataset[num_s])//10

            if simbol==0:
                if len(dataset[num_s])==2:
                    my_list2.append(chr(34))
                    my_list2.append("+"+"0"+str(int(dataset[num_s])))
                    my_list2.append(chr(34))
                else:
                    my_list2.append(chr(34))
                    my_list2.append("0" + str(int(dataset[num_s])))
                    my_list2.append(chr(34))
            else:
                my_list2.append(chr(34))
                my_list2.append(dataset[num_s])
                my_list2.append(chr(34))
        except ValueError:

            my_list2.append(dataset[num_s])

    return my_list2
def New_String (dataset1: list)-> str:
    Single_s=""
    for num_s in range(len(dataset1)):

        if dataset1[num_s]==chr(34):
            if num_s==1 :
                Single_s =  Single_s+dataset1[num_s]
            elif num_s==3:
                Single_s = Single_s + dataset1[num_s]+ chr(32)
            elif num_s == 5:
                Single_s = Single_s + dataset1[num_s]
            elif num_s == 7:
                Single_s = Single_s + dataset1[num_s] + chr(32)
            elif num_s == 12:
                Single_s = Single_s + dataset1[num_s]
            elif num_s == 14:
                Single_s = Single_s + dataset1[num_s] + chr(32)
        else:
                Single_s = Single_s +dataset1[num_s]+  chr(32)
    Single_s=Single_s.replace(' " ', '" ', )
    return Single_s

print(convert_list_in_str(my_list))
my_list3=convert_list_in_str(my_list)
print("Выводим в строку полученный список:")
print(New_String(my_list3))

