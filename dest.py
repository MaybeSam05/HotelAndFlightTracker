import airportsdata


airport_dict = [[1, "Paris, France"],
            [2, "Rome, Italy"],
            [3, "London, England"],
            [4, "Tokyo, Japan"],
            [5, "Amsterdam, Netherlands"],
            [6, "Barcelona, Spain"],
            [7, "Sydney, Austraila"],
            [8, "Dubai, UAE"],
            [9, "New York City, New York"],
            [10, "Florence, Italy"],
            [11, "Rio de Janeiro, Brazil"],
            [12, "Prague, Czech Republic"],
            [13, "Vancouver, Canada"],
            [14, "Bangkok, Thailand"],
            [15, "Los Angeles, California"]]

airport_code_list = [[1, "CDG"],
            [2, "FCO", "IT"],
            [3, "LHR", "GB"],
            [4, "HND", "JP"],
            [5, "AMS", "NL"],
            [6, "BCN", "ES"],
            [7, "SYD", "AU"],
            [8, "DXB", "AE"],
            [9, "JFK", "US"],
            [10, "FLR", "IT"],
            [11, "GIG", "BR"],
            [12, "PRG", "CZ"],
            [13, "YVR", "CA"],
            [14, "BKK", "TH"],
            [15, "LAX", "US"]]

airports = airportsdata.load('IATA')
airports = {code: info for code, info in airports.items() if info['country'] == 'US'}
allports = airportsdata.load('IATA')



