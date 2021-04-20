import time
import helper
import config

print("Start Engine")
while (1):
    conn_toko = helper.connect_db(config.DB_TOKO)
    conn_bank = helper.connect_db(config.DB_BANK)
    cur_toko = conn_toko.cursor()
    cur_bank = conn_bank.cursor()

    query = "SELECT * FROM tb_transaksi"
    cur_toko.execute(query)
    transaksi = cur_toko.fetchall()

    query = "SELECT * FROM tb_history"
    cur_toko.execute(query)
    integrasi = cur_toko.fetchall()

    # get update
    print('get update')
    for data_transaksi in transaksi:
        query = "SELECT * FROM tb_history WHERE id_transaksi = %s AND sumber = 'bank' ORDER BY id_history DESC LIMIT 1"
        cur_toko.execute(query, data_transaksi[0])
        history = cur_toko.fetchone()

        if history is None:
            continue

        if (data_transaksi[4] != history[5]):
            print("Update id %s" % (data_transaksi[0]))
            data = (history[5], history[1])
            query = "UPDATE tb_transaksi SET status = %s where id_transaksi = %s"
            cur_toko.execute(query, data)
            conn_toko.commit()

    query = "SELECT * FROM tb_transaksi"
    cur_toko.execute(query)
    transaksi = cur_toko.fetchall()

    query = "SELECT * FROM tb_history"
    cur_toko.execute(query)
    integrasi = cur_toko.fetchall()

    # insert
    print('find insert')
    for data_transaksi in transaksi:
        is_sync = 0
        for data_integrasi in integrasi:
            if (data_transaksi[0] == data_integrasi[1]):
                is_sync = 1
        if (is_sync == 0):
            print("Insert id %s to history" % (data_transaksi[0]))

            data = (data_transaksi[0], config.KODE_TOKO, data_transaksi[1],
                    data_transaksi[2], data_transaksi[3], data_transaksi[4])

            query = "INSERT INTO tb_history (`id_transaksi`, `rekening`, `tanggal`, `total`, `status`, `action`, `created_at`, `sumber`) VALUES (%s,%s,%s,%s,%s,'insert', NOW(), 'toko')"
            cur_toko.execute(query, data_transaksi)
            conn_toko.commit()

            query = "INSERT INTO tb_history (`id_transaksi`, `kode_toko`, `rekening`, `tanggal`, `total`, `status`, `action`, `created_at`, `sumber`) VALUES (%s,%s,%s,%s,%s,%s,'insert', NOW(), 'toko')"
            cur_bank.execute(query, data)
            conn_bank.commit()

    # delete
    print('find delete')
    for data_integrasi in integrasi:
        is_sync = 0
        for data_transaksi in transaksi:
            if (data_integrasi[1] == data_transaksi[0]):
                is_sync = 1

        query = "SELECT id_transaksi, action FROM tb_history WHERE id_transaksi = %s"
        cur_toko.execute(query, data_integrasi[1])
        actions = cur_toko.fetchall()

        if actions is None:
            continue

        for action in actions:
            if (action[1] == 'delete'):
                is_sync = 1

        if (is_sync == 0):
            print("Delete id %s to history" % (data_integrasi[1]))

            data = (data_integrasi[1], data_integrasi[2],
                    data_integrasi[3], data_integrasi[4], data_integrasi[5])
            data_kode = (data_integrasi[1], config.KODE_TOKO, data_integrasi[2],
                         data_integrasi[3], data_integrasi[4], data_integrasi[5])

            query = "INSERT INTO tb_history (`id_transaksi`, `rekening`, `tanggal`, `total`, `status`, `action`, `created_at`, `sumber`) VALUES (%s,%s,%s,%s,%s,'delete', NOW(), 'toko')"
            cur_toko.execute(query, data)
            conn_toko.commit()

            query = "INSERT INTO tb_history (`id_transaksi`, `kode_toko`, `rekening`, `tanggal`, `total`, `status`, `action`, `created_at`, `sumber`) VALUES (%s,%s,%s,%s,%s,%s,'delete', NOW(), 'toko')"
            cur_bank.execute(query, data_kode)
            conn_bank.commit()

    # update
    print('find update')
    for data_transaksi in transaksi:
        query = "SELECT * FROM tb_history WHERE id_transaksi = %s ORDER BY id_history DESC LIMIT 1"
        cur_toko.execute(query, data_transaksi[0])
        history = cur_toko.fetchall()
        for data_history in history:
            if ((data_transaksi[1] != data_history[2]) or (data_transaksi[2] != data_history[3]) or (data_transaksi[3] != data_history[4])):
                print("Update id %s  to history" % (data_transaksi[0]))

                data = (data_transaksi[0], config.KODE_TOKO, data_transaksi[1],
                        data_transaksi[2], data_transaksi[3], data_transaksi[4])

                query = "INSERT INTO tb_history (`id_transaksi`, `rekening`, `tanggal`, `total`, `status`, `action`, `created_at`, `sumber`) VALUES (%s,%s,%s,%s,%s,'update', NOW(), 'toko')"
                cur_toko.execute(query, data_transaksi)
                conn_toko.commit()

                query = "INSERT INTO tb_history (`id_transaksi`, `kode_toko`, `rekening`, `tanggal`, `total`, `status`, `action`, `created_at`, `sumber`) VALUES (%s,%s,%s,%s,%s,%s,'update', NOW(), 'toko')"
                cur_bank.execute(query, data)
                conn_bank.commit()

    print('done')

    cur_toko.close()
    cur_bank.close()

    time.sleep(config.DELAY1)
