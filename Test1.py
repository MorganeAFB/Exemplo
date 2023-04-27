import customtkinter
import math

def calcular():
  ValorN = int(entry1.get())
  ValorX = int(entry2.get())
  ValorP = float(entry3.get())

  P = ValorP / 100
  Q = 1 - P

  CalculoCombinacoesPossiveis = math.factorial(ValorN) / ((math.factorial(ValorN - ValorX)) * math.factorial(ValorX))

  CalculoProbabilidadeIndividual = CalculoCombinacoesPossiveis * P ** ValorX * Q ** (ValorN - ValorX)

  Temp = ValorX

  CalculoProbabilidadeAcumulativa = 0

  while Temp >= 0:
      CalculoCombinacoesPossiveis = math.factorial(ValorN) / ((math.factorial(ValorN - Temp)) * math.factorial(Temp))

      CalculoProbabilidadeTemp = CalculoCombinacoesPossiveis * P ** Temp * Q ** (ValorN - Temp)

      Temp -= 1
      CalculoProbabilidadeAcumulativa += CalculoProbabilidadeTemp

  result.configure(state="normal")
  result.delete("1.0", "end")
  result.insert("end", f"P(x): {CalculoProbabilidadeIndividual:.4f} ou {CalculoProbabilidadeIndividual*100:.2f}%\n\nP(≤x): {CalculoProbabilidadeAcumulativa:.2f} ou {CalculoProbabilidadeAcumulativa*100:.2f}%")
  result.configure(state="disabled")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.geometry("400x500")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=5, padx=10, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Calculadora de Distribuição Biomial", font=("Roboto", 20))
label.pack(pady=12, padx=10)

#2
frame2 = customtkinter.CTkFrame(master=frame)
frame2.pack(pady=4, padx=65, fill="x", expand=True)

label = customtkinter.CTkLabel(master=frame2, text="Número de Elementos", font=("Roboto", 18))
label.pack(pady=4, padx=10)

entry1 = customtkinter.CTkEntry(master=frame2, placeholder_text="Variável N")
entry1.pack(pady=4, padx=10, fill="y")

#3
frame2 = customtkinter.CTkFrame(master=frame)
frame2.pack(pady=4, padx=65, fill="x", expand=True)

label = customtkinter.CTkLabel(master=frame2, text="Número de Possibilidades", font=("Roboto", 18))
label.pack(pady=4, padx=10)

entry2 = customtkinter.CTkEntry(master=frame2, placeholder_text="Variável X")
entry2.pack(pady=4, padx=10, fill="y")

#4
frame3 = customtkinter.CTkFrame(master=frame)
frame3.pack(pady=4, padx=65, fill="x", expand=True)

label = customtkinter.CTkLabel(master=frame3, text="Porcentagem de sucessos", font=("Roboto", 18))
label.pack(pady=4, padx=10)

entry3 = customtkinter.CTkEntry(master=frame3, placeholder_text="100, 20, 30, 22.34 ...")
entry3.pack(pady=4, padx=10, fill="y")

button = customtkinter.CTkButton(master=frame, text="Calcular", command=lambda: calcular())

button.pack(pady=12, padx=16)

result = customtkinter.CTkTextbox(root, font=customtkinter.CTkFont(size=15))
result.pack(pady=5,fill="both", padx=10)
result.configure(state="disabled")

root.mainloop()