times = ("internacional", "são paulo", "flamengo", "atlético-MG", "palmeiras", "grêmio", "fluminense", "corinthians",
         "santos", "ceará", "bragantino", "atlético-PR", "atlético-GO", "vasco", "fortaleza", "bahia", "sport recife",
         "coritiba", "goiás", "botafogo")

print(f"""
Primeiros cinco colocados: {times[:5]}
Últimos quatro colocados: {times[-4:]}
Times em ordem alfabética: {sorted(times)}
O MENGÃO está na {times.index("flamengo") + 1}° posição""")
