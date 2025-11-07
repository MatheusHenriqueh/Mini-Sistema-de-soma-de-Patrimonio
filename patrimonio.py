#Mini sistema de soma de patrimÔnio
#Autor: Matheus Ruivo
#Data: 07/11/25

print("Calculamento de Patrimônio")
dinheiro_ativo = int(input("Quanto você tem de dinheiro ativo(investimento, casas e etc)?"))
dinheiro_passivo = int(input("Quanto de dinheiro passivo? (dívidas, parcelas, empréstimos)?"))

somando_patrimonio = dinheiro_ativo - dinheiro_passivo

if somando_patrimonio >=0:
   print(f"Seu patrimônio líquido é de {somando_patrimonio:.2f}")
elif somando_patrimonio <=0:
   print(F"Seu saldo é negativo, suas dívidas é maior que seus ganhos! {somando_patrimonio:.2f}")
else:
   print("Algo errado!")