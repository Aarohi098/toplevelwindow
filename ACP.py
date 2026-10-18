from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Reading Schedule Planner")
root.geometry("400x200")

def open_planner():
    planner_window = Toplevel(root)
    planner_window.title("Plan Your Reading")
    planner_window.geometry("350x250")
    
    def calculate_schedule():
        try:
            total_pages = int(entry_total.get())
            pages_per_day = int(entry_daily.get())
            
    
            if total_pages < 0 or pages_per_day <= 0:
                raise ValueError("Numbers must be positive, and daily pages cannot be zero.")
          
            complete_days = total_pages // pages_per_day
          
            remaining_pages = total_pages % pages_per_day
        
            label_result.config(
                text=f"Complete Reading Days: {complete_days}\nRemaining Pages: {remaining_pages}",
                fg="green"
            )
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid positive whole numbers.")
            label_result.config(text="")
        except ZeroDivisionError:
            messagebox.showerror("Invalid Input", "Pages per day cannot be zero.")
            label_result.config(text="")

    lbl_total = Label(planner_window, text="Total Pages in Book:")
    lbl_total.pack(pady=5)
    entry_total = Entry(planner_window)
    entry_total.pack(pady=5)
    
    lbl_daily = Label(planner_window, text="Pages to Read Each Day:")
    lbl_daily.pack(pady=5)
    entry_daily = Entry(planner_window)
    entry_daily.pack(pady=5)
    
    btn_calculate = Button(planner_window, text="Calculate", command=calculate_schedule)
    btn_calculate.pack(pady=10)
    
    label_result = Label(planner_window, text="", font=("Arial", 10, "bold"))
    label_result.pack(pady=10)

# Main window widgets
lbl_welcome = Label(root, text="Welcome to the Reading Planner!", font=("Arial", 12))
lbl_welcome.pack(pady=20)

btn_open = Button(root, text="Open Schedule Planner Window", command=open_planner, padx=10)
btn_open.pack(pady=10)

root.mainloop()
