from typing import List

from utils import admin_access, user_access


def main():
  clients: List[dict] = [
    {
      'first_name': 'Jose',
      'last_name': 'Quevedo',
      'address': 'Los naranjos',
      'phone': '04121111111',
      'dni': '27014788',
      'accounts': [
        {'number': 1, 'type': 'corriente', 'balance': 100.0, 'opening_date': '25/09/24'},
        {'number': 2, 'type': 'ahorro', 'balance': 1000000.0, 'opening_date': '25/09/24'},
        {'number': 3, 'type': 'corriente', 'balance': 500.0, 'opening_date': '25/09/24'}
      ]
    },
    {
      'first_name': 'Ivanna',
      'last_name': 'Padron',
      'address': 'Los naranjos',
      'phone': '04141111111',
      'dni': '23828274',
      'accounts': [
        {'number': 1, 'type': 'corriente', 'balance': 1000.0, 'opening_date': '23/09/24'}
      ]
    },
    {
      'first_name': 'Luis',
      'last_name': 'Bello',
      'address': 'El marquez',
      'phone': '04241111111',
      'dni': '23871097',
      'accounts': [
        {'number': 1, 'type': 'ahorro', 'balance': 10000.0, 'opening_date': '25/09/22'},
        {'number': 2, 'type': 'corriente', 'balance': 150.0, 'opening_date': '25/09/23'}
      ]
    }
  ]

  menu = """
  0. CONSULTAR BALANCE
  1. DEPOSITAR
  2. RETIRAR
  3. SOLICITAR PRESTAMO -> NOTA: Solo se podra prestar el 30% del saldo disponible
  4. CREAR CUENTA
"""

  menu_admin = """
    5. [ADMINISTRADOR]: Balances disponibles
  """

  SECRET_CODE = '-999'

  ans = 'y'

  while ans == 'y':
    access_code = input('Ingrese su codigo de acceso: ')
    if access_code == SECRET_CODE:
      admin_access(menu_admin, clients)
    else:
      user_access(menu, clients)
    ans = input('Desea continuar? (y/n): ').lower()

main()
