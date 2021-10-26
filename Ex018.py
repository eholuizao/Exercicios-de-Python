from math import sin, cos, tan, radians

ang = float(input("Digite um angulo: "))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tang = tan(radians(ang))

print(f"O angulo escolhido foi {ang}\n"
      f"Seu seno mede: {seno:.2f}\n"
      f"Seu cosseno mede: {cosseno:.2f}\n"
      f"Sua tangente mede: {tang:.2f}")
