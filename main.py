class Package:

    def __init__(self, package_id, sender, receive, status="Pending"):

        # Initializes a package 

        self.package_id = package_id
        self.sender = sender
        self.receive = receive
        self.status = status

    # Display package detalis
    
    def display(self):

        print(f"ID: {self.package_id} | From: {self.sender} | To: {self.receive} | Status: {self.status}")

    # Update package status

    def update_status(self, new_status):

        self.status = new_status
    
class LogisticsApp:
    
    def __init__(self):

        # Initialize the logistics app

        self.packages = []
    
    # Adds a new package

    def add_package(self):

        pid = input("Enter Package ID: ")

        sender = input("Enter Sender Name: ")

        receiver = input("Enter Receiver Name: ")

        pkg = Package(pid, sender, receiver)

        self.packages.append(pkg)

        print("Package added.\n")
    
    # Views all packages

    def view_packages(self):

        if not self.packages:

            print("No packages.\n")

            return
        
        for pkg in self.packages:

            pkg.display()

        print()
        
    #Updateas package status

    def update_packages(self):

        pid = input("Enter Package ID to update: ")

        for pkg in self.packages:

            if pkg.package_id == pid:
                
                new_status = input("Enter new status: ")

                pkg.update_status(new_status)

                print("Status updated.\n")

                return
            
            print("Package not found.\n")
        
    # Runs the main menu

    def run(self):

        while True:

            print("Logistics App Menu")

            print("1. Add Package")

            print("2. View Packages")

            print("3. Update Packages Status")

            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":

                self.add_package()
            
            elif choice == "2":

                self.view_packages()
            
            elif choice == "3":

                self.update_packages()
            
            elif choice == "4":

                print("Exiting...")

                break
            
            else:

                print("Invalid choice.\n")

# Start The app 

if __name__ == "__main__":

    app = LogisticsApp()

    app.run()



