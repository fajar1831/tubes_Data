#------ head section ------

import json
import itertools
import os
from os import  system, name
from itertools import chain
import sys
import time

def clear_screen():
        # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def proceed():
    pill2x = input('masukan "y" untuk kemabali ke main menu atau "n" untuk keluar : ')
    if pill2x == 'y' or pill2x == 'Y':
        clear_screen()
        main_menu()
    elif pill2x == 'n' or pill2x == 'N':
        clear_screen()
        sys.exit()
    else:
        print('input invalid')
        clear_screen()
        proceed()

#------ head section end ------

#------ data fetching section ------

with open('data_pembeli.json') as f:    #membuka file json data_pembeli.json
    data = json.load(f)
with open('data_unique_key.json') as f:     #membuka file json data_unique_key.json
    data_unik = json.load(f)


order_id_temp = [] #list sementara untuk data "order_id" (id_order harus unique)
product_temp = [] #list sementara untuk data "product" ("nama produk")
name_temp = [] #list sementara untuk data "name" (nama)
phone_temp = [] #list sementara untuk data "phone" (no hp)
address_temp = [] #list untuk data "address" (alamat)
province_temp =[] #list sementara untuk data "province" (provinsi)
city_temp = [] #list sementara untuk data "city" (kota)
subdistrict_temp = [] #list sementara untuk data "subdistrict" (kecamatan)
zip_temp = [] #list sementara untuk data "zip" (kode pos)
harga_temp= [] #list sementara untuk data "product_price" (harga)
list_av = [] #list untuk menampung order_id baru yang bisa 
list_com = [] #list menampung key hasil generate (string)
temp_D =[] #list menampung diskon

def must_run(): #proses fetch data dari json ke python object list wajib diexecute saat memulai
    
    #fetching data order_id
    for items in data ["order_jam_tangan"]:
        if items["order_id"]!= "":
            order_id_temp.append(items["order_id"])

    #fetching data product
    for items in data ["order_jam_tangan"]:
        product_temp.append(items["product"])

    #fetching data name
    for items in data ["order_jam_tangan"]:
        if items["name"]!= "":
            name_temp.append(items["name"])

    #fetching data phone
    for items in data ["order_jam_tangan"]:
        if items["phone"]!= "":
            phone_temp.append(items["phone"])

    #fetching data address
    for items in data ["order_jam_tangan"]:
        if items["address"]!= "":
            address_temp.append(items["address"])

    #fetching data province
    for items in data ["order_jam_tangan"]:
        if items["province"]!= "":
            province_temp.append(items["province"])

    #fetching data city
    for item in data["order_jam_tangan"]:
        if item["city"]!="":
            city_temp.append(item["city"])

    #fetching data subdisctrict
    for items in data ["order_jam_tangan"]:
        if items["subdistrict"]!= "":
            subdistrict_temp.append(items["subdistrict"])

    #fetching data zip
    for items in data ["order_jam_tangan"]:
        if items["zip"]!= "":
            zip_temp.append(items["zip"])

    #fetching data product_price 
    for items in data ["order_jam_tangan"]:
        if items["product_price"]!= "":
            harga_temp.append(items["product_price"])
    
    #fetching data unique_key
    for items in data_unik ["key_av"]:
        if items!= "":
            list_com.append(items)

must_run()

#------ data fetching section end ------

#------ fiture section ------

def chain_cityp():
    chainn = lambda x : chain(x, city_temp)
    print(list(chainn(province_temp)))

def count_city():
    kota = input('masukan nama kota : ')
    coun = lambda x : x.count(kota)
    print(coun(city_temp))

def accumulatez():
    order_id = []
    for items in order_id_temp:
        order_id.append(int(items))
    accumulatex = lambda x : itertools.accumulate(x, max)
    hasil_A = list(accumulatex(order_id))
    print("Ascending : ")
    print(hasil_A)
    print("Descending : ")
    print(list(reversed(hasil_A)))

def sortedx():
    b = sorted(harga_temp)
    c = list(b)
    d = reversed(c)
    print("Ascending")
    print(list(b))
    print("Descending")
    print(list(d))

def compressx():
    result = itertools.compress(zip_temp,name_temp)
    print(list(result))

def generate_permu():
    for x1 in order_id_temp:
        x3 = int(x1)
        for x2 in list_com:
            b = int(x2)
            if x3 == b :
                list_com.remove(x2)
            elif x3 != b :
                xs = 0
                xs = 1
    for items in list_com:
        list_av.append(items)
    
generate_permu()

def country_comb():
    c = zip(name_temp, address_temp)
    comb = itertools.combinations(c,1) 
    # Print semua kombinasi
    for i in comb: 
        print(i)

def collect():
    for items in harga_temp:
        z = int(items)
        y = z/2
        if z > 243000 :
            x = z/100 * 20
            fin = x * -1
            temp_D.append(fin)
        else:
            temp_D.append(0)

def map_disc():
    collect()
    harga= []
    for item in harga_temp:
        y = int(item)
        harga.append(y)
    disc = map(sum, zip(harga, temp_D))
    print('setelah diskon :')
    print(list(disc))

def repeat_harga():
    ListBuffer = itertools.cycle(harga_temp) 
    SequenceRepeation = 0
    SequenceStart = 0
    SequenceEnd = len(harga_temp) 
  
    for output in ListBuffer: 
        if(SequenceStart == 0): 
            print("Sequence % d"%(SequenceRepeation + 1)) 
        print(output, end =" ") 
        if(SequenceStart == SequenceEnd-1): 
            if(SequenceRepeation>= 1):
                break
            else: 
                SequenceRepeation+= 1
                SequenceStart = 0
                print("\n") 
        else: 
            SequenceStart+= 1
    print (list(itertools.repeat(harga_temp, 2)))

def group_by():
    L = zip(address_temp,city_temp)

    # Key function 
    key_func = lambda x: x[0] 
  
    for key, group in itertools.groupby(L, key_func): 
        print(key + " :", list(group))

def proceed_fil():
    print('1. lanjut mencari')
    print('2. kembali ke menu utama')
    print('3. keluar')
    pilq = input('input : ')
    if pilq == '1':
        inp()
        filtere()
    elif pilq == '2':
        clear_screen()
        main_menu()
    elif pilq == '3':
        clear_screen()
        sys.exit()
    else:
        clear_screen()
        proceed_fil()
        print('input invalid')
inx = ''
def inp():
    inx2 = input('masukan order_id yang akan dicari : ')
    global inx
    inx = inx2
def myFunc(x):
    if inx in x:
        return True
    else:
        return False
def filtere():
    y = 1
    fil = filter(myFunc, order_id_temp)
    

    for items in fil:
        if items == inx:
            print('ada')
            y = y+1
    if y == 2:
        proceed_fil()
    elif y == 1:
        print('tidak ada')
        proceed_fil()
    

def add_record():
    order_id1 = min(list_av)
    product1 = input('masukan nama_product : ')
    nama1 = input('masukan nama pemesan : ')
    phone1 = input('masukan nomor hp : ')
    address1 = input('masukan alamat : ')
    province1 = input('masukan provinsi : ')
    city1 = input('masukan kota : ')
    subdistrict1 = input('masukan kecamatan : ')
    kode_pos1 = input('masukan kode pos : ')
    product_price1 = input('masukan nilai pembelian : ')
    new_rec={
        "order_id": order_id1,
        "product": product1,
        "name": nama1,
        "phone": phone1,
        "address": address1,
        "province": province1,
        "city": city1,
        "subdistrict": subdistrict1,
        "zip": kode_pos1,
        "product_price": product_price1
    }
    list_av.remove(order_id1)
    new_key_rec = {"key_av": list_av}
    data['order_jam_tangan'].append(new_rec)
    with open('data_pembeli.json', 'w') as f:
        json.dump(data, f, indent=2)
    with open('data_unique_key.json', 'w') as f:
        json.dump(new_key_rec, f)

def delete_record():
    print('masukan order_id yang akan di delete')
    key = int(input())
    stat_key = 0
    y = 0
    index = 0
    for items in data['order_jam_tangan']:
        key_id_x = int(items['order_id'])
        if key_id_x == key:
            stat_key = 1
            index = y
        y = y+1
    if stat_key == 0 :
        print('id order tidak ditemukan')
        time.sleep(0.2)
        pilza = input('lanjutkan mencari ? (y/n) : ')
        if pilza == 'y' or pilza == 'Y':
            delete_record()
        elif pilza == 'n' or pilza == 'N':
            proceed()
    elif stat_key == 1 : 
        confirm = input('id order ditemukan, lanjutkan menghapus? (y/n) : ')
        if confirm == 'y' or confirm == 'Y':
            data_temp = data['order_jam_tangan']
            items = data_temp[index]
            data['order_jam_tangan'].remove(items)
            print('done, kembali ke main menu')
            with open('data_pembeli.json', 'w') as f:
                json.dump(data, f, indent = 2)
            time.sleep(0.2)
            clear_screen()
            main_menu()
        elif confirm == 'n' or confirm == 'N':
            print('ok understandable, have a nice day')
            proceed()

def update_record():
    data_temp = data["order_jam_tangan"]
    key_id = int(input('masukan order_id yang mau di update : ')) #order_id yang hendak diganti
    par = 0
    parx = -1
    for items in data['order_jam_tangan']:
        id_key = int(items['order_id'])
        if id_key == key_id:
            parx = par
        par = par + 1

    if parx == -1:
        print('id tidak ditemukan')
        proceed()

    elif parx > -1:
        print('id ditemukan, lanjut isikan data yang akan di update ? (y/n)')
        pilx_1 = input()
        if pilx_1 == 'y' or pilx_1 == 'Y':
            product1 = input('masukan nama_product : ')
            nama1 = input('masukan nama pemesan : ')
            phone1 = input('masukan nomor hp : ')
            address1 = input('masukan alamat : ')
            province1 = input('masukan provinsi : ')
            city1 = input('masukan kota : ')
            subdistrict1 = input('masukan kecamatan : ')
            kode_pos1 = input('masukan kode pos : ')
            product_price1 = input('masukan nilai pembelian : ')

            key_idx = str(key_id)

            new_rec={
            "order_id": key_idx,
            "product": product1,
            "name": nama1,
            "phone": phone1,
            "address": address1,
            "province": province1,
            "city": city1,
            "subdistrict": subdistrict1,
            "zip": kode_pos1,
            "product_price": product_price1
            }
            data_temp[parx] = new_rec
            data['order_jam_tangan'] = data_temp
            with open('data_pembeli.json', 'w') as f:
                json.dump(data, f, indent = 2)
            print('done')
        elif pilx_1 == 'n' or pilx_1 == 'N':
            proceed()
        
        

#------ fiture section end ------

#------ UI section ------

def preview_data():
    print('1. display all')
    print('2. city + province')
    print('3. city count by order')
    print('4. order_id sorted')
    print('5. nilai order')
    print('6. compress kode pos dan nama')
    print('7. name, country combination')
    print('8. repeat harga')
    print('9. address dan city')
    pil = int(input('masukan input : '))
    if pil == 1:
        for order1 in data['order_jam_tangan']:
            print(order1)
    elif pil == 2:
        chain_cityp()
    elif pil == 3:
        count_city()
    elif pil == 4:
        accumulatez()
    elif pil == 5:
        sortedx()
    elif pil == 6:
        compressx()
    elif pil == 7 :
        country_comb()
    elif pil == 8:
        repeat_harga()
    elif pil == 9:
        group_by()
    else:
        print('input invalid')
        preview_data()

def main_menu():
    print("Menu : ")
    print("1. Preview Data")
    print("2. Update Data")
    print("3. Delete Data")
    print("4. Add Data")
    print("5. Calculate Disount")
    print('6. Cek order')
    print("7. exit")
    pil = input('masukan pilihan : ')
    if pil == '1' :
        preview_data()
        proceed()
    elif pil == '2':
        update_record()
        proceed()
    elif pil == '3':
        delete_record()
    elif pil == '4':
        add_record()
        proceed()
    elif pil == '5':
        map_disc()
        proceed()
    elif pil == '6':
        proceed_fil()
    elif pil == '7':
        print('ok bye')
        clear_screen()
        sys.exit()
    else:
        print('input invalid')
        main_menu()

def main_exec():
    print("Data Administrator V1.0")
    pil1 = input("proceed to menu? (y/n) : ")
    if pil1 == 'y' or pil1 == 'Y':
        clear_screen()
        main_menu()
    elif pil1 =='n' or pil1 == 'N':
        print('ok bye')
        clear_screen()
        sys.exit()
    else :
        print('invalid_input')
        main_exec()

main_exec() #execute main function

#------ UI section end ------

#done : count(), chain(), lambda(), accumulate(), sorted(), permutation(), compress(), map(), group by(), combination(),repeat(), cycle(), filter