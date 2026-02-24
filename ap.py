import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class POS:
    def __init__(self, root):
        self.root = root
        self.root.title("Supermarket POS System")
        self.root.geometry("900x600")

        # --- Sample Product Database ---
        self.products = {
            "1001": {"name": "Milk 1L", "price": 1.50},
            "1002": {"name": "Bread", "price": 1.00},
            "1003": {"name": "Sugar 1Kg", "price": 2.20},
            "1004": {"name": "Rice 1Kg", "price": 1.80},
            "1005": {"name": "Soap", "price": 0.80},
        }

        self.cart = []

        self.create_widgets()

    def create_widgets(self):
        # -------- Top Frame --------
        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=10)

        tk.Label(top_frame, text="Barcode / Product Code:").grid(row=0, column=0, padx=5)
        self.code_entry = tk.Entry(top_frame, width=20)
        self.code_entry.grid(row=0, column=1, padx=5)

        tk.Label(top_frame, text="Quantity:").grid(row=0, column=2, padx=5)
        self.qty_entry = tk.Entry(top_frame, width=5)
        self.qty_entry.insert(0, "1")
        self.qty_entry.grid(row=0, column=3, padx=5)

        tk.Button(top_frame, text="Add to Cart", command=self.add_to_cart, bg="green", fg="white").grid(row=0, column=4, padx=10)

        # -------- Cart Table --------
        columns = ("Code", "Name", "Price", "Qty", "Total")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings", height=15)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.CENTER)

        self.tree.pack(pady=20)

        # -------- Bottom Frame --------
        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack()

        tk.Button(bottom_frame, text="Remove Selected", command=self.remove_item, bg="red", fg="white").grid(row=0, column=0, padx=10)

        tk.Button(bottom_frame, text="Clear Cart", command=self.clear_cart).grid(row=0, column=1, padx=10)

        tk.Button(bottom_frame, text="Generate Receipt", command=self.generate_receipt, bg="blue", fg="white").grid(row=0, column=2, padx=10)

        self.total_label = tk.Label(self.root, text="Total: $0.00", font=("Arial", 16))
        self.total_label.pack(pady=10)

    # -------- Add Item --------
    def add_to_cart(self):
        code = self.code_entry.get()
        qty = self.qty_entry.get()

        if code not in self.products:
            messagebox.showerror("Error", "Product not found")
            return

        try:
            qty = int(qty)
        except:
            messagebox.showerror("Error", "Invalid quantity")
            return

        product = self.products[code]
        total_price = product["price"] * qty

        self.cart.append({
            "code": code,
            "name": product["name"],
            "price": product["price"],
            "qty": qty,
            "total": total_price
        })

        self.tree.insert("", tk.END, values=(code, product["name"], product["price"], qty, total_price))

        self.update_total()

        self.code_entry.delete(0, tk.END)
        self.qty_entry.delete(0, tk.END)
        self.qty_entry.insert(0, "1")

    # -------- Remove Item --------
    def remove_item(self):
        selected = self.tree.selection()
        if not selected:
            return

        for item in selected:
            index = self.tree.index(item)
            self.tree.delete(item)
            del self.cart[index]

        self.update_total()

    # -------- Clear Cart --------
    def clear_cart(self):
        self.tree.delete(*self.tree.get_children())
        self.cart = []
        self.update_total()

    # -------- Update Total --------
    def update_total(self):
        total = sum(item["total"] for item in self.cart)
        self.total_label.config(text=f"Total: ${total:.2f}")

    # -------- Receipt --------
    def generate_receipt(self):
        if not self.cart:
            messagebox.showinfo("Info", "Cart is empty")
            return

        receipt_window = tk.Toplevel(self.root)
        receipt_window.title("Receipt")

        text = tk.Text(receipt_window, width=50, height=25)
        text.pack()

        text.insert(tk.END, "===== SUPERMARKET RECEIPT =====\n")
        text.insert(tk.END, f"Date: {datetime.now()}\n")
        text.insert(tk.END, "-" * 35 + "\n")

        for item in self.cart:
            text.insert(tk.END, f"{item['name']} x{item['qty']} - ${item['total']:.2f}\n")

        text.insert(tk.END, "-" * 35 + "\n")
        total = sum(item["total"] for item in self.cart)
        text.insert(tk.END, f"TOTAL: ${total:.2f}\n")
        text.insert(tk.END, "===============================")

        text.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = POS(root)
    root.mainloop()