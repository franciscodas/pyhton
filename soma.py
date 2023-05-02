indice =13
soma =0
k =0
while k < indice:
    k=k+1
    soma = soma+k;
    print(soma)
    
    numero = int(input("informe um numero: "))
fibonacci = [0, 1]
while fibonacci[-1] < numero:
  proximo = fibonacci[-1]+fibonacci[-2]
  fibonacci.append(proximo)
  if numero in fibonacci:
    print(f"o numero {numero}fa parte da sequencia de fibonacci: {fibonacci}")
  else:
      print(f" o numero {numero} nao faz parte da sequencia de fibonacci: {fibonacci}")
      
      
      
      # sequencia a)
lista_a = [1, 3, 5, 7]

if lista_a[1] - lista_a[0] == lista_a[2] - lista_a[1]:
    proximo_elemento_a = lista_a[-1] + (lista_a[1] - lista_a[0])
    
print(f" A sequência é, {lista_a} e o próximo elemento é, {proximo_elemento_a}")


# sequência b)
lista_b = [2, 4, 8, 16, 32, 64]

if lista_b[1] / lista_b[0] == lista_b[2] / lista_b[1]:
    proximo_elemento_b = lista_b[-1] * (lista_b[1] / lista_b[0])
    
print(f" A sequência é, {lista_b}, e o próximo elemento é' {proximo_elemento_b}")


# sequência c)
lista_c = [0, 1, 4, 9, 16, 25, 36]

if lista_c[1] - lista_c[0] == lista_c[2] - lista_c[1]:
  proximo_elemento_c = lista_c[-1] + (lista_c[1] - lista_c[0])
elif lista_c[1] + lista_c[0] == lista_c[2]:
  proximo_elemento_c = (len(lista_c) ** 2)
  print(f"A sequência é, {lista_c}, e o próximo elemento é, {proximo_elemento_c}")


# sequência d)
lista_d = [4, 16, 36, 64]

if lista_d[1] - lista_d[0] == lista_d[2] - lista_d[1]:
    proximo_elemento_d = lista_d[-1] + (lista_d[1] - lista_d[0])
else:
    proximo_elemento_d = ((len(lista_d) * 6) ** 2)
    
print(f"A sequência é, {lista_d}, e o próximo elemento é, {proximo_elemento_d}")


# sequência e)
lista_e = [1, 1, 2, 3, 5, 8]

if lista_e[-1] - lista_e[-2] == lista_e[-2] - lista_e[-3]:
    proximo_elemento_e = lista_e[-1] + lista_e[-2]
    print(f" A sequência é, {lista_e}, e o próximo elemento é, {proximo_elemento_e}")


# sequência f)
lista_f = [2, 10, 12, 16, 17, 18, 19]

if lista_f[1] - lista_f[0] == lista_f[2] - lista_f[1]:
    proximo_elemento_f = lista_f[-1] + (lista_f[1] - lista_f[0])
else:
    temp = []
    for i in range(len(lista_f)-1):
        temp.append(lista_f[i+1] - lista_f[i])
    next_element = lista_f[-1] + min(temp)
    proximo_elemento_f = next_element
    
print(f" A sequência é, {lista_f}, e o próximo elemento é, {proximo_elemento_f}")