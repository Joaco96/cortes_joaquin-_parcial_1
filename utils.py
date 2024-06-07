def for_each(procesadora, lista: list) -> None:
  if not isinstance(lista,list):
    raise TypeError("No es una lista")
  for i in range(len(lista)):
    lista[i] = procesadora(lista[i])

def map(procesadora, lista: list) -> list:
  if not isinstance(lista,list):
    raise TypeError("No es una lista")
  lista_retorno = []
  for element in lista:
    lista_retorno.append(procesadora(element))
  return lista_retorno

def sort(comparador, lista:list) -> None:
  if not isinstance(lista,list):
    raise TypeError("No es una lista")
  tam = len(lista)
  for i in range(tam - 1):
    for j in range(i + 1, tam):
      if (comparador(lista[i], lista[j])):
        aux = lista[i]
        lista[i] = lista[j]
        lista[j] = aux

def sorted_map(comparador, lista:list) -> list:
  if not isinstance(lista,list):
    raise TypeError("No es una lista")
  copia_lista = map(lambda numero: numero, lista)
  sort(comparador, copia_lista)
  return copia_lista

def filter(filtradora, lista: list) -> list:
  if not isinstance(lista,list):
    raise TypeError("No es una lista")
  lista_retorno = []
  for element in lista:
    if(filtradora(element)):
      lista_retorno.append(element)
  return lista_retorno

def custom_reduce(func, iterable: list, initial = None):
    if not isinstance(iterable,list):
      raise TypeError("No es una lista")
    value = initial if initial != None else iterable[0]
    start_index = 0 if initial != None else 1
    for i in range(start_index, len(iterable)):
      value = func(value, iterable[i])
    return value