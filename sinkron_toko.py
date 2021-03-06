import pymysql
import time
import config
import json

# CONNECT TO DATABASE
db_toko = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='db_toko3',
    cursorclass=pymysql.cursors.DictCursor
)
cursor_toko = db_toko.cursor()


def create_json():
    print("========================CREATE JSON========================")
    data = {}

    data_tb_integrasi = 'SELECT * FROM tb_transaksi'
    cursor_toko.execute(data_tb_integrasi)
    result_data_tb_integrasi = cursor_toko.fetchall()
    db_toko.commit()

    data['tb_transaksi'] = []
    for dataIntegrasi in result_data_tb_integrasi:
        data['tb_transaksi'].append({
            'id_transaksi': str(dataIntegrasi['id_transaksi']),
            'kode_toko': config.KODE_TOKO,
            'rekening': str(dataIntegrasi['rekening']),
            'tanggal': str(dataIntegrasi['tanggal']),
            'total': str(dataIntegrasi['total']),
            'status': str(dataIntegrasi['status'])
        })
    writer = open('toko.json', 'w')
    writer.write(json.dumps(data, indent=4))
    writer.close()
    print('==> SUCCESS CREATE FILE TOKO.json')
    exit_fun()


def cek_data():
    print("========================CHECK DATA========================")
    error = 0
    db_toko.commit()
    jumlah_data_transaksi = "SELECT COUNT(id_transaksi) as 'jumlah' FROM tb_transaksi"
    select_data_transaksi = "SELECT * FROM tb_transaksi"
    cursor_toko.execute(select_data_transaksi)
    data_db = cursor_toko.fetchall()
    cursor_toko.execute(jumlah_data_transaksi)
    jumlah = cursor_toko.fetchall()
    print("==> CHECKS DATABASE")
    i = 0
    with open('bank.json') as toko_json:
        data = json.load(toko_json)
        error += 1
        message = "=====> TOTAL DATA TRANSACTION IN TABLE AND JSON FILE IS DIFFERENT, DATABASE = '%s' BANK.json = '%s'" % (
            jumlah[0]['jumlah'], len(data['tb_transaksi']))
        print(message)
        for datacek in data['tb_transaksi']:
            if(jumlah[0]['jumlah'] == 0):
                error += 1
                message = "=====> NO DATA IN TB_TRANSAKSI DATABASE"
                print(message)
                break
            if(str(data_db[i]['id_transaksi']) != str(datacek['id_transaksi'])):
                error += 1
                message = "=====> DIFFERENT DATA DETECTED !!, ID_TRANSAKSI DATABASE = '%s' ID_TRANSAKSI TOKO.json = '%s'" % (
                    data_db[i]['id_transaksi'], datacek['id_transaksi'])
                print(message)
            if(str(data_db[i]['rekening']) != str(datacek['rekening'])):
                error += 1
                message = "=====> DIFFERENT DATA DETECTED !!, NO_REKENING DATABASE = '%s' NO_REKENING TOKO.json = '%s' WHERE ID_TRANSAKSI = '%s'" % (
                    data_db[i]['rekening'], datacek['rekening'], data_db[i]['id_transaksi'])
                print(message)
            if(str(data_db[i]['tanggal']) != str(datacek['tanggal'])):
                error += 1
                message = "=====> DIFFERENT DATA DETECTED !!, TGL_TRANSAKSI DATABASE = '%s' TGL_TRANSAKSI TOKO.json = '%s' WHERE ID_TRANSAKSI = '%s'" % (
                    data_db[i]['tanggal'], datacek['tanggal'], data_db[i]['id_transaksi'])
                print(message)
            if(str(data_db[i]['total']) != str(datacek['total'])):
                error += 1
                message = "=====> DIFFERENT DATA DETECTED !!, TOTAL_TRANSAKSI DATABASE = '%s' TOTAL_TRANSAKSI TOKO.json = '%s' WHERE ID_TRANSAKSI = '%s'" % (
                    data_db[i]['total'], datacek['total'], data_db[i]['id_transaksi'])
                print(message)
            if(str(data_db[i]['status']) != str(datacek['status'])):
                error += 1
                message = "=====> DIFFERENT DATA DETECTED !!, STATUS DATABASE = '%s' STATUS TOKO.json = '%s' WHERE ID_TRANSAKSI = '%s'" % (
                    data_db[i]['status'], datacek['status'], datacek['id_transaksi'])
                print(message)
            if(i+1 == jumlah[0]['jumlah']):
                error += 1
                message = "=====> %s DATA NOT MATCHED IN TOKO.json" % (
                    len(data['tb_transaksi']) - jumlah[0]['jumlah'])
                print(message)
                break
            i = i + 1
        if(len(data['tb_transaksi']) - jumlah[0]['jumlah'] < 0):
            message = "=====> %s DATA NOT MATCHED IN DATABASE BANK" % (
                jumlah[0]['jumlah'] - len(data['tb_transaksi']))
            print(message)
        else:
            message = "=====> TOTAL DATA TRANSACTION AND TABLE BANK.json = %s " % (
                jumlah[0]['jumlah'])
            print(message)

            i = 0
            for datacek in data['tb_transaksi']:
                if(str(data_db[i]['id_transaksi']) != str(datacek['id_transaksi'])):
                    error += 1
                    message = "=====> DIFFERENT DATA DETECTED !!, ID_TRANSAKSI DATABASE = '%s' ID_TRANSAKSI TOKO.json = '%s'" % (
                        data_db[i]['id_transaksi'], datacek['id_transaksi'])
                    print(message)
                if(str(data_db[i]['rekening']) != str(datacek['rekening'])):
                    error += 1
                    message = "=====> DIFFERENT DATA DETECTED !!, NO_REKENING DATABASE = '%s' NO_REKENING TOKO.json = '%s' WHERE ID_TRANSAKSI = '%s'" % (
                        data_db[i]['rekening'], datacek['rekening'], data_db[i]['id_transaksi'])
                    print(message)
                if(str(data_db[i]['tanggal']) != str(datacek['tanggal'])):
                    error += 1
                    message = message = "===> DIFFERENT DATA DETECTED !!, TGL_TRANSAKSI DATABASE = '%s' TGL_TRANSAKSI TOKO.json = '%s' WHERE ID_TRANSAKSI = '%s'" % (
                        data_db[i]['tanggal'], datacek['tanggal'], data_db[i]['id_transaksi'])
                    print(message)
                if(str(data_db[i]['total']) != str(datacek['total'])):
                    error += 1
                    message = "=====> DIFFERENT DATA DETECTED !!, TOTAL_TRANSAKSI DATABASE = '%s' TOTAL_TRANSAKSI TOKO.json = '%s' WHERE ID_TRANSAKSI = '%s'" % (
                        data_db[i]['total'], datacek['total'], data_db[i]['id_transaksi'])
                    print(message)
                if(str(data_db[i]['status']) != str(datacek['status'])):
                    error += 1
                    message = "=====> DIFFERENT DATA DETECTED !!, STATUS DATABASE = '%s' STATUS TOKO.json = '%s' WHERE ID_TRANSAKSI = '%s'" % (
                        data_db[i]['status'], datacek['status'], datacek['id_transaksi'])
                    print(message)
                i = i + 1
            if (error == 0):
                print("=====> DIFFERENT DATA NOT FOUND")
            elif(error > 0):
                print("=====> DATABASE IS NOT INTEGRATED, READ TOKO.json !")
        exit_fun()


def read_json():
    print("========================READ JSON========================")
    print('==> READ BANK.JSON')
    db_toko.commit()
    with open('bank.json') as toko_json:
        data = json.load(toko_json)
        toko_list = []
        for transaksi in data['tb_transaksi']:
            toko_list.append(transaksi['id_transaksi'])
            select_transaksi = "SELECT * FROM tb_transaksi WHERE id_transaksi = '%s'" % (
                transaksi['id_transaksi'])
            cursor_toko.execute(select_transaksi)
            result_transaksi_db = cursor_toko.fetchone()
            #	INTEGRATE !!!!
            if type(result_transaksi_db) is type(None):
                insert_transaksi = "INSERT INTO tb_transaksi values('%s','%s','%s','%s','%s')" % (
                    transaksi['id_transaksi'], transaksi['rekening'], transaksi['tanggal'], transaksi['total'], transaksi['status'])
                cursor_toko.execute(insert_transaksi)
                insert_integrasi = "INSERT INTO tb_history values('%s','%s','%s','%s','%s')" % (
                    transaksi['id_transaksi'], transaksi['rekening'], transaksi['tanggal'], transaksi['total'], transaksi['status'])
                cursor_toko.execute(insert_integrasi)
                db_toko.commit()
                message = ("=====>INSERT NEW DATA INTO TB_INTEGRATED TOKO WITH ID = %s FROM TOKO.json") % (
                    transaksi['id_transaksi'])
                print(message)

            #	CEK TIAP KOLOM DATA
            else:
                if str(result_transaksi_db['status']) != str(transaksi['status']):
                    message = ("=====>UPDATE DATA IN TB_INTEGRATE, SET '%s' TO '%s WHERE TB_INTEGRATE ID = '%s'") % (
                        result_transaksi_db['status'], transaksi['status'], transaksi['id_transaksi'])
                    print(message)
                    update_transaksi_bank = "UPDATE tb_transaksi SET tb_transaksi.status = '%s' WHERE tb_transaksi.id_transaksi = '%s'" % (
                        transaksi['status'], transaksi['id_transaksi'])
                    cursor_toko.execute(update_transaksi_bank)
                    db_toko.commit()

    print('=====> INTEGRATED SUCCESS')
    exit_fun()


def menu():
    print("========================TOKO ENGINE MENU========================")
    print("===> ENGINE BACKUP DATABASE")
    print("=====> 1. CHECKS DATABASE DATA WITH BANK.json FILE")
    print("=====> 2. INTEGRATE DATA WITH BANK.json FILE")
    print("=====> 3. CREATE BACK UP DATA")
    print("=====> 4. EXIT")
    opsi = str(input("=====>ENTER : "))

    if (opsi == '1'):
        print("\n\n")
        cek_data()
    elif (opsi == '2'):
        print("\n\n")
        read_json()
    elif (opsi == '3'):
        print("\n\n")
        create_json()
    elif (opsi == '4'):
        print("\n\n")
        exit()
    else:
        print("TRY AGAIN\n\n")
        time.sleep(1)
        menu()


def exit_fun():
    time.sleep(3)
    print("========================TOKO ENGINE========================")
    print("===> CONTINUE / QUIT ?")
    print("=====> 1. CONTINUE")
    print("=====> 2. QUIT")
    opsi = str(input("=====> ENTER : "))
    if(opsi == '2'):
        print("BYE")
        exit()
    elif(opsi == '1'):
        menu()
    else:
        exit_fun()


menu()
