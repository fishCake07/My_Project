import random
import time
from tkinter import *
from tkinter import messagebox
from ui_utils import center_window
class App(Tk):
    def __init__(self):
        super().__init__()

        # Center Window
        center_window(self, 800, 500)

        # Title, size, icon
        self.title("Timed Math Challenge")
        self.image = PhotoImage(file='assets\calculator.png')
        self.iconphoto(True, self.image)
        self.label_title = Label(self, text="Timed Math Challenge", font=('Helvetica', 24, 'bold'), bg='#ccffff')
        self.label_title.pack(pady=20)
        self.config(bg='#ccffff')

        # Math Problem_count
        self.problem_count_label = Label(self, text="", font=('Helvetica', 20), bg='#ccffff')
        self.problem_count_label.pack(pady=5)

        # Math Problem
        self.problem_label = Label(self, text='', font=('Helvetica', 18, 'bold'), bg='#ccffff')
        self.problem_label.pack(pady=5)

        # User's Answer
        self.user_entry = Entry(self, justify='center', font=('Helvetica', 16), width=25)
        self.user_entry.focus()
        self.user_entry.bind("<Return>", self.check)
        self.user_entry.pack(pady=10)

        # Submit button
        self.submit_button = Button(self,text='Submit', font=('Helvetica', 15), width=10,bg='#d9ffcc', command=self.check)
        self.submit_button.pack(pady=10)
        
        # True_False Label
        self.true_false_answer_label = Label(self, text='', font=('Helvetica', 17), fg='red', bg="#ccffff")
        self.true_false_answer_label.pack(pady=10)

        # Elapsed Time Label
        self.elapsed_time_label = Label(self, text='0.00 seconds', font=('Helvetica', 30, 'bold'), bg='#ccffff')
        self.elapsed_time_label.pack()

        # Variables
        self.problem_count = 1
        self.wrong = 0
        self.correct = 0
        
        # Start the challenge
        self.is_running = False
        self.start_time = time.time()
        self.generate_problems()
        self.update_ui()

    # Define Check Answer Function
    def check(self, event=None):
        try:
            user_input = self.user_entry.get()
            # Solve the 1 (user_input) not equal to 1.0 (answer) issue
            user_numeric_answer = float(user_input)
            # Make sure user input something
            if not user_input:
                messagebox.showerror("Error", "Please enter your answer!")
                print("Please enter your answer!")
            else:
                if self.problem_count < 10:
                    if user_numeric_answer == self.answer:
                            self.problem_count += 1
                            print("correct!")
                            # Display 'Correct' label
                            self.true_false_answer_label.config(text='Correct!')
                            # 'Correct' label disappear after 0.8 second
                            self.true_false_answer_label.after(800, self.hide)
                            self.user_entry.delete(0, END)
                            self.generate_problems()
                            self.update_ui()
                    else:                           
                        print("Incorrect. Try again!")
                        # Display 'Incorrect' label
                        self.true_false_answer_label.config(text="Incorrect. Please try again!")
                        # 'Incorrect' label disapper after 0.8 second
                        self.true_false_answer_label.after(800, self.hide)
                        self.user_entry.delete(0, END)
                        self.wrong += 1
                else:
                    # Stop time
                    self.stop()
                    self.user_entry.config(state="disabled")
                    self.submit_button.config(state="disabled")
                    messagebox.showinfo(title="Finish", 
                                        message=f"Congratulations! You conquered the challenge in {self.total_time:.2f} seconds.\nTotal wrong attempt: {self.wrong}.\nTotal correct attempt:{10 - self.wrong}.")
                    print(f'Total time: {self.total_time} seconds')
                    self.destroy()
        # Catch invalid number and non number characters
        except ValueError:
            print("That's invalid number.")
            messagebox.showerror("Error", "That's invalid number.")

    # Update elapsed time every 50 milliseconds
    def update_time(self):
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
            self.elapsed_time_label.config(text=f"{self.elapsed_time:.2f} seconds")
            self.elapsed_time_label.after(50, self.update_time)
    # Start Time Function
    def start(self):
        if not self.is_running:
            self.is_running = True
            print("START!")
            self.update_time()
    # Stop Time Function
    def stop(self):
        if self.is_running:
            self.is_running = False
            print("STOP!")
            self.total_time = time.time() - self.start_time
            self.elapsed_time_label.config(text=f"Total time: {self.total_time:.2f} seconds")
            print(f'Total time: {self.total_time:.2f} seconds')

    # Hide the true_false label
    def hide(self):
        self.true_false_answer_label.config(text='')
        
    # Generate Math Problems
    def generate_problems(self):
        # start time
        self.start()
        self.left = random.randint(3, 12)
        self.right = random.randint(3, 12)
        self.operand = random.choice(["+", "-", "*", "/"])
        self.math_equation = f"{self.left} {self.operand} {self.right}"
        self.answer = round(eval(self.math_equation),2)
        self.problem_label.config(text=self.math_equation)
        print("Problem #", self.problem_count)
        print(self.answer)

    # Update User Interface
    def update_ui(self):
        #print("Next question")
        self.problem_label.config(text=self.math_equation)
        self.problem_count_label.config(text=f"Problem # {self.problem_count}")

if __name__ == "__main__":
    app = App()
    app.mainloop()