from typing import List
from Worker import Worker
from Invoice import Invoice
from Engineer import Engineer
from Architect import Architect
from Obrero import Obrero

class Company:
  def __init__(self):
    self.workers: List[Worker] = []
    self.invoices: List[Invoice] = []

  def search_worker(self, dni: str):
    worker = None
    for w in self.workers:
      if w.dni == dni:
        worker = w
        break
    return worker

  def create_worker(self, dni: str):
    first_name = input('Por favor ingrese su nombre: ')
    last_name = input('Por favor ingrese su apellido: ')
    profession = input('Por favor ingerese su profesión (e/a/w): ').lower()
    specialty = input('Por favor ingrese su especialidad: ')

    worker = None
    if profession == 'e':
      worker = Engineer(first_name, last_name, dni, specialty)
    elif profession == 'a':
      worker = Architect(first_name, last_name, dni, specialty)
    elif profession == 'w':
      worker = Obrero(first_name, last_name, dni, specialty)
    else:
      print('Error la profesión no existe ... ')

    self.workers.append(worker)
    return worker


  def create_invoice(self, worker: Worker):
    month = int(input('Por favor ingrese el mes: '))
    year = int(input('Por favor ingrese el año: '))
    hours = float(input('Por favor ingrese las horas: '))
    invoice = Invoice(worker, hours, month, year)
    self.invoices.append(invoice)
    return invoice

  def total_payed(self):
    total = 0
    for invoice in self.invoices:
      total += invoice.total
    return total

  def get_employees_by_type(self):
    engineers = 0
    architects = 0
    workers = 0
    for worker in self.workers:
      if isinstance(worker, Engineer):
        engineers += 1
      elif isinstance(worker, Architect):
        architects += 1
      elif isinstance(worker, Obrero):
        workers += 1
    return engineers, architects, workers

  def get_avg_per_type(self):
    engineers = 0
    architects = 0
    workers = 0
    pay_engineers = 0
    pay_architects = 0
    pay_workers = 0

    for invoice in self.invoices:
      if isinstance(invoice.worker, Engineer):
        pay_engineers += invoice.total
        engineers += 1
      elif isinstance(invoice.worker, Architect):
        pay_architects += invoice.total
        architects += 1
      elif isinstance(invoice.worker, Obrero):
        pay_workers += invoice.total
        workers += 1

    avg_engineers = 0
    avg_architects = 0
    avg_workers = 0

    if engineers > 0:
      avg_engineers = pay_engineers / engineers
    if architects > 0:
      avg_architects = pay_architects / architects
    if workers > 0:
      avg_workers = pay_workers / workers

    return avg_engineers, avg_architects, avg_workers


  def most_payment_per_type(self):
    engineer: Invoice = None
    architect: Invoice = None
    worker: Invoice = None

    for invoice in self.invoices:
      if isinstance(invoice.worker, Engineer):
        if engineer != None:
          if engineer.total < invoice.total:
            engineer = invoice
        else:
          engineer = invoice
      if isinstance(invoice.worker, Architect):
        if architect != None:
          if architect.total < invoice.total:
            architect = invoice
        else:
          architect = invoice
      if isinstance(invoice.worker, Obrero):
        if worker != None:
          if worker.total < invoice.total:
            worker = invoice
        else:
          worker = invoice

    return engineer, architect, worker

  def statics(self):
    total_pay = self.total_payed()
    print(f'El total pagado por la compañía es: {total_pay}')
    e, a, w = self.get_employees_by_type()
    print(f'''El total por tipo de empleado es:
          1. Ingeniero: {e}
          2. Arquitecto: {a}
          3. Obrero: {w}
          ''')
    avg_eng, avg_arc, avg_wor = self.get_avg_per_type()
    print(f'''El promedio por tipo de empleado es:
          1. Ingeniero: {avg_eng}
          2. Arquitecto: {avg_arc}
          3. Obrero: {avg_wor}
          ''')
    eng, arc, wor = self.most_payment_per_type()
    print(f'''El trabajador más pagado por tipo es:
          1. Ingeniero: {eng}
          2. Arquitecto: {arc}
          3. Obrero: {wor}
          ''')

  def menu(self):
    option = input(f'''1. Crear trabajador
                   2. Pagar trabajador
                   3. Ver estadisticas
                   ''')
    dni = input('Por favor ingrese la cédula: ')
    if option == '1':
      worker = self.search_worker(dni)
      if worker == None:
        self.create_worker(dni)
      else:
        print(f'El trabajador con cédula {dni} ya existe')
    elif option == '2':
      worker = self.search_worker(dni)
      if worker == None:
        worker = self.create_worker(dni)
      if worker == None:
        # crear la factura
        invoice = self.create_invoice(worker)
        print(invoice)
    elif option == '3':
      self.statics()



  def start(self):
    ans = 'y'
    while ans == 'y':
      self.menu()
      ans = input('Desea continuar? (y/n): ').lower()
