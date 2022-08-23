import math

p_ii = 1
p_i = 1

while True:
    p_ii += 3
    p_i += p_ii

    t_d = 2 + p_ii % 9
    inc_pd = 3 * t_d + 12
    dif = p_i - t_d * (t_d - 1) / 6

    while t_d <= dif:
        if dif % t_d == 0:
            j = dif // t_d
            delta = 1 + 24*(j*(3*j-1) + p_i)
            s_d = math.sqrt(delta)

            if s_d * s_d == delta and s_d % 6 == 5:
                print(p_i)
                exit()

        if dif < inc_pd:
            break

        t_d += 9
        dif -= inc_pd
        inc_pd += 27
