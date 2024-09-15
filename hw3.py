import sqlite_lib

def check_winner(country, year):
    "SELECT song_name from eurovision_winners ew where country = 'Israel' "+\
        f"and year = 2024;"
    result = sqlite_lib.run_query_select(f"SELECT song_name from eurovision_winners ew where "+\
                                         f"country like '{country}' and year = {year};")
    # print(result)
    if result:
        return result[0][0]  # [(Toy,)]
    else:
        return "wrong"

def check_winner_filter(country, year):
    "SELECT song_name from eurovision_winners ew where country = 'Israel' "+\
        f"and year = 2024;"
    result_sql = sqlite_lib.run_query_select(f"SELECT song_name from eurovision_winners ew;")
    # print(result) [(), () ...]
    # for row in results:
    #     year, country, winner, host_country, song_name = row
    result = list(filter(lambda winner: winner[1] == country and winner[0] == year, result_sql))
    if result:
        return result[0][2]  # [(Toy,)]
    else:
        return "wrong"

def main():
    print(check_winner_filter('israel', 2018))
    sqlite_lib.connect('hw.db')
    country = input('country?')
    year = int(input('year?'))
    result = check_winner(country, year)
    print(result)
    sqlite_lib.close()

if __name__ == "__main__":
    main()