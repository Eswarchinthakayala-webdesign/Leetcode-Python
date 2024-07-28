min_price,max_profit=10**4,0
    for price in prices:
        if price<min_price:
            min_price=price
        elif price-min_price>max_profit:
            max_profit=price-min_price
    return max_profit
