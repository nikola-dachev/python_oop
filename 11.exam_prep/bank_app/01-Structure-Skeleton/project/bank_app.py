
from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
  VALID_LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
  VALID_CLIENTS_TYPES = {"Student": Student, "Adult": Adult}
  
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.loans = []
    self.clients = []
    self.granted_loans = 0
    self.granted_sum =0

  def add_loan(self, loan_type: str):
    if loan_type not in self.VALID_LOAN_TYPES:
      raise Exception("Invalid loan type!")

    new_loan = self.VALID_LOAN_TYPES[loan_type]()
    self.loans.append(new_loan)
    return f"{loan_type} was successfully added."

  def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
    if client_type not in self.VALID_CLIENTS_TYPES:
      raise Exception("Invalid client type!")

    if len(self.clients) >= self.capacity:
      return "Not enough bank capacity."

    new_client = self.VALID_CLIENTS_TYPES[client_type](client_name, client_id, income)
    self.clients.append(new_client)
    return f"{client_type} was successfully added."

  def grant_loan(self, loan_type: str, client_id: str):
    current_client = [client for client in self.clients if client.client_id == client_id][0]
    current_loan = [loan for loan in self.loans if loan.TYPE_ == loan_type][0]
      
      
    if not ((current_client.TYPE_ == "Student" and current_loan.TYPE_ == "StudentLoan") or (current_client.TYPE_ == "Adult" and current_loan.TYPE_ == "MortgageLoan")):
      return "Inappropriate loan type!"

    self.loans.remove(current_loan)
    current_client.loans.append(current_loan)
    self.granted_loans += 1
    self.granted_sum +=current_loan.amount
    return f"Successfully granted {loan_type} to {current_client.name} with ID {client_id}."


  def remove_client(self,client_id: str):
    try:
      client = next(filter(lambda x:x.client_id == client_id, self.clients))
      if len(client.loans) > 0:
        raise Exception("The client has loans! Removal is impossible!")
      self.clients.remove(client)
      return f"Successfully removed {client.name} with ID {client_id}."

    except StopIteration:
      raise Exception("No such client!")

  def increase_loan_interest(self, loan_type: str):
    increased_loans = [loan.increase_interest_rate() for loan in self.loans if loan.TYPE_ == loan_type]
    return f"Successfully changed {len(increased_loans)} loans."

  def increase_clients_interest(self, min_rate: float):
    increased_clients_interests = [client.increase_clients_interest() for client in self.clients if client.interest < min_rate]
    return f"Number of clients affected: {len(increased_clients_interests)}."

  def get_statistics(self):
    total_clients_income = sum([client.income for client in self.clients])
    not_granted_sum = sum([loan.amount for loan in self.loans])
    avg_client_interest_rate = sum([client.interest for client in self.clients])/len(self.clients) if self.clients else 0
    return f"Active Clients: {len(self.clients)}\n" +\
           f"Total Income: {total_clients_income:.2f}\n" +\
           f"Granted Loans: {self.granted_loans}, Total Sum: {self.granted_sum:.2f}\n" +\
           f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}\n" +\
           f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
