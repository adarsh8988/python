# import re
# txt="""In today's digital age, communication has evolved significantly. Gone are the days when sending a letter via postal mail was the primary means of conveying information. Instead, we now rely heavily on electronic communication. Here are some example email addresses that illustrate the diversity of email domains and formats:

# John.Doe@example.com is a classic email address format with a straightforward name and a generic domain.
# In contrast, alice_smith1234@gmail.com reflects the popular use of email services like Gmail, known for its user-friendly interface and large storage capacity.

# info@company.co.uk demonstrates a business-oriented email with a UK domain, emphasizing the global reach of email communication.
# In today's interconnected world, support@my-website.io is essential for any online business, ensuring customers can easily seek assistance.

# contact_me@subdomain.example.net exemplifies the use of subdomains, a common practice for organizing different sections of a website.

# webmaster@another-site.org is a classic technical email address often responsible for maintaining website functionality.

# marketing@company-name.biz highlights the role of email in marketing strategies and its potential impact on businesses.

# sales@domain_name.museum is a unique address showcasing how even museums use email for ticket sales and event promotions.

# help@myapp.travel caters to travelers seeking assistance with travel apps, underlining the versatility of email for various industries.

# contact@local-organization.jobs reflects the importance of email in the job application and hiring process.

# The convenience and speed of email have transformed the way we interact personally and professionally. Whether you're sending a quick message to a friend or conducting business negotiations, email addresses

# """
# p="[a-zA-Z]+[_]*[.]*[_]*[a-zA-Z]*[0-9]*[@][a-z]+[-]*[_]*[a-z]*[.][a-z]+[.]?[a-z]+"
# r=re.findall(p,txt)
# print(r)

    
import tkinter as tk

def on_click(button_text):
    current_text = entry.get()
    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the input and result
entry = tk.Entry(root, width=20, font=("Helvetica", 16))
entry.grid(row=0, column=0, columnspan=4)

# Buttons for the calculator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Create and place the buttons in the grid
row_val = 1
col_val = 0
for button_text in buttons:
    tk.Button(root, text=button_text, width=5, height=2, command=lambda bt=button_text: on_click(bt)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the Tkinter main loop
root.mainloop()





