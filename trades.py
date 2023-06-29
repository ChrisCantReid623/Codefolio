success_rate = 0.02
failure_rate = 1 - success_rate

def probability(s_rate, f_rate, good_trades, trials):
    success = s_rate**good_trades
    failure = f_rate**(trials - good_trades)
    return success * failure
    
print(probability(success_rate, failure_rate, 4, 270))

    