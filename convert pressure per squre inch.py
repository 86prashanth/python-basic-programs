kpa=float(input('input pressure in in kilopascals '))
psi=kpa/6.89475729

mmhg=kpa*760/101.325
atm=kpa/101.325
print("The pressure in piunds per square inch %.2f psi"%(psi))
print("The pressure in millimeter of mercury %.2f mmhg"%(mmhg))
print("The atmosphere pressure  %.2f atm:"%(atm))