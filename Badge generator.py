import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser, ttk

# ================= THEME ================= #
BG = "#0d1117"
FG = "#c9d1d9"
ACCENT = "#58a6ff"
BOX = "#161b22"

# ================= AI STYLE TEMPLATES ================= #
TEMPLATES = {
    "Professional": {
        "description": "This repository contains a production-ready implementation designed with scalability, maintainability, and performance in mind.",
        "features": "- Clean architecture\n- Modular design\n- Production-grade practices",
    },
    "Open Source": {
        "description": "An open-source project built with the community in mind. Contributions, issues, and discussions are welcome!",
        "features": "- Community-driven\n- Easy to contribute\n- Transparent development",
    },
    "Student Project": {
        "description": "This project was created as part of a learning journey to understand core concepts through hands-on implementation.",
        "features": "- Beginner friendly\n- Well commented\n- Educational focus",
    },
    "Research": {
        "description": "Experimental and research-oriented implementation exploring ideas, prototypes, and technical feasibility.",
        "features": "- Experimental design\n- Research focused\n- Rapid iteration",
    },
    "Startup": {
        "description": "A product-focused repository aimed at delivering real-world value with speed and innovation.",
        "features": "- MVP oriented\n- Fast iteration\n- Business focused",
    }
}

# ================= BADGES ================= #
BADGES = {

# ================= LANGUAGES ================= #

"Languages": {
    "Python": "https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white",
    "C": "https://img.shields.io/badge/C-A8B9CC?logo=c",
    "C++": "https://img.shields.io/badge/C%2B%2B-00599C?logo=c%2B%2B",
    "C#": "https://img.shields.io/badge/C%23-239120?logo=csharp",
    "Java": "https://img.shields.io/badge/Java-ED8B00?logo=openjdk",
    "JavaScript": "https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript",
    "TypeScript": "https://img.shields.io/badge/TypeScript-3178C6?logo=typescript",
    "Go": "https://img.shields.io/badge/Go-00ADD8?logo=go",
    "Rust": "https://img.shields.io/badge/Rust-000000?logo=rust",
    "Kotlin": "https://img.shields.io/badge/Kotlin-0095D5?logo=kotlin",
    "Swift": "https://img.shields.io/badge/Swift-FA7343?logo=swift",
    "PHP": "https://img.shields.io/badge/PHP-777BB4?logo=php",
    "Ruby": "https://img.shields.io/badge/Ruby-CC342D?logo=ruby",
    "R": "https://img.shields.io/badge/R-276DC3?logo=r",
    "MATLAB": "https://img.shields.io/badge/MATLAB-0076A8",
    "Dart": "https://img.shields.io/badge/Dart-0175C2?logo=dart",
    "Scala": "https://img.shields.io/badge/Scala-DC322F?logo=scala",
    "Haskell": "https://img.shields.io/badge/Haskell-5D4F85?logo=haskell",
    "Lua": "https://img.shields.io/badge/Lua-2C2D72?logo=lua",
    "Perl": "https://img.shields.io/badge/Perl-39457E?logo=perl"
},

# ================= FRAMEWORKS ================= #

"Frameworks": {
    "Django": "https://img.shields.io/badge/Django-092E20?logo=django",
    "Flask": "https://img.shields.io/badge/Flask-000000?logo=flask",
    "FastAPI": "https://img.shields.io/badge/FastAPI-009688?logo=fastapi",
    "Spring": "https://img.shields.io/badge/Spring-6DB33F?logo=spring",
    "React": "https://img.shields.io/badge/React-61DAFB?logo=react",
    "Next.js": "https://img.shields.io/badge/Next.js-000000?logo=nextdotjs",
    "Vue": "https://img.shields.io/badge/Vue.js-4FC08D?logo=vue.js",
    "Angular": "https://img.shields.io/badge/Angular-DD0031?logo=angular",
    "Svelte": "https://img.shields.io/badge/Svelte-FF3E00?logo=svelte",
    "Node.js": "https://img.shields.io/badge/Node.js-339933?logo=node.js",
    "Express": "https://img.shields.io/badge/Express-000000?logo=express",
    "Electron": "https://img.shields.io/badge/Electron-47848F?logo=electron"
},

# ================= DATABASES ================= #

"Databases": {
    "MySQL": "https://img.shields.io/badge/MySQL-4479A1?logo=mysql",
    "PostgreSQL": "https://img.shields.io/badge/PostgreSQL-336791?logo=postgresql",
    "SQLite": "https://img.shields.io/badge/SQLite-003B57?logo=sqlite",
    "MongoDB": "https://img.shields.io/badge/MongoDB-47A248?logo=mongodb",
    "Redis": "https://img.shields.io/badge/Redis-DC382D?logo=redis",
    "Firebase": "https://img.shields.io/badge/Firebase-FFCA28?logo=firebase",
    "DynamoDB": "https://img.shields.io/badge/DynamoDB-4053D6?logo=amazondynamodb"
},

# ================= DEVOPS ================= #

"DevOps / Cloud": {
    "Docker": "https://img.shields.io/badge/Docker-2496ED?logo=docker",
    "Kubernetes": "https://img.shields.io/badge/Kubernetes-326CE5?logo=kubernetes",
    "AWS": "https://img.shields.io/badge/AWS-232F3E?logo=amazonaws",
    "Azure": "https://img.shields.io/badge/Azure-0078D4?logo=microsoftazure",
    "GCP": "https://img.shields.io/badge/GCP-4285F4?logo=googlecloud",
    "Heroku": "https://img.shields.io/badge/Heroku-430098?logo=heroku",
    "Netlify": "https://img.shields.io/badge/Netlify-00C7B7?logo=netlify",
    "Vercel": "https://img.shields.io/badge/Vercel-000000?logo=vercel"
},

# ================= TOOLS ================= #

"Tools": {
    "Git": "https://img.shields.io/badge/Git-F05032?logo=git",
    "GitHub": "https://img.shields.io/badge/GitHub-181717?logo=github",
    "GitLab": "https://img.shields.io/badge/GitLab-FCA121?logo=gitlab",
    "VS Code": "https://img.shields.io/badge/VSCode-007ACC?logo=visualstudiocode",
    "PyCharm": "https://img.shields.io/badge/PyCharm-000000?logo=pycharm",
    "IntelliJ": "https://img.shields.io/badge/IntelliJ-000000?logo=intellijidea",
    "Jupyter": "https://img.shields.io/badge/Jupyter-F37626?logo=jupyter"
},

# ================= QUALITY / STATUS ================= #

"Quality & Status": {
    "Build Passing": "https://img.shields.io/badge/Build-Passing-brightgreen",
    "Tests Passing": "https://img.shields.io/badge/Tests-Passing-success",
    "Coverage High": "https://img.shields.io/badge/Coverage-90%25-brightgreen",
    "Maintained": "https://img.shields.io/badge/Maintained-Yes-brightgreen",
    "Active": "https://img.shields.io/badge/Status-Active-success",
    "Experimental": "https://img.shields.io/badge/Status-Experimental-orange",
    "Deprecated": "https://img.shields.io/badge/Status-Deprecated-red"
},

# ================= LICENSE ================= #

"License": {
    "MIT": "https://img.shields.io/badge/License-MIT-yellow",
    "Apache 2.0": "https://img.shields.io/badge/License-Apache%202.0-blue",
    "GPL v3": "https://img.shields.io/badge/License-GPLv3-blue",
    "BSD 3-Clause": "https://img.shields.io/badge/License-BSD%203--Clause-blue",
    "Unlicense": "https://img.shields.io/badge/license-Unlicense-blue"
}
 }

# ================= SECTIONS ================= #
SECTIONS = [
    ("📖 Description", "description"),
    ("✨ Features", "features"),
    ("⚙️ Installation", "installation"),
    ("🚀 Usage", "usage"),
    ("📦 Requirements", "requirements"),
    ("🛣️ Roadmap", "roadmap"),
    ("❓ FAQ", "faq"),
    ("⚠️ Limitations", "limits"),
    ("🔮 Future Scope", "future"),
    ("🤝 Contributing", "contributing"),
    ("⭐ Support", "star"),
    ("📜 License", "license"),
]

# ================= APP ================= #
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Offline README Generator — AI Templates GOD MODE")
        self.root.geometry("1100x820")
        self.root.configure(bg=BG)

        self.badges = []
        self.section_vars = {}
        self.section_inputs = {}

        self.build_scroll()

    # ---------- SCROLLABLE UI ----------
    def build_scroll(self):
        canvas = tk.Canvas(self.root, bg=BG)
        scrollbar = tk.Scrollbar(self.root, command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        self.container = tk.Frame(canvas, bg=BG)
        canvas.create_window((0, 0), window=self.container, anchor="nw")

        self.container.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        self.ui()

    # ---------- UI ----------
    def ui(self):
        tk.Label(
            self.container,
            text="🤖 AI-Style Offline README Generator",
            font=("Segoe UI", 22, "bold"),
            bg=BG,
            fg=ACCENT
        ).pack(pady=10)

        self.project_name = self.entry("Project Name")

        self.template = tk.StringVar(value="Professional")
        tk.Label(self.container, text="AI-Style Template", bg=BG, fg=FG).pack(anchor="w", padx=10)
        ttk.Combobox(
            self.container,
            textvariable=self.template,
            values=list(TEMPLATES.keys()),
            state="readonly"
        ).pack(fill="x", padx=10)

        self.build_badges()
        self.custom_badge_builder()
        self.build_sections()

        self.output = tk.Text(self.container, height=12, bg=BOX, fg=FG)
        self.output.pack(fill="x", padx=10, pady=10)

        tk.Button(self.container, text="🧾 Generate README", bg=ACCENT, command=self.generate).pack(pady=4)
        tk.Button(self.container, text="💾 Save README.md", bg=ACCENT, command=self.save).pack(pady=4)

    def entry(self, label):
        tk.Label(self.container, text=label, bg=BG, fg=FG).pack(anchor="w", padx=10)
        e = tk.Entry(self.container)
        e.pack(fill="x", padx=10, pady=4)
        return e

    # ---------- BADGES ----------
    def build_badges(self):
        for cat, items in BADGES.items():
            frame = tk.LabelFrame(self.container, text=cat, bg=BG, fg=FG)
            frame.pack(fill="x", padx=10, pady=4)
            for name, url in items.items():
                var = tk.BooleanVar()
                tk.Checkbutton(
                    frame,
                    text=name,
                    variable=var,
                    bg=BG,
                    fg=FG,
                    selectcolor=BG,
                    command=lambda u=url, v=var: self.toggle_badge(u, v)
                ).pack(side="left", padx=4)

    def toggle_badge(self, url, var):
        md = f"![Badge]({url})"
        if var.get():
            self.badges.append(md)
        else:
            if md in self.badges:
                self.badges.remove(md)

    # ---------- CUSTOM BADGE ----------
    def custom_badge_builder(self):
        frame = tk.Frame(self.container, bg=BG)
        frame.pack(fill="x", padx=10, pady=8)

        tk.Label(frame, text="🧩 Custom Badge", bg=BG, fg=ACCENT).pack(anchor="w")

        self.c_label = tk.Entry(frame)
        self.c_label.insert(0, "Label")
        self.c_label.pack(side="left", padx=4)

        self.c_msg = tk.Entry(frame)
        self.c_msg.insert(0, "Message")
        self.c_msg.pack(side="left", padx=4)

        self.color = "4CAF50"
        tk.Button(frame, text="🎨 Color", command=self.pick_color).pack(side="left", padx=4)
        tk.Button(frame, text="➕ Add", command=self.add_custom_badge).pack(side="left", padx=4)

    def pick_color(self):
        c = colorchooser.askcolor()[1]
        if c:
            self.color = c.replace("#", "")

    def add_custom_badge(self):
        badge = f"![Badge](https://img.shields.io/badge/{self.c_label.get()}-{self.c_msg.get()}-{self.color})"
        self.badges.append(badge)
        messagebox.showinfo("Added", "Custom badge added!")

    # ---------- SECTIONS ----------
    def build_sections(self):
        template = TEMPLATES[self.template.get()]
        for title, key in SECTIONS:
            var = tk.BooleanVar(value=True)
            self.section_vars[key] = var

            tk.Checkbutton(
                self.container,
                text=title,
                variable=var,
                bg=BG,
                fg=FG,
                selectcolor=BG
            ).pack(anchor="w", padx=20)

            txt = tk.Text(self.container, height=4, bg=BOX, fg=FG)
            txt.insert("1.0", template.get(key, ""))
            txt.pack(fill="x", padx=30, pady=3)

            self.section_inputs[key] = (title, txt)

    # ---------- GENERATE ----------
    def generate(self):
        self.output.delete("1.0", "end")
        md = f"# {self.project_name.get()}\n\n{' '.join(self.badges)}\n\n"

        for key, enabled in self.section_vars.items():
            if enabled.get():
                title, txt = self.section_inputs[key]
                content = txt.get("1.0", "end").strip()
                if key == "star":
                    content = "If you find this project useful, please ⭐ **star the repository**."
                if content:
                    md += f"## {title}\n{content}\n\n"

        self.output.insert("end", md)

    # ---------- SAVE ----------
    def save(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".md",
            initialfile="README.md"
        )
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.output.get("1.0", "end"))
            messagebox.showinfo("Saved", "README.md saved successfully!")

# ---------- RUN ----------
if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
