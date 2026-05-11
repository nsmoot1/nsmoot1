# Repair Manager System

A comprehensive web-based repair ticket management system built with **Streamlit** and **Python**. Track customer repairs, manage pricing, and analyze business metrics all in one place.

---

## ✨ Features

- **📝 Ticket Creation** - Easily create new repair tickets with customer details, device information, and service selection
- **📊 Ticket Management** - View all repair records, update ticket status, and track repair progress in real-time
- **💰 Pricing Management** - Automatic price calculation based on selected services
- **📈 Analytics Dashboard** - Revenue metrics, completion statistics, and visual charts for business insights
- **📱 Mobile Responsive** - Optimized UI/UX for desktop and mobile devices
- **💾 Data Persistence** - Automatic saving and loading of repair history and pricing data
- **🏗️ Object-Oriented Design** - Built with Python classes for maintainability and scalability

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository:**
```bash
git clone <your-repo-url>
cd repair-manager
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
streamlit run repair_app_streamlit.py
```

4. **Access the app:**
- Open your browser and navigate to `http://localhost:8501`
- The app will automatically detect your pricing and history files

---

## 📋 How to Use

### Tab 1: Create New Tickets
1. Enter customer name and email
2. Select the device type
3. Choose a service from the available options
4. Review auto-calculated price
5. Submit to save the ticket

### Tab 2: View Tickets
1. Browse all repair records
2. Update ticket status (Received, In Progress, Completed, Cancelled)
3. Track ticket details and history

### Tab 3: Analytics
1. View total revenue and ticket statistics
2. Analyze service popularity
3. Track completion rates with visual charts

---

## 📁 Project Structure

```
├── app.py                       # Main application setup (legacy)
├── repair_app_streamlit.py      # Streamlit web application
├── repair_ticket.py             # RepairTicket class (OOP backend)
├── repair_manager.py            # Core ticket management logic
├── repair_prices.txt            # Pricing data (auto-generated)
├── repair_history.txt           # Repair ticket history
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

---

## 🔧 Technical Details

### Core Classes

**RepairTicket**
- Manages individual repair ticket data with encapsulation
- Stores customer info, service details, pricing, and status
- Includes getters and setters for all attributes

**RepairManager**
- Handles ticket creation, updates, and retrieval
- Manages data persistence to text files
- Provides analytics and reporting functions

### Data Persistence

The system uses text files for data storage:
- `repair_prices.txt` - Service pricing configuration
- `repair_history.txt` - Complete repair ticket history

Data is automatically loaded on startup and saved with each operation.

---

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | ≥1.0.0 | Web application framework |
| pandas | ≥1.0.0 | Data manipulation and analysis |

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## 🎯 Assignment Checklist

This project fulfills the following requirements:

- [x] Streamlit Migration - Logic successfully ported to web UI
- [x] UI/UX Design - Organized, intuitive, and easy-to-navigate layout
- [x] GitHub Integration - Full source code in public repository
- [x] System Resilience - Graceful handling of invalid inputs
- [x] OOP Backend - Classes/Objects used for data management
- [x] Data Persistence - Reads/writes to text files
- [x] Mobile Responsiveness - Fully responsive design

---

## 💡 Tips & Best Practices

- **Before running:** Ensure Python and pip are installed and added to your PATH
- **Troubleshooting:** If the app doesn't open, check that port 8501 is available
- **File locations:** Keep all `.txt` data files in the same directory as the Python scripts
- **Updates:** Modify `repair_prices.txt` directly to add new services and pricing

---

## 👨‍💻 Developer Notes

- **Language:** Python 3
- **Framework:** Streamlit
- **Architecture:** Object-Oriented Programming (OOP)
- **Data Format:** Plain text files (.txt)

---

## 📄 License

This project is open source and available for educational and commercial use.

---

## 🤝 Contributing

Feel free to fork, modify, and improve this project. Submit pull requests with enhancements and bug fixes.

---

## 📞 Support

For issues, questions, or suggestions, please open an issue in the repository.

---

**Happy repairing! 🔧✨**
