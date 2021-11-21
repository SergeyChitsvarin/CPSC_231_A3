import sys

constellation_list = [['CAS EPSILON', 'CAS DELTA'],
                       ['CAS DELTA', 'CAS GAMMA'],
                       ['CAS GAMMA', 'SCHEDAR'],
                       ['SCHEDAR', 'CAPH'],
                       ['CAS GAMMA', 'CAS KAPPA'],
                       ['CAS KAPPA', 'CAS IOTA'],
                       ['SCHEDAR', 'CAS ZETA'],
                       ['CAS ZETA', 'CAS THETA']]
used_stars = {}
for sub_list in constellation_list:
    for name in sub_list:
        used_stars[name] = True

print(list(used_stars.keys()))
