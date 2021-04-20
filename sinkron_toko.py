import pymysql
import time
import json
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

folder_bank = '1utm8XGBRgxW7xFE6OcEwwV_ymxqCw17F'
bank_done = '1zK9xKerS0bEtLhyEXRq3yoYmWT1cmpDc'
folder_toko = '18bGpLejuSN86BnJZg9b2UpOYQVI8JqcO'
toko_done = '1134z4zcMULA1Nveyza3ORXrjvGLolUop'

first_boot = 1

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)


def fileOperation(table, data, filename, operation, gauth):
    try:
        print("-- PROCESS %s --" % filename)

        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)
        try:
            filepath = './bankbackup/' + filename
            with open(filepath, 'r') as f:
                try:
                    datajson = json.load(f)
                except:
                    datajson = {}
                    datajson[table] = []
        except:
            datajson = {}
            datajson[table] = []
        if(operation != "delete"):
            datajson[table].append({
                'operation': operation,
                'id_transaksi': str(data[0]),
                'rekening': str(data[1]),
                'tanggal': str(data[2]),
                'total': str(data[3]),
                'status': str(data[4]),
                'action': str(data[5])
            })
        else:
            datajson[table].append({
                'operation': operation,
                'id_transaksi': str(data[0])
            })
        with open(filepath, 'w') as outfile:
            json.dump(datajson, outfile)

        file_list = drive.ListFile(
            {'q': "'%s' in parents" % folder_bank}).GetList()
        try:
            for file1 in file_list:
                if file1['title'] == filename:
                    file1.Delete()
        except:
            pass

        print("-- UPDATE %s --" % filename)
        file_u = drive.CreateFile({'title': filename, 'parents': [
                                  {"kind": "drive#fileLink", "id": folder_bank}]})
        file_u.SetContentString(json.dumps(datajson))
        file_u.Upload()

    except(pymysql.Error, pymysql.Warning) as e:
        print(e)

    return 1


while (1):
    first_boot = 1
    try:
        connection_to_bank = 1
        try:
            connToko = pymysql.connect(
                host='localhost', user='root', passwd='', db='db_toko3')
            curToko = connToko.cursor()
        except:
            print("can't connect to TOKO")
        try:
            connBank = pymysql.connect(
                host='localhost', user='root', passwd='', db='db_bank3')
            curBank = connBank.cursor()
        except:
            print("can't connect to BANK")
            connection_to_bank = 0

        # read data dari json history toko saat first boot
        while (first_boot):
            try:
                file_list = drive.ListFile(
                    {'q': "'%s' in parents" % folder_toko}).GetList()
                try:
                    for file1 in file_list:
                        if "toko_" in file1['title']:
                            file1.GetContentFile(file1['title'])
                            file1.Delete()
                            with open(file1['title'], 'r') as f:
                                json_dict = json.load(f)
                                print('-- LOADING JSON FILE --')
                            for jsonData in json_dict['tb_history']:
                                if (jsonData['operation'] != 'delete'):
                                    data = []
                                    data.append(jsonData['id_transaksi'])
                                    data.append(jsonData['rekening'])
                                    data.append(jsonData['tanggal'])
                                    data.append(jsonData['total'])
                                    data.append(jsonData['status'])
                                    data.append(jsonData['action'])

                                    if (jsonData['operation'] == 'insert'):
                                        val = (data[0], data[1],
                                               data[2], data[3], data[4])

                                        insert_integrasi_toko = "insert into tb_history (id_transaksi, rekening, tanggal, total, status, action) values(%s,%s,%s,%s,%s,%s)"
                                        curToko.execute(
                                            insert_integrasi_toko, val)
                                        connToko.commit()

                                        insert_transaksi_toko = "insert into tb_transaksi (id_transaksi, rekening, tanggal, total, status) values(%s,%s,%s,%s,%s)"
                                        curToko.execute(
                                            insert_transaksi_toko, val)
                                        connToko.commit()
                                        print(
                                            '- insert data from json file - id_transaksi = %s' % jsonData['id_transaksi'])

                                    if (jsonData['operation'] == 'update'):
                                        val = (data[1], data[2],
                                               data[3], data[4], data[0])

                                        update_integrasi_toko = "update tb_history set rekening = %s, tanggal = %s, total = %s, status = %s, action = %s where id_transaksi = %s"
                                        curToko.execute(
                                            update_integrasi_toko, val)
                                        connToko.commit()

                                        update_transaksi_toko = "update tb_transaksi set rekening = %s, tanggal = %s, total = %s, status = %s where id_transaksi = %s"
                                        curToko.execute(
                                            update_transaksi_toko, val)
                                        connToko.commit()
                                        print(
                                            '- update data from json file - id_transaksi = %s' % jsonData['id_transaksi'])
                                else:
                                    data = []
                                    data.append(jsonData['id_transaksi'])
                                    val = (data[0])

                                    delete_integrasi_toko = "delete from tb_history where id_transaksi = %s"
                                    curToko.execute(delete_integrasi_toko, val)
                                    connToko.commit()

                                    delete_transaksi_toko = "delete from tb_transaksi where id_transaksi = %s"
                                    curToko.execute(delete_transaksi_toko, val)
                                    connToko.commit()
                                    print('- delete data from json file - %s' %
                                          jsonData['id_transaksi'])

                            folderName = 'tokodone'
                            folders = drive.ListFile(
                                {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
                            for folder in folders:
                                if folder['title'] == folderName:
                                    filename2 = file1['title']
                                    file2 = drive.CreateFile(
                                        {'parents': [{"kind": "drive#fileLink", "id": toko_done}]})
                                    file2.SetContentFile(filename2)
                                    file2.Upload()
                                    print('-- DONE LOADING JSON FILE --')
                except:
                    pass
            except:
                print('-- TIDAK TERDAPAT INTEGRASI --')
            first_boot = 0

        sql_select = "SELECT * FROM tb_transaksi"
        curToko.execute(sql_select)
        result = curToko.fetchall()

        sql_select = "SELECT * FROM tb_history"
        curToko.execute(sql_select)
        integrasi = curToko.fetchall()

        # insert listener
        if (len(result) > len(integrasi)):
            print("-- INSERT DETECTED --")
            for data in result:
                a = 0
                for dataIntegrasi in integrasi:
                    if (data[0] == dataIntegrasi[0]):
                        a = 1
                if (a == 0):
                    print("-- RUN INSERT FOR ID = %s" % (data[0]))
                    val = (data[0], data[1], data[2], data[3], data[4])
                    insert_integrasi_toko = "insert into tb_history (id_transaksi, rekening, tanggal, total, status, action) values(%s,%s,%s,%s,%s,%s)"
                    curToko.execute(insert_integrasi_toko, val)
                    connToko.commit()
                    if (connection_to_bank == 1):
                        timestr = time.strftime("%Y%m%d-%H%M%S")
                        backupfile = 'bank_' + timestr + '.json'
                        fileOperation('tb_history', data,
                                      backupfile, 'insert', gauth)
                    else:
                        timestr = time.strftime("%Y%m%d-%H%M%S")
                        backupfile = 'bank_'+timestr + '.json'
                        fileOperation('tb_history', data,
                                      backupfile, 'insert', gauth)

        # delete listener
        if (len(result) < len(integrasi)):
            print("-- DELETE DETECTED --")
            for dataIntegrasi in integrasi:
                a = 0
                for data in result:
                    if (dataIntegrasi[0] == data[0]):
                        a = 1
                if (a == 0):
                    print("-- RUN DELETE FOR ID = %s" % (dataIntegrasi[0]))
                    delete_integrasi_toko = "delete from tb_history where id_transaksi = '%s'" % (
                        dataIntegrasi[0])
                    curToko.execute(delete_integrasi_toko)
                    connToko.commit()

                    if (connection_to_bank == 1):
                        timestr = time.strftime("%Y%m%d-%H%M%S")
                        backupfile = 'bank_' + timestr + '.json'
                        fileOperation('tb_history', dataIntegrasi,
                                      backupfile, 'delete', gauth)
                    else:
                        timestr = time.strftime("%Y%m%d-%H%M%S")
                        backupfile = 'bank_' + timestr + '.json'
                        fileOperation('tb_history', dataIntegrasi,
                                      backupfile, 'delete', gauth)

        # update listener
        if (result != integrasi):
            print("-- EVENT SUCCESS OR UPDATE DETECTED --")
            for data in result:
                for dataIntegrasi in integrasi:
                    if (data[0] == dataIntegrasi[0]):
                        if (data != dataIntegrasi):
                            val = (data[1], data[2], data[3], data[4], data[0])
                            update_integrasi_toko = "update tb_history set rekening = %s, tanggal = %s, total = %s, status = %s, action = %s where id_transaksi = %s"
                            curToko.execute(update_integrasi_toko, val)
                            connToko.commit()

                            if (connection_to_bank == 1):
                                timestr = time.strftime("%Y%m%d-%H%M%S")
                                backupfile = 'bank_' + timestr + '.json'
                                fileOperation('tb_history', data,
                                              backupfile, 'update', gauth)
                            else:
                                timestr = time.strftime("%Y%m%d-%H%M%S")
                                backupfile = 'bank_' + timestr + '.json'
                                fileOperation('tb_history', data,
                                              backupfile, 'update', gauth)

    except(pymysql.Error, pymysql.Warning) as e:
        print(e)

    # Untuk delay
    time.sleep(1)
