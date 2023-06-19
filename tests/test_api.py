user_agent = {'User-agent': 'Mozilla/5.0'}
    url = f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{symbol}?modules=price%2CsummaryDetail%2CpageViews%2CfinancialsTemplate"
    r = requests.get(url, headers=user_agent)

    # IMPRIME LO DEL LINK
    print(r.json())
