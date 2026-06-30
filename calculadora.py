class Calculadora:

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b


if __name__ == "__main__":
    calc = Calculadora()

    while True:
        print("\n===== CALCULADORA =====")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "5":
            print("Hasta luego.")
            break

        try:
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))

            if opcion == "1":
                print("Resultado:", calc.sumar(a, b))
            elif opcion == "2":
                print("Resultado:", calc.restar(a, b))
            elif opcion == "3":
                print("Resultado:", calc.multiplicar(a, b))
            elif opcion == "4":
                print("Resultado:", calc.dividir(a, b))
            else:
                print("Opción inválida.")

        except Exception as e:
            print("Error:", e)