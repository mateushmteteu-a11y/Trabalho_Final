from conector import conectar
def executar(sql, params=None, fetch=False):

    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute(sql, params or ())
    

    resultado = None

    if fetch:
        resultado = cursor.fetchall()

    conexao.commit()

    cursor.close()
    conexao.close()

    return resultado