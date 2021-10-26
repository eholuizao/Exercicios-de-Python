metro = float(input('Digite uma distância em metros: '))
km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000

print(f"""
\033[30m{metro}m é igual a:
\033[31m{km}km
\033[36m{hm}hm
\033[34m{dam}dam
\033[32m{dm}dm
\033[31m{cm}cm
\033[35m{mm}mm
""")
