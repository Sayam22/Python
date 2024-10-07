import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Manager")
        
        self.contacts = {}

        self.label = tk.Label(master, text="Contact Manager", font=("Arial", 18))
        self.label.pack(pady=10)

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(master, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(pady=5)

        self.search_button = tk.Button(master, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=5)

        self.update_button = tk.Button(master, text="Update Contact", command=self.update_contact)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        if name:
            phone = simpledialog.askstring("Input", "Enter phone number:")
            email = simpledialog.askstring("Input", "Enter email:")
            address = simpledialog.askstring("Input", "Enter address:")
            if name in self.contacts:
                messagebox.showwarning("Warning", "Contact already exists!")
            else:
                self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
                messagebox.showinfo("Success", f"Contact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts available.")
            return
        
        contact_list = "\n".join([f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}\n" 
                                   for name, details in self.contacts.items()])
        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        search_term = simpledialog.askstring("Input", "Enter name or phone number to search:")
        if not search_term:
            return
        
        results = [f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}\n" 
                   for name, details in self.contacts.items() if search_term in name or search_term in details['phone']]
        
        if results:
            messagebox.showinfo("Search Results", "\n".join(results))
        else:
            messagebox.showinfo("Search Results", "No matching contacts found.")

    def update_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to update:")
        if name in self.contacts:
            phone = simpledialog.askstring("Input", "Enter new phone number:", initialvalue=self.contacts[name]['phone'])
            email = simpledialog.askstring("Input", "Enter new email:", initialvalue=self.contacts[name]['email'])
            address = simpledialog.askstring("Input", "Enter new address:", initialvalue=self.contacts[name]['address'])
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            messagebox.showinfo("Success", f"Contact '{name}' updated successfully!")
        else:
            messagebox.showwarning("Warning", "Contact not found!")

    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to delete:")
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", f"Contact '{name}' deleted successfully!")
        else:
            messagebox.showwarning("Warning", "Contact not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
