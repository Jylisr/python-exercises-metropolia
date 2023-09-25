import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='12345'
)


def getairport(iso):
    sql = ('SELECT airport.name, airport.type from airport where airport.iso_country = iso" order by airport.type)
    cur = connection.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    if cur.rowcount > 0:
        for row in result:
            print(f"Airports in: {icao} {row[0]} {row[1]}")
    else:
        print("Airport not found")
    return

iso = input("Enter country iso: ")
getairport(iso)