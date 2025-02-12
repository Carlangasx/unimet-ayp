# Ejercicios clase 9: Funciones

## Ejercicio 1

Elabore una función que dado un número determine si es un número primo o no

**Output:**

```python
print(is_prime(2)) # True
print(is_prime(6)) # False
```

## Ejercicio 2

Realice un función que dado una lista de números `nums`, para cada número _i_ (`nums[i]`) determine cuantos números dentro de la lista son menores que el, es decir, para cada `nums[i]` debe contar los números `nums[j]` tal que `nums[j] < nums[i]` y `j!=i`. Debe regresar su respuesta como otra lista.

**Input:**

```python
nums = [8,1,2,2,3]
```

**Output:**

```python
print(count_smaller(nums)) # [4,0,1,1,3]
```

## Ejercicio 3

Realice una función que haga un registro de los datos de los pacientes de un consultorio médico y los guarde dentro de una lista que la función deberá devolver. Los datos que deberá solicitar son:

1. Número de cédula
2. Nombre
3. Apellido
4. Teléfono
5. Razón de consulta

## Ejercicio 4

Escriba una función llamada leer_tiempo.

La función debe tomar **un** argumento, un número entero y **devolver** un **string** que indique cuántas semanas y días son.

Por ejemplo, llamando a la función e imprimiendo el resultado de esta manera:

```python
print(leer_tiempo(10))
```

`Debe dar como **Output:**`

```python
'1 semana(s) y 3 dias(s).'
```

## Ejercicio 5

Realice una función que dado un entero `x` devuelva `True` si ese número es palindrome o `False` en otro caso.

Un entero es palindrome cuando se lee igual de derecha a izquierda y al revés

**Input:**

```python
x = 121
```

**Output:**

```python
True
```

_Explicación:_: 121 se lee como `121` de izquierda a derecha y de derecha a izquierda.

## Ejercicio 6

Dado un entero `x` realiza una función que reverse sus dígitos.

**Input:**

```python
x = 123
```

**Output:**

```python
x = 321
```
