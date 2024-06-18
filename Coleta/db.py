import sqlite3

con = sqlite3.connect("data.db", check_same_thread=False)
cur = con.cursor()

def create_table_pontoColeta():
    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS pontoColeta (
                        PK_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                        STATE TEXT, 
                        CITY TEXT, 
                        TAGS TEXT, 
                        REPUTATION INTEGER,
                        NAME TEXT, 
                        ADDR TEXT, 
                        NUMBER TEXT
                                                            );""")
    except:
        print("erro ao criar a tabela de pontos de coletas")

def create_table_users():
    try:
        cur.execute("CREATE TABLE IF NOT EXISTS users(PK_CPF, EMAIL, HASH_PASSWORD, \
ID_PONTOS)")
    except:
        print("erro ao criar a tabela de usuarios")

def create_tables():
    create_table_pontoColeta()
    create_table_users()

def populate_test():
    print("teste")
    cur.execute("INSERT INTO pontoColeta VALUES \
                (1, 'SC', 'Blumenau', '10101001', 100, 'teste1', 'rua de teste', 612), \
                (2, 'SC', 'Blumenau', '10101001', 50, 'teste2', 'rua de merda', 624)")

    cur.execute("INSERT INTO users VALUES \
                ('123.456.789-10', 'memama@gmail.com', 'senhaBLA', 1), \
                ('098.765.432-10', 'memama@gmail.com', 'senhaBLABLA', 1)")

    con.commit()

def add_into_pontoColeta(name: str, address: str, address2: str, state:str, city:str, items: list[int]):
    items_string = ""
    for i in items:
        items_string += i

    print(name, address, address2, state, city, items, "BBBBBBBBBBBBBBBBBB")

    cur.execute(f"INSERT INTO pontoColeta (STATE, CITY, TAGS, REPUTATION, NAME, ADDR, NUMBER) VALUES\
    ('{state}', '{city}', '{items_string}', 100 ,'{name}', '{address}', '{address2}')")

    con.commit()    

def search_by_city(city: str):
    cur.execute(f"SELECT PK_ID FROM pontoColeta WHERE CITY='{city}'")
    lista = []
    result = cur.fetchall()

    for i in result:
        lista.append(i[0])
    return lista

def get_info(id: int):
    cur.execute(f"SELECT * FROM pontoColeta WHERE PK_ID='{id}'")
    return cur.fetchall()[0]

def search_and_get_by_city(city: str):
    cur.execute(f"SELECT * FROM pontoColeta WHERE CITY='{city}'")
    return cur.fetchall()

def make_dic_list(lista: list):
    list_return = []
    for card in lista:
        temp_dic = {
            'state':  card[1],
            'city':   card[2],
            'tags':   [int(i) for i in card[3]],
            'name':   card[5],
            'addr1':  card[6],
            'addr2':  card[7]
        }
        list_return.append(temp_dic)

    return list_return

create_tables()
# populate_test()
