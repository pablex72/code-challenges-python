def quarter_of(month):
    year_quarters ={1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9], 4: [10, 11, 12]}   
    for k, v in year_quarters.items():
        if month in v:
            return k