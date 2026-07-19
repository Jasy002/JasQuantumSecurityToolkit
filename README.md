<div align="center">

# 🔐 Jas Quantum Security Toolkit

### A Python-Based BB84 Quantum Key Distribution Simulator with Eve Attack Detection

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Qiskit](https://img.shields.io/badge/Qiskit-Quantum-purple?style=for-the-badge)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-blue?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-success?style=for-the-badge)

A simulation of the **BB84 Quantum Key Distribution (QKD) Protocol** demonstrating secure quantum communication, secret key generation, and eavesdropping detection using the **Intercept–Resend Attack**.

</div>

---

# 📖 Introduction

Quantum Key Distribution (QKD) is one of the most important applications of quantum computing and quantum cryptography.

Unlike classical encryption, BB84 enables two communicating parties (**Alice** and **Bob**) to establish a secret cryptographic key while detecting any eavesdropper (**Eve**) through the **Quantum Bit Error Rate (QBER)**.

This project implements a complete BB84 simulation in Python with graphical analysis.

---

# ✨ Features

- 🔹 BB84 Quantum Key Distribution Simulation
- 🔹 Random Quantum Bit Generation
- 🔹 Random Basis Selection
- 🔹 Alice–Bob Secure Communication
- 🔹 Eve Intercept–Resend Attack
- 🔹 Secret Key Extraction
- 🔹 Quantum Bit Error Rate (QBER) Calculation
- 🔹 Security Decision
- 🔹 Automatic Graph Generation
- 🔹 Object-Oriented Python Design

---

# 🏗 Project Architecture

```text
                 Alice
                   │
        Random Bits & Bases
                   │
            Prepare Qubits
                   │
         Quantum Communication
                   │
        ┌────────────────────┐
        │  Eve (Optional)    │
        │Intercept & Resend  │
        └────────────────────┘
                   │
                   ▼
                 Bob
                   │
         Random Measurement
                   │
          Basis Comparison
                   │
         Secret Key Extraction
                   │
          QBER Calculation
                   │
          Security Analysis
```

---

# 📂 Project Structure

```text
JasQuantumSecurityToolkit/

│
├── outputs/
│   ├── accuracy.png
│   ├── attack_analysis.png
│   ├── key_distribution.png
│   └── qber.png
│
├── report/
│
├── bb84.py
├── config.py
├── eve.py
├── main.py
├── utils.py
├── visualization.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming |
| NumPy | Random Bit Generation |
| Matplotlib | Data Visualization |
| Qiskit | Quantum Computing Framework |

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/JasQuantumSecurityToolkit.git
```

Move into the project

```bash
cd JasQuantumSecurityToolkit
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Run

```bash
python main.py
```

---

# 📊 Sample Output

```text
==========================================================
BB84 QUANTUM KEY DISTRIBUTION
==========================================================

Total Qubits           : 100
Matching Bases         : 52
Secret Key Length      : 52
Measurement Accuracy   : 80.77 %
Quantum Bit Error Rate : 19.23 %
Security Status        : Possible Eavesdropping Detected

==========================================================
```

---

# 📈 Generated Graphs

The simulator automatically generates

- Measurement Accuracy
- Quantum Bit Error Rate
- Secret Key Distribution
- Eve Attack Analysis

inside

```text
outputs/
```

---

# 📸 Screenshots

After uploading to GitHub, add your generated images here.

```markdown
![Accuracy](outputs/accuracy.png)

![QBER](outputs/qber.png)

![Key Distribution](outputs/key_distribution.png)

![Attack Analysis](outputs/attack_analysis.png)
```

---

# 🔬 BB84 Workflow

1. Alice generates random bits.
2. Alice randomly selects bases.
3. Qubits are transmitted.
4. Eve optionally intercepts and resends qubits.
5. Bob measures using random bases.
6. Alice and Bob compare bases.
7. Matching bits become the secret key.
8. QBER is calculated.
9. Communication security is determined.

---

# 📌 Learning Outcomes

This project demonstrates

- Quantum Cryptography
- BB84 Protocol
- Quantum Communication
- Quantum Security
- Python Programming
- Object-Oriented Programming
- Data Visualization

---

# 🚀 Future Enhancements

- IBM Quantum Hardware Integration
- Quantum Circuit Visualization
- GUI using PyQt
- Noise Channel Simulation
- E91 Protocol
- B92 Protocol
- Multiple Eavesdropping Models
- Flask Web Dashboard

---

# 👩‍💻 Author

**Jasmine Sultana**

M.Tech (Computer Science & Engineering – AI/ML)

Research Interests

- Quantum Computing
- Quantum Cryptography
- Artificial Intelligence
- Machine Learning
- Cyber Security

GitHub:
https://github.com/Jasy002

LinkedIn:
(Add your LinkedIn URL)

---

# ⭐ Support

If you found this project helpful,

⭐ Star this repository

🍴 Fork this repository

📢 Share it with others

---

# 📄 License

This project is developed for educational and research purposes.

© 2026 Jasmine Sultana