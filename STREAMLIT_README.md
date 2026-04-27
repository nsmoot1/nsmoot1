# Repair Manager - Streamlit Web App

A web-based interface for managing repair tickets using Streamlit.

## Features

✨ **Create New Tickets** - Add customer repairs with service selection and pricing
📂 **View Tickets** - Browse all repair tickets and update their status
📊 **Analytics Dashboard** - Track revenue, ticket counts, and service statistics

## Requirements

- Python 3.7+
- Streamlit 1.0.0+
- Pandas 1.0.0+

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure you have the following files in the project directory:
   - `repair_prices.txt` - Service pricing data
   - `repair_ticket.py` - RepairTicket class
   - `repair_app_streamlit.py` - Streamlit application

## Running the App

From the project directory, run:

```bash
streamlit run repair_app_streamlit.py
```

The app will open in your default browser at `http://localhost:8501`

## Data Files

The app uses the following data files:

- **repair_prices.txt** - Contains service types and prices (CSV format)
  ```
  Diagnostics,40.00
  Virus Removal,90.00
  OS Installation,100.00
  Data Backup/Recovery,95.00
  ```

- **repair_history.txt** - Logs all created tickets (auto-generated)
  ```
  Customer Name,Email,Device,Service,Price,Status,Timestamp
  ```

- **repair_report.txt** - Latest ticket receipt (auto-generated)

## Usage

### 📋 New Ticket Page
1. Enter customer information (name, email, device type)
2. Select a service from the available options
3. Click "Create Ticket" to save
4. View the generated receipt

### 📂 View Tickets Page
1. Browse all repair tickets in table format
2. Select a ticket to update its status
3. Choose a new status from the dropdown
4. Click "Update Status" to save changes

Status options:
- Received (default)
- In Progress
- Completed
- Ready for Pickup
- Cancelled

### 📊 Analytics Page
View business metrics:
- Total tickets and revenue
- Average repair cost
- Completion rate
- Charts showing:
  - Tickets by status
  - Tickets by device type
  - Revenue by service

## File Structure

```
nsmoot1/
├── repair_app_streamlit.py    # Main Streamlit app
├── repair_ticket.py            # RepairTicket class
├── repair_manager.py           # Original CLI version
├── repair_prices.txt           # Service pricing data
├── repair_history.txt          # Ticket log (auto-generated)
├── repair_report.txt           # Latest ticket receipt (auto-generated)
└── requirements.txt            # Python dependencies
```

## Differences from CLI Version

The Streamlit web app improves upon the original CLI version:

- **Interactive GUI** - No console input required
- **Visual History** - See all tickets in a formatted table
- **Status Updates** - Update tickets without navigating a menu
- **Analytics** - Real-time business insights and charts
- **Receipt Display** - Immediate visual feedback after ticket creation

## Troubleshooting

**Port 8501 already in use:**
```bash
streamlit run repair_app_streamlit.py --server.port 8502
```

**Prices file not found:**
Make sure `repair_prices.txt` exists in the same directory as the script.

**No tickets appearing:**
Check that `repair_history.txt` exists or create a new ticket to generate it.

## Future Enhancements

- Customer search and filtering
- Ticket notes and history tracking
- Email notifications
- Service-specific pricing templates
- Multi-user login system
- Database backend instead of text files
