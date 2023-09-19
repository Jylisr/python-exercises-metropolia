import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='12345'
)


def getairport(icao):
    sql = ('SELECT airport.ident, airport.name, airport.municipality, airport.iso_country, country.name FROM airport, country')
    sql += " WHERE airport.iso_country = country.iso_country AND ident ='" + icao + "'"
    cur = connection.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    if cur.rowcount > 0:
        for row in result:
            print(f"ICAO: {row[0]}, corresponds to {row[1]} in {row[2]}, {row[4]}, {row[3]}")
    else:
        print("Airport not found")
    return

icao = input("Enter ICAO: ")
getairport(icao)
