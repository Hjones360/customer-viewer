import csv

class Customer:
    def __init__(self, cust_id, first_name, last_name, company_name, address, city, state, zip_code):
        self.id = cust_id
        self.firstName = first_name
        self.lastName = last_name
        self.company = company_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip_code

    def getFullName(self):
        fullName = self.firstName + " " + self.lastName
        return fullName

    def getFullAddress(self):
        a = ""
        if self.company != "":
            a += self.company + "\n"
        a += self.address + "\n"
        a += self.city + ", " + self.state + " " + self.zip
        return a

def read_customers_from_csv(file_path):
    customers = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            cust_id, first_name, last_name, company_name, address, city, state, zip_code = row
            customer = Customer(cust_id, first_name, last_name, company_name, address, city, state, zip_code)
            customers.append(customer)
    return customers

def find_customer_by_id(customers, cust_id):
    for customer in customers:
        if customer.id == cust_id:
            return customer
    return None

def main():
    print("Customer viewer")
    print()
    customers = read_customers_from_csv('customers.csv')
    
    while True:
        cust_id = input("Enter customer ID: ")
        customer = find_customer_by_id(customers, cust_id)
        print()
        
        if customer:
            print(customer.getFullName())
            print(customer.getFullAddress())
            print()
        else:
            print("No customer with that ID.")
        
        continue_prompt = input("Continue? (y/n): ")
        print()
        if continue_prompt.lower() != 'y':
            break
    print()
    print("Bye!")

if __name__ == "__main__":
    main()