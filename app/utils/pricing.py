def calculate_price(cost, shipping):
    p = cost * 1.5

    while True:
        fee = 0.029 * p + 0.30
        gst = 0.1 * p
        landed = cost + shipping + fee + gst
        margin = (p - landed) / p

        if margin >= 0.25:
            break
        p += 0.1

    return round(p * 2) / 2