import tkinter as tk
from tkinter import ttk, filedialog

class CollectorGui():
    def __init__(self):
        x=5

    def choose_output_directory(self):
        directory = filedialog.askdirectory(title="Select Output Directory")
        if directory:
            self.output_directory_var.set(directory)


    def toggle_automation_fields(self):
        """Enable automation-specific fields only when automation is checked."""
        if self.automation_var.get():
            scope_hosts_text.config(state="normal")
            crawl_minutes_entry.config(state="normal")
        else:
            scope_hosts_text.config(state="disabled")
            crawl_minutes_entry.config(state="disabled")


    def build_gui(self):

        self.root = tk.Tk()
        self.root.title("HAR Collector")
        self.root.geometry("700x550")
        self.root.resizable(False, False)


        # --------------------------------------------------
        # Main container
        # --------------------------------------------------

        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)
        main_frame.columnconfigure(1, weight=1)


        # --------------------------------------------------
        # Variables
        # --------------------------------------------------

        self.output_directory_var = tk.StringVar()
        proxy_var = tk.StringVar()
        start_url_var = tk.StringVar()

        self.automation_var = tk.BooleanVar(value=False)

        crawl_minutes_var = tk.StringVar()


        # --------------------------------------------------
        # Output Directory
        # --------------------------------------------------

        ttk.Label(
            main_frame,
            text="Output Directory:"
        ).grid(
            row=0,
            column=0,
            sticky="nw",
            padx=(0, 10),
            pady=8
        )

        output_frame = ttk.Frame(main_frame)
        output_frame.grid(row=0, column=1, sticky="ew", pady=8)
        output_frame.columnconfigure(0, weight=1)

        output_directory_entry = ttk.Entry(output_frame, textvariable=self.output_directory_var)
        output_directory_entry.grid(row=0, column=0, sticky="ew")

        browse_button = ttk.Button(output_frame, text="Browse...", command=self.choose_output_directory)
        browse_button.grid(row=0, column=1, padx=(8, 0))


        # --------------------------------------------------
        # Proxy
        # --------------------------------------------------

        ttk.Label(
            main_frame,
            text="Proxy:"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=(0, 10),
            pady=8
        )

        proxy_entry = ttk.Entry(main_frame, textvariable=proxy_var)
        proxy_entry.grid(row=1, column=1, sticky="ew", pady=8)


        # --------------------------------------------------
        # Start URL
        # --------------------------------------------------

        ttk.Label(
            main_frame,
            text="Start URL:"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=(0, 10),
            pady=8
        )

        start_url_entry = ttk.Entry(main_frame, textvariable=start_url_var)
        start_url_entry.grid(row=2, column=1, sticky="ew", pady=8)


        # --------------------------------------------------
        # Automation
        # --------------------------------------------------

        ttk.Label(
            main_frame,
            text="Automation:"
        ).grid(
            row=3,
            column=0,
            sticky="w",
            padx=(0, 10),
            pady=8
        )

        automation_checkbox = ttk.Checkbutton(
            main_frame,
            text="Enable automation",
            variable=self.automation_var,
            command=self.toggle_automation_fields
        )

        automation_checkbox.grid(row=3, column=1, sticky="w", pady=8)


        # --------------------------------------------------
        # In Scope Hosts
        # --------------------------------------------------

        ttk.Label(
            main_frame,
            text="In Scope Hosts:"
        ).grid(
            row=4,
            column=0,
            sticky="nw",
            padx=(0, 10),
            pady=8
        )

        scope_hosts_text = tk.Text(main_frame, height=6, width=50, wrap="none", state="disabled")
        scope_hosts_text.grid(row=4, column=1, sticky="ew", pady=8)


        # --------------------------------------------------
        # Crawl Time
        # --------------------------------------------------

        ttk.Label(
            main_frame,
            text="Time to Crawl (minutes):"
        ).grid(
            row=5,
            column=0,
            sticky="w",
            padx=(0, 10),
            pady=8
        )

        crawl_minutes_entry = ttk.Entry(main_frame, textvariable=crawl_minutes_var, state="disabled")
        crawl_minutes_entry.grid(row=5, column=1, sticky="ew", pady=8)


        # --------------------------------------------------
        # Separator
        # --------------------------------------------------

        separator = ttk.Separator(main_frame, orient="horizontal")
        separator.grid(row=6, column=0, columnspan=2, sticky="ew", pady=(20, 15))


        # --------------------------------------------------
        # Buttons
        # --------------------------------------------------

        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=7, column=0, columnspan=2)

        start_button = ttk.Button(button_frame, text="Start")
        start_button.grid(row=0, column=0, padx=8)

        pause_button = ttk.Button(button_frame, text="Pause")
        pause_button.grid(row=0, column=1, padx=8)

        stop_button = ttk.Button(button_frame, text="Stop")
        stop_button.grid(row=0, column=2, padx=8)


    def mainloop(self):
        self.root.mainloop()

gui = CollectorGui()
gui.build_gui()
gui.mainloop()
