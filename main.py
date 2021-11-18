import sys

stars_location_file = [['0.512379', '0.020508', '2.28', 'CAPH;CAS BETA'],
                       ['0.450342', '0.065296', '4.17', 'CAS KAPPA'],
                       ['0.581589', '0.094643', '3.69', 'CAS ZETA']]
for i in stars_location_file:
    x = float(i[0])
    y = float(i[1])
    mag = float(i[2])
    name_of_star = i[3]
    print(x, y, mag, name_of_star)
