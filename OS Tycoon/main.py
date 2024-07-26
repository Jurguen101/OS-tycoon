import tkinter as tk
from tkinter import simpledialog, messagebox
import random

class OperatingSystem:
    def __init__(self, name):
        self.name = name
        self.market_share = random.uniform(0, 10)  # Market share in percentage
        self.revenue = 0
        self.packages = []
        self.version = 1
        self.update_count = 0
        self.r_and_d_investment = 0
        self.marketing_campaigns = 0
        self.customizations = []
        self.maintenance_cost = 1000
        self.employee_salaries = 5000
        self.debt = 0

    def launch(self):
        self.revenue = (self.market_share * random.uniform(1000, 5000)) - self.maintenance_cost - self.employee_salaries
        return f"{self.name} launched with market share of {self.market_share:.2f}% and revenue of ${self.revenue:.2f}"

    def add_package(self, package_name):
        self.packages.append(package_name)
        self.revenue += 500  # Increase revenue for each package added

    def apply_event(self, event):
        self.revenue += event['impact']
        return f"{self.name} {event['description']} Impact: ${event['impact']:.2f}"

    def update(self):
        self.update_count += 1
        self.version += 0.1
        return f"The distro {self.name} has been updated to version {self.version:.1f}"

    def invest_in_r_and_d(self, amount):
        self.r_and_d_investment += amount
        self.revenue -= amount
        improvement = amount * 0.1
        self.market_share += improvement
        return f"Invested ${amount} in R&D. Market share increased by {improvement:.2f}%."

    def run_marketing_campaign(self, amount):
        self.marketing_campaigns += amount
        self.revenue -= amount
        visibility_increase = amount * 0.05
        self.market_share += visibility_increase
        return f"Spent ${amount} on marketing. Market share increased by {visibility_increase:.2f}%."

    def participate_in_competition(self):
        competition_result = random.choice(["won", "lost"])
        if competition_result == "won":
            bonus = random.uniform(2000, 5000)
            self.revenue += bonus
            return f"Participated in a competition and won! Bonus: ${bonus:.2f}"
        else:
            return "Participated in a competition and lost."

    def customize_interface(self, customization):
        self.customizations.append(customization)
        satisfaction_increase = 0.1
        self.market_share += satisfaction_increase
        return f"Applied customization: {customization}. Market share increased by {satisfaction_increase:.2f}%."

    def manage_finances(self, action, amount):
        if action == "borrow":
            self.debt += amount
            self.revenue += amount
            return f"Borrowed ${amount}. Total debt: ${self.debt:.2f}"
        elif action == "repay":
            if amount <= self.debt:
                self.debt -= amount
                self.revenue -= amount
                return f"Repaid ${amount}. Remaining debt: ${self.debt:.2f}"
            else:
                return "Repayment amount exceeds debt."

class OSTycoonGame:
    def __init__(self, root):
        self.root = root
        self.root.title("OS Tycoon")
        
        self.running = False
        self.paused = False
        self.time_elapsed = 0

        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        # Top frame for OS name, version, and timer
        self.top_frame = tk.Frame(self.frame)
        self.top_frame.grid(row=0, column=0, columnspan=2)

        self.os_name_label = tk.Label(self.top_frame, text="OS Name: Not Started")
        self.os_name_label.grid(row=0, column=0, sticky='w')

        self.version_label = tk.Label(self.top_frame, text="Version: 1.0")
        self.version_label.grid(row=0, column=1, sticky='e')

        self.timer_label = tk.Label(self.top_frame, text="Time Elapsed: 0s")
        self.timer_label.grid(row=1, column=0, columnspan=2, sticky='w')

        # Middle frame for events and rankings
        self.middle_frame = tk.Frame(self.frame)
        self.middle_frame.grid(row=1, column=0, columnspan=2)

        self.events_label = tk.Label(self.middle_frame, text="Events", font=("Helvetica", 12, "bold"))
        self.events_label.grid(row=0, column=0, padx=5, pady=5)

        self.events_log = tk.Text(self.middle_frame, state='disabled', height=10, width=50)
        self.events_log.grid(row=1, column=0, padx=5, pady=5)

        self.distro_rank_label = tk.Label(self.middle_frame, text="DistroRank", font=("Helvetica", 12, "bold"))
        self.distro_rank_label.grid(row=0, column=1, padx=5, pady=5)

        self.distro_rank_log = tk.Text(self.middle_frame, state='disabled', height=10, width=50)
        self.distro_rank_log.grid(row=1, column=1, padx=5, pady=5)

        # Bottom frame for buttons
        self.bottom_frame = tk.Frame(self.frame)
        self.bottom_frame.grid(row=2, column=0, columnspan=2)

        self.packages_button = tk.Button(self.bottom_frame, text="Packages", command=self.open_packages_window, width=15)
        self.packages_button.grid(row=0, column=0, padx=5, pady=5)

        self.release_button = tk.Button(self.bottom_frame, text="Release", command=self.release_distro, width=15)
        self.release_button.grid(row=0, column=1, padx=5, pady=5)

        self.r_and_d_button = tk.Button(self.bottom_frame, text="Invest in R&D", command=self.invest_in_r_and_d, width=15)
        self.r_and_d_button.grid(row=1, column=0, padx=5, pady=5)

        self.marketing_button = tk.Button(self.bottom_frame, text="Run Marketing", command=self.run_marketing_campaign, width=15)
        self.marketing_button.grid(row=1, column=1, padx=5, pady=5)

        self.competition_button = tk.Button(self.bottom_frame, text="Participate in Competition", command=self.participate_in_competition, width=30)
        self.competition_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.customize_button = tk.Button(self.bottom_frame, text="Customize Interface", command=self.customize_interface, width=15)
        self.customize_button.grid(row=3, column=0, padx=5, pady=5)

        self.manage_finances_button = tk.Button(self.bottom_frame, text="Manage Finances", command=self.manage_finances, width=15)
        self.manage_finances_button.grid(row=3, column=1, padx=5, pady=5)

        self.start_button = tk.Button(self.bottom_frame, text="Start Game", command=self.start_game, width=15)
        self.start_button.grid(row=4, column=0, padx=5, pady=5)

        self.pause_button = tk.Button(self.bottom_frame, text="Pause", command=self.pause_game, width=15)
        self.pause_button.grid(row=4, column=1, padx=5, pady=5)

        self.quit_button = tk.Button(self.bottom_frame, text="Quit", command=self.root.quit, width=15)
        self.quit_button.grid(row=5, column=0, padx=5, pady=5)

        self.about_button = tk.Button(self.bottom_frame, text="About", command=self.show_about, width=15)
        self.about_button.grid(row=5, column=1, padx=5, pady=5)

    def start_game(self):
        if not self.running:
            self.running = True
            self.paused = False
            self.time_elapsed = 0

            # Get user's OS name
            user_os_name = simpledialog.askstring("Input", "Name your new Linux Distro.")
            if user_os_name:
                self.user_os = OperatingSystem(user_os_name)
                self.os_name_label.config(text=f"OS Name: {self.user_os.name}")
                self.version_label.config(text=f"Version: {self.user_os.version:.1f}")
                self.log_message(self.user_os.launch(), self.events_log)

                # Create and launch competitor OS
                competitor_names = ["CompOS", "RivalOS", "ContestOS"]
                self.competitors = [OperatingSystem(name) for name in competitor_names]
                for competitor in self.competitors:
                    self.log_message(competitor.launch(), self.events_log)

                self.update_time()
                self.update_rank()
                self.random_events()

    def update_time(self):
        if self.running and not self.paused:
            self.time_elapsed += 1
            minutes, seconds = divmod(self.time_elapsed, 60)
            self.timer_label.config(text=f"Time Elapsed: {minutes}m {seconds}s")
            self.root.after(1000, self.update_time)

    def pause_game(self):
        self.paused = not self.paused
        if not self.paused:
            self.update_time()

    def log_message(self, message, log_widget):
        log_widget.config(state='normal')
        log_widget.insert(tk.END, message + "\n")
        log_widget.config(state='disabled')

    def update_rank(self):
        if self.running and not self.paused:
            self.distro_rank_log.config(state='normal')
            self.distro_rank_log.delete(1.0, tk.END)
            rankings = sorted([self.user_os] + self.competitors, key=lambda os: os.revenue, reverse=True)
            for os in rankings:
                self.distro_rank_log.insert(tk.END, f"{os.name}: ${os.revenue:.2f}\n")
            self.distro_rank_log.config(state='disabled')
            self.root.after(5000, self.update_rank)

    def open_packages_window(self):
        packages_window = tk.Toplevel(self.root)
        packages_window.title("Select Packages")

        # Define available packages with descriptions
        self.available_packages = {
            "SuperApp": "A powerful application suite for productivity.",
            "MegaSuite": "An all-in-one software package with utilities and tools.",
            "CoolEditor": "A versatile text editor with advanced features.",
            "FastBrowser": "A lightning-fast web browser with privacy protection.",
            "SecureMail": "An email client with top-notch security features.",
            "PhotoMagic": "A photo editing application with various filters and tools."
        }
        self.package_vars = {}

        for package, description in self.available_packages.items():
            var = tk.BooleanVar()
            chk = tk.Checkbutton(packages_window, text=package, variable=var)
            chk.pack(anchor='w')
            desc_label = tk.Label(packages_window, text=description, wraplength=300)
            desc_label.pack(anchor='w')
            self.package_vars[package] = var

        ok_button = tk.Button(packages_window, text="Add Packages", command=self.add_packages)
        ok_button.pack()

    def add_packages(self):
        for package, var in self.package_vars.items():
            if var.get():
                self.user_os.add_package(package)
        messagebox.showinfo("Packages", "Packages added to your OS.")

    def release_distro(self):
        if hasattr(self, 'user_os'):
            update_message = self.user_os.update()
            release_message = f"The distro {self.user_os.name} has been released in its version {self.user_os.version:.1f}"
            self.log_message(update_message, self.events_log)
            self.log_message(release_message, self.events_log)
            messagebox.showinfo("Release", release_message)
            self.version_label.config(text=f"Version: {self.user_os.version:.1f}")

    def invest_in_r_and_d(self):
        amount = simpledialog.askfloat("Investment", "Enter amount for R&D investment:")
        if amount and amount > 0:
            self.log_message(self.user_os.invest_in_r_and_d(amount), self.events_log)

    def run_marketing_campaign(self):
        amount = simpledialog.askfloat("Marketing", "Enter amount for marketing campaign:")
        if amount and amount > 0:
            self.log_message(self.user_os.run_marketing_campaign(amount), self.events_log)

    def participate_in_competition(self):
        self.log_message(self.user_os.participate_in_competition(), self.events_log)

    def customize_interface(self):
        customization = simpledialog.askstring("Customization", "Enter a customization for your OS:")
        if customization:
            self.log_message(self.user_os.customize_interface(customization), self.events_log)

    def manage_finances(self):
        action = simpledialog.askstring("Finance", "Enter action (borrow/repay):")
        amount = simpledialog.askfloat("Amount", "Enter amount:")
        if action in ["borrow", "repay"] and amount is not None:
            self.log_message(self.user_os.manage_finances(action, amount), self.events_log)

    def random_events(self):
        if self.running and not self.paused:
            events = [
                {"description": "has gained popularity!", "impact": random.uniform(1000, 5000)},
                {"description": "has faced a security breach!", "impact": random.uniform(-5000, -1000)},
                {"description": "has been updated successfully!", "impact": random.uniform(1000, 5000)},
                {"description": "has faced a major bug!", "impact": random.uniform(-5000, -1000)},
                {"description": "has experienced a technological breakthrough!", "impact": random.uniform(2000, 7000)},
                {"description": "has been hit by an economic downturn!", "impact": random.uniform(-7000, -2000)},
                {"description": "has formed a strategic alliance!", "impact": random.uniform(3000, 8000)},
            ]

            all_os = [self.user_os] + self.competitors

            for os in all_os:
                event = random.choice(events)
                self.log_message(os.apply_event(event), self.events_log)

            self.update_rank()
            self.root.after(10000, self.random_events)  # Trigger next event in 10 seconds

    def show_about(self):
        messagebox.showinfo("About", "OS Tycoon Game\nVersion 1.0\nDeveloped by Jurguen Delgadillo")

if __name__ == "__main__":
    root = tk.Tk()
    game = OSTycoonGame(root)
    root.mainloop()
