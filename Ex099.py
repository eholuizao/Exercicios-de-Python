def valores(* num):
    print("=-" * 30)
    if len(num) > 0:
        for v in num:
            print(v, end=" ")
        print(f"Foram passados {len(num)} valores ao todo.")
        print(f"O maior valor informado foi {max(num)}.")
    else:
        print("Foram passados 0 valores ao todo.")
        print(f"O maior valor informado foi 0.")


valores(2, 9, 4, 5, 7, 1)
valores(4, 7, 0)
valores(1, 2)
valores(6)
valores()
