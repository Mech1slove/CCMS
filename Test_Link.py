import math
import sqlite3
#from sympy import symbols, solve, parse_expr, simplify



def Volume_buff(dc,dh,Kp,lb, L, Lver): # Объём буферной жидкости
    '''
    :param dc: диаметр скважины
    :param dh: внешний диаметр колонны
    :param Kp: коэффициент резерва
    :param lb: высота столба буферной жидкости в кольцевом пространстве
    :return: объем буферной жидкости для колонн
    '''
    a = L/Lver
    Vb = 0.785 * a * ( math.pow(dc, 2) - math.pow(dh, 2) ) * Kp * lb * math.pow(10,-6)
    return round(Vb, 3)

def outer_space_simple(Lver,L,lb,dc1,Kav,dh1,di,stak, Klos, density, n, name): # масса цемента для направления
    '''
    :param lb1: интервал цементирования
    :param klos: коэффициент потерь цемента
    :param dc1: Диаметр долота
    :param Kav: коэффициент каверзности
    :param dh1: внешний диаметр скважины
    :param di: внутренний диаметр колонны
    :param stak: длина цементного стакана
    :param L: длина скважины по Оси
    :param Lver: длина скважины по вертикали
    :return:
    '''
    switch_type_book = ["Направление", "Кондуктор", "Промежуточная кол.", "Эксплуатационная кол.", "Хвостовик"]
    a = L/Lver # отношение длины скважины к её глубине
    OUT = 0.785 * lb * a * (math.pow(dc1*math.sqrt(Kav), 2) - math.pow(dh1, 2)) * math.pow(10, -6) #объём заколонного пространства
    stakvol = 0.785 * stak * math.pow(di, 2) * math.pow(10, -6) #объём цементного стакана
    summ = OUT + stakvol #суммарный объём
    q = density/(1+n)  #количество цемента для приготовления одного м3 тампонажного раствора
    cem = round(summ * q * Klos, 3) #общая масса цемента для с учётом потерь
    FK = OUT / (lb * a)
    FT = stakvol / stak
    F0 = FK / FT
    F1 = FT / FK
    mass = [summ, OUT, stakvol, cem, F1, F0]
    return mass







def outer_space(lb,lb1,dc,dc1,Kav,dh,di,stak, Klos, density, n, L, Lver, lb_cem): # масса цемента
    '''
    :param lb: длина предыдущей колонны
    :param lb1: длина текущей колонны
    :param klos: коэффициент потерь цемента
    :param dc: внутренний диаметр предыдущей колонны
    :param dc1: диаметр долота
    :param Kav: коэффициент каверзности
    :param dh: внешний диаметр обсадной колонны текущей
    :param di: внутренний диаметр колонны
    :param stak: длина цементного стакана
    :param lb_cem: интервал цементирования
    :return:
    '''
    # необходимо прописать условие учитывающее выбранный интервал цементирования и его длинну
    a = L/Lver
    lb_int = lb1 - lb
    OUT = round(0.785 * a * lb * (math.pow(dc, 2) - math.pow(dh, 2)) * math.pow(10, -6), 3)
    OUT1 = round(0.785 * a * lb_cem * (math.pow(dc1*math.sqrt(Kav), 2) - math.pow(dh, 2)) * math.pow(10, -6), 3)
    stakvol = round(0.785 * stak * math.pow(di, 2) * math.pow(10, -6), 3)
    summ = round(OUT + OUT1 + stakvol, 3)
    q = density/(1+n)
    cem = round(summ * q * Klos, 3)

    FKdown = 0.785 * (math.pow(dc1*math.sqrt(Kav), 2) - math.pow(dh, 2)) * math.pow(10, -6) # Площадь сечения кольцевого пространства внизу
    FKupper = round(0.785 * (math.pow(dc, 2) - math.pow(dh, 2)) * math.pow(10, -6), 3) # Площадь сечения кольцевого пространства сверху
    FT = round(0.785 * math.pow(di, 2) * math.pow(10, -6), 3) # Площадь внутреннего сечения обсадной колонны
    F0 = FKdown / FKupper #
    F1 = FKdown / FT #
    F2 = FKupper / FT #

    mass = [summ, OUT, stakvol, cem, OUT, F2, F0, F1, OUT1]

    return mass

def volume_water(n, OUT1, den):
    '''
    :param n: водоцементное отношение
    :param OUT1: объём
    :param den: плотность цемента
    :return:
    '''
    q= den/(1+n)
    WV = n * OUT1 * q
    return round(WV, 3)

def push_volume(Kcprod, di1, Lc, stakan2): # объём продавочной жидкости
    """

    :param Kcprod: коэффициент резерва продавочной жидкости
    :param di1: внутренницй диаметр колонны
    :param Lc: длинна колонны по оси
    :param stakan2: высота стакана
    :return:
    """
    Column_volume = round(0.785  * math.pow(di1, 2) * (Lc) * math.pow(10, -6), 3)
    Vprod = round( 0.785 * Kcprod * math.pow(di1, 2) * (Lc - stakan2) * math.pow(10, -6), 3)
    return [Vprod, Column_volume]

def Qpod(Vcr, Vstak, Hcr, V): # Скорость подачи насосов (не актуально)
    """
    :param Vcr: Объём заколонного пространства с учётом цем. стакана
    :param Vstak: Объём стакана
    :param Hcr: Интервал цементирования ???
    :param V: Скорость в затрубном пространстве
    :return:
    """
    Pzagr = (Vcr - Vstak) / Hcr
    Q = Pzagr * V
    return round(Q, 3)


def PMAX(H, h, pcr, ppr, dv2, n, Q, L, dc, dh, t0): # максимальное давление в устье скважины (не актуально)
    '''
    :param H:  интервал цементирования
    :param h:  высота цементного стакана
    :param pcr:  плотность цементного раствора
    :param ppr:  плотность продавочной жидкости
    :param dv2:  внутренний диаметр колонны
    :param n: пластическая вязкость
    :param Q: расход продавочной жидкости
    :param L: длинна обсадной колонны
    :param dc: диаметр скважины
    :param dh:  внешний диаметр обсадной колонны
    :param t0: Динамическое напряжение сдвига
    :return:
    '''
    Pp = (H - h) * (pcr - ppr) * 9.81

    Ret =  4 * ppr * Q / 3.14 * dv2 * n
    lamt = 0.1 * math.pow( ( (1.46 * 3 * 0.0001 / dv2) + (100 / Ret) ), 0.25)
    Ptr = lamt * ( (8 * ppr * math.pow(Q, 2) * L) / (math.pow(3.14, 2) * math.pow(dv2,5) ) )
#
    Rekp = 4 * ppr * Q / 3.14 * (dc + dh) * n
    lamt1 = 0.107 * math.pow( (1.46 * 3 * 0.0001 / (dc - dh) + (100 / Rekp) ), 0.25 )
    Pkp = lamt1 * (8 * ppr * math.pow(Q, 2) * L) / ( 3.14 * (dc + dh) * math.pow( (dc-dh) ,2) )

    Rekr = 2100 + 7.3 * math.pow((pcr * math.pow( (dc-dh), 2) * t0 ) , 0.58)
    Rekp_cem = 4 * pcr * Q / 3.14 * (dc + dh) * n
    if Rekp_cem < Rekr:
        lamif = 0.107 * math.pow( (1.46 * 3 * 0.0001 / (dc - dh) + (100 / Rekp_cem) ), 0.25 )
        Pkpif = lamif * (8 * ppr * math.pow(Q, 2) * L) / ( 3.14 * (dc + dh) * math.pow( (dc-dh) ,2) )
    else:
        Pkpif = 0.0

    Pk = (Pp + Ptr + Pkp + Pkpif)
    all1 = [Pp, Ret, lamt, Ptr, Rekp, lamt1, Pkp, Rekr, Rekp_cem, Pk]
    return round(Pk, 3)


def bethas(t0, Dc, Dout, d, viscosity, Q):
    #Dc, Dout, d = math.pow(10, -3) * Dc, Dout * math.pow(10, -3), d * math.pow(10, -3)
    spd_tube = 4 * Q / (math.pi * math.pow(d, 2)) # Скорость Нисходящего потока
    spd_out = 4 * Q / (math.pi * (math.pow(Dc, 2) - math.pow(Dout, 2))) # Скорость восходящего потока
    Se = round(math.pow(10, -3)*(t0 * d / (viscosity * spd_tube)), 2)
    SeK = round(t0 * (Dc - Dout) / (viscosity * spd_out), 2)

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute('SELECT Betta FROM Bethans WHERE SenVenanI = ?', (Se,))
    Betha = cursor.fetchone()
    cursor.execute('SELECT Betta FROM Bethans WHERE SenVenanI = ?', (SeK,))
    BethaK = cursor.fetchone()
    conn.close()
    result = [Betha, BethaK]
    return result

class Preassure():
    def HeRe(self, Q, t0, density, viscosity, Dc, Dout, d, d_past):

        He = t0 * density * math.pow(d, 2) / math.pow(viscosity, 2) # Число Хендсрема
        HeK = t0 * density * math.pow((Dc - Dout), 2) / math.pow(viscosity, 2) # Число Хендстрема для кольцевого пространства
        Hek_high = t0 * density * math.pow((d_past - Dout), 2) / math.pow(viscosity, 2) # Число Хендстрема для кольцевого в верхнем участке

        Recrit = 7.3 * math.pow(He, 0.58) + 2100 # Число Рейнольдса критическое для турбулетного режима
        ReKcrit = 7.3 * math.pow(HeK, 0.58) + 2100 #
        ReKcrit_high = 7.3 * math.pow(Hek_high, 0.58) + 2100 #  Число Рейнольдса критическое для турбулетного режима в верхнем участке обсадной колонны

        spd_tube = 4 * Q * 1000/ (math.pi * math.pow(d, 2)) # Скорость Нисходящего потока
        spd_out = 4 * Q * 1000 / (math.pi * (math.pow(Dc, 2) - math.pow(Dout, 2))) # Скорость восходящего потока
        spd_out_high = 4 * Q * 1000 / (math.pi * (math.pow(d_past, 2) - math.pow(Dout, 2))) # Скорость восходящего потока в верхнем участке

        ReTR_tube = density * spd_tube * d / viscosity
        ReKP_out = density * spd_out * (Dc - Dout) / viscosity
        ReKP_out_high = density * spd_out * (d_past - Dout) / viscosity

        lam = 0.3164 / math.pow(ReTR_tube, 0.25)
        lamK = 0.339 / math.pow(ReKP_out, 0.25)
        lamK_high = 0.339 / math.pow(ReKP_out_high, 0.25)

        result = [He, HeK, Hek_high, Recrit, ReKcrit, ReKcrit_high, spd_tube, spd_out, spd_out_high, ReTR_tube, ReKP_out, ReKP_out_high, lam, lamK, lamK_high]
        return


    def static_preassure(self, ): #эксперементальная функция. Пока не работает
        pass


       #preassure_tube =(density_cem_light*L0 + density_cem_heavy * L1 + density_buff * L2 + density_push * L3 + density_flush * L4) * 9.81
       #preassure_ring = 1

      # if True == "Направление":
      #          P_614 = (density_clean * Sole - Sole - Lk - Hb + density_buff * Hb + density_cemm * (Sole - Sole - Lk - h_cement_out)) * 9.81 + Pcircut_low * (Sole - Hb - Sole - Lk - h_cement_out)
      #      else:
      #          P_614 = (density_clean * Sole - Sole - Lk - Hb + density_buff * Hb + density_cemm * (Sole - Sole - Lk - h_cement_out)) * 9.81 + Pcircut_low * (Sole - Hb - L_past- Sole - Lk - h_cement_out) + Pcircut_high * L_past








def critical_speed(Q, t0, density, density_push, density_buff, density_cemm, Dc, Dout, d,
                   viscosity, L, Lk, Hb, Betha, BethaK, d_past, Column_volume, Gradientlist, density_clean, L_past, column_type):
    """
    :param Q: Производительность ЦМ
    :param t0_push:
    :param t0_clean:
    :param t0: Динамическое напряжение сдвига
    :param density: ???
    :param density_clean: плотность промывочной жидкости
    :param density_push: плотность продавочной жидкости
    :param density_buff: плотность продавочной жидкости
    :param density_cemm: плотность цементного раствора
    :param Dc: диаметр скважины
    :param Dout: внешний диаметр обсадной колонны
    :param d: Внутренний диаметр обсадной колонны
    :param viscosity: Пластическая вязкость
    :param L: Глубина спуска
    :param Lk: Длина по оси
    :param Hb: Высота столба буферной жидкости в обсадной колонне
    :param L_past: длинна предыдущей обсадной колонны
    :return:
    """
    '''
    приставка K означает, что расчёт ведётся для кольцевого пространства, если нет то для внутритрубного пространства обсадной колонны 
    приставка crit означает, что скорость в том или ином участке является критической, а поток турбулентным 
    density неизвестная величина на время естов заменена на плотность цемента
    '''
    #Откоректировать значения для верхнего участка кольцевого пространства
    He = t0 * density * math.pow(d, 2) / math.pow(viscosity, 2) # Число Хендсрема
    Hek = t0 * density * math.pow((Dc - Dout), 2) / math.pow(viscosity, 2) # Число Хендстрема для кольцевого пространства
    Hek_high = t0 * density * math.pow((d_past - Dout), 2) / math.pow(viscosity, 2) # Число Хендстрема для кольцевого в верхнем участке
    Recrit = 7.3 * math.pow(He, 0.58) + 2100 # Число Рейнольдса критическое для турбулетного режима
    ReKcrit = 7.3 * math.pow(Hek, 0.58) + 2100 #
    ReKcrit_high = 7.3 * math.pow(Hek_high, 0.58) + 2100 #  Число Рейнольдса критическое для турбулетного режима в верхнем участке обсадной колонны


    #wcrit = viscosity * Recrit / (density * d) # Критическая скорость в обсадной колонне
    #wKcrit = viscosity * ReKcrit / (density * (Dc - Dout)) # Критическая скорость в затрубном пространстве
    #wKcrit_high = viscosity * ReKcrit_high / (density * (Dc - Dout)) # Критическая скорость в затрубном пространстве в верхнем участке



    spd_tube = 4 * Q * 1000/ (math.pi * math.pow(d, 2)) # Скорость Нисходящего потока
    spd_out = 4 * Q * 1000 / (math.pi * (math.pow(Dc, 2) - math.pow(Dout, 2))) # Скорость восходящего потока
    spd_out_high = 4 * Q * 1000 / (math.pi * (math.pow(d_past, 2) - math.pow(Dout, 2))) # Скорость восходящего потока в верхнем участке
    ReTR_tube = density * spd_tube * d / viscosity
    ReKP_out = density * spd_out * (Dc - Dout) / viscosity

    if column_type != "Направление":
        ReKP_out_high = density * spd_out * (d_past - Dout) / viscosity
        lamK_high = 0.339 / math.pow(ReKP_out_high, 0.25)
    else:
        ReKP_out_high = 0
        lamK_high = 0
 # Re = spd_tube * d * density / viscosity # Число Рейнольдса для ламинарного(структурного) режима
 # ReK = spd_out * (Dc - Dout) * density / viscosity # В кольцелом пространстве
    lam = 0.3164 / math.pow(ReTR_tube, 0.25)
    lamK = 0.339 / math.pow(ReKP_out, 0.25)


    if ReTR_tube > Recrit:
        Ptube = lam * density_push * L * math.pow(spd_tube, 2) / (2 * d)
    else:
        Ptube = 4 * t0 * L / (Betha * d) # 

    if column_type == "Направление":
        Pcircut_high = 0.0
        if ReKP_out > ReKcrit:
            Pcircut_low = 0.5 * lamK * density_push * math.pow(spd_out, 2) / (Dc - Dout) # Наибольшее давление в цементировочной головке в момент начала закачки
        else:
            Pcircut_low = 4 * t0 / (BethaK * (Dc - Dout))
    else:
        if ReKP_out_high > ReKcrit_high:
            Pcircut_high = 0.5 * lamK_high * density_push * math.pow(spd_out_high, 2) / (d_past - Dout) # нужно сделать расчёт скорости для верхнего участка
        else:
            Pcircut_high = 4 * t0  / (BethaK * (d_past - Dout))
        if ReKP_out > ReKcrit:

            Pcircut_low = 0.5 * lamK * density_push * math.pow(spd_out, 2) / (Dc - Dout) # Наибольшее давление в цементировочной головке в момент начала закачки
        else:
            Pcircut_low = 4 * t0 / (BethaK * (Dc - Dout))
    P_zak = (density_push - density_buff) * 9.81 * Hb + Ptube + (Pcircut_low * Lk) + (Pcircut_high * Lk)

    P_anti = (density_cemm * Lk - density_buff * Hb - density_push * (Lk - Hb)) * 9.8 - Ptube - (Pcircut_low * Lk)  - (Pcircut_high * Lk)

    h_cement_out = (Column_volume - (0.785 * math.pow(d_past, 2) *Lk))  / ( 0.785 * (Lk/L) * (math.pow(Dc, 2) - math.pow(Dout, 2)))

    for record in Gradientlist:

        Gradient = record  #.item(record, "values")
        Roof = float(Gradient[1])
        Sole = float(Gradient[2])
        Preassure = float(Gradient[3])
        if Lk-Sole >= h_cement_out:  #  если лк меньше значит тампонажный раствор учитывается
            if Lk-Sole >= h_cement_out + Hb:
                if column_type == "Направление":
                    P_614 = density_clean * Sole * 9.81 + Pcircut_low * Sole
                else:
                    P_614 = density_clean * Sole * 9.81 + (Pcircut_low * (Sole - L_past)) + Pcircut_high * L_past
            else:
                if column_type == "Направление":
                    P_614 = (density_clean * Sole - Sole - Lk - Hb + density_buff * (Sole - Lk - Hb)) * 9.81 + Pcircut_low * (Sole - Sole - Lk - Hb)
                else:
                    P_614 = (density_clean * (Sole - Sole - Lk - Hb) + density_buff * (Sole - Lk - Hb)) * 9.81 + Pcircut_low * (Sole - Sole - Lk - Hb - L_past) + Pcircut_high * L_past
        else:
            if column_type == "Направление":
                P_614 = (density_clean * Sole - Sole - Lk - Hb + density_buff * Hb + density_cemm * (Sole - Sole - Lk - h_cement_out)) * 9.81 + Pcircut_low * (Sole - Hb - Sole - Lk - h_cement_out)
            else:
                P_614 = (density_clean * Sole - (Sole - Lk - Hb + density_buff * Hb + density_cemm * (Sole - (Sole - Lk - h_cement_out)))) * 9.81 + Pcircut_low * (Sole - Hb - L_past- (Sole - Lk - h_cement_out)) + Pcircut_high * L_past
        сcit_preassure = round((Preassure * math.pow(10, -3) * Sole), 3)
        if P_614 <= сcit_preassure:
            print('цементировать можно')
        else:
            print('разорвёт пласт')








    #P_crit =   + P_anti + Pcircut_high + Pcircut_low  давление на слабые пласты

    answer = [spd_out, spd_tube, ReKcrit, Recrit, Hek, He, P_614, сcit_preassure]
    answer1 = [P_zak, P_anti]
    return answer


#P_plast = height * density * 9.81 + () / (2 * (Dc - Dout))







def mixing_cem(Mass_cement, mc, Ucm, water_injection, n, cemdensity, waterdensity):
    '''
    :param Mass_cement: Масса тамнонажного цемента
    :param mc: Насыпная плонтность цементна
    :param Ucm: Вместимость бункера
    :param water_injection: Подача воды
    :param n: водоцементное отношение
    :param cemdensity:
    :param waterdensity: плотность воды для затворения цементного раствора с учётом химрегентов
    :return:
    '''
    ic = Mass_cement * waterdensity / (mc * Ucm)
    qcm = waterdensity * water_injection * 0.001 / (n * mc)
    qc = (1 + n) * mc * qcm * 0.001 / cemdensity
    answer = [ic, qcm, qc]
    return answer


def time():
    pass

























