def kinetic_energy(m:'in KG', v:'in M/S')->'Joules':
    return 1/2*m*v**2

x = kinetic_energy.__annotations__

for key,value in x.items():
    print(f"{key}:{value}".format())