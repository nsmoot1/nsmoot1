"""
STREAMLIT WEB APP: Repair Manager V1.0
A web-based interface for managing repair tickets using Streamlit
"""

import streamlit as st
import datetime
import pandas as pd
from repair_ticket import RepairTicket
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Repair Manager", layout="wide", initial_sidebar_state="expanded")

# --- GLOBAL CONSTANTS ---
PRICES_FILE = "repair_prices.txt"
HISTORY_FILE = "repair_history.txt"
REPORT_FILE = "repair_report.txt"

# --- FUNCTIONS ---
def load_prices():
    """Gets repair prices from repair_prices.txt"""
    prices = {}
    try:
        with open(PRICES_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                prices[parts[0].strip()] = float(parts[1].strip())
    except FileNotFoundError:
        st.error("Prices file not found.")
    return prices

def load_history():
    """Loads all repair records from repair_history.txt"""
    history = []
    try:
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r") as file:
                for line in file:
                    if line.strip():
                        history.append(line.strip())
    except FileNotFoundError:
        pass
    return history

def save_ticket(customer_info, price):
    """Saves a new ticket to repair_history.txt and report file"""
    name, email, device = customer_info
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(HISTORY_FILE, "a") as file:
            file.write(f"{name},{email},{device},Unknown Service,{price:.2f},Received,{timestamp}\n")
        
        with open(REPORT_FILE, "w") as file:
            file.write(f"[{timestamp}]\n")
            file.write(f"Customer: {name}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Device: {device}\n")
            file.write(f"Total: ${price:.2f}\n")
            file.write("-" * 50 + "\n")
        return True
    except Exception as e:
        st.error(f"Error saving ticket: {e}")
        return False

def parse_history_line(line):
    """Parses a history file line into components"""
    parts = [p.strip() for p in line.split(",")]
    if len(parts) >= 7:
        try:
            return {
                "Name": parts[0],
                "Email": parts[1],
                "Device": parts[2],
                "Service": parts[3],
                "Price": float(parts[4]),
                "Status": parts[5],
                "Timestamp": parts[6]
            }
        except (ValueError, IndexError):
            pass
    return None

def load_tickets_with_indices():
    """Loads tickets and tracks their line indices in the history file"""
    history = load_history()
    tickets_with_indices = []
    
    for line_idx, line in enumerate(history):
        parsed = parse_history_line(line)
        if parsed:
            parsed['_line_index'] = line_idx
            tickets_with_indices.append(parsed)
    
    return tickets_with_indices

def update_ticket_status(line_index, new_status):
    """Updates a ticket's status in the history file"""
    history = load_history()
    if 0 <= line_index < len(history):
        parts = [p.strip() for p in history[line_index].split(",")]
        if len(parts) >= 7:
            parts[5] = new_status
            history[line_index] = ",".join(parts)
            
            try:
                with open(HISTORY_FILE, "w") as file:
                    for h in history:
                        file.write(h + "\n")
                return True
            except Exception as e:
                st.error(f"Error updating ticket: {e}")
                return False
    return False

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🔧 Repair Manager")
page = st.sidebar.radio("Navigation", ["📋 New Ticket", "📂 View Tickets", "📊 Analytics"])

# --- PAGE: NEW TICKET ---
if page == "📋 New Ticket":
    st.header("Create New Repair Ticket")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Customer Information")
        customer_name = st.text_input("Customer Name", placeholder="John Doe")
        customer_email = st.text_input("Customer Email", placeholder="john@example.com")
    
    with col2:
        st.subheader("Device Information")
        device_type = st.text_input("Device Type", placeholder="Laptop, Desktop, etc.")
        
    # Load available services
    prices = load_prices()
    if prices:
        st.subheader("Select Service")
        service = st.selectbox("Service Type", list(prices.keys()))
        price = prices[service]
        
        col3, col4 = st.columns(2)
        with col3:
            st.metric("Service Price", f"${price:.2f}")
        
        # Create button
        if st.button("✅ Create Ticket", use_container_width=True, type="primary"):
            if customer_name and customer_email and device_type:
                if save_ticket((customer_name, customer_email, device_type), price):
                    st.success(f"✓ Ticket created successfully!")
                    st.balloons()
                    
                    # Display receipt
                    st.markdown("---")
                    st.subheader("Receipt")
                    receipt_cols = st.columns(2)
                    with receipt_cols[0]:
                        st.write(f"**Customer:** {customer_name}")
                        st.write(f"**Email:** {customer_email}")
                    with receipt_cols[1]:
                        st.write(f"**Device:** {device_type}")
                        st.write(f"**Service:** {service}")
                    st.write(f"**Total:** ${price:.2f}")
                    st.write(f"**Timestamp:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                st.error("Please fill in all fields.")
    else:
        st.error("No services available. Please check repair_prices.txt")

# --- PAGE: VIEW TICKETS ---
elif page == "📂 View Tickets":
    st.header("Repair Ticket History")
    
    tickets = load_tickets_with_indices()
    
    if tickets:
        # Display as table (remove internal _line_index for display)
        display_tickets = [{k: v for k, v in t.items() if k != '_line_index'} for t in tickets]
        df = pd.DataFrame(display_tickets)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Filter by status
        st.subheader("Update Ticket Status")
        statuses = ["Received", "In Progress", "Completed", "Ready for Pickup", "Cancelled"]
        
        ticket_labels = [f"{t['Name']} - {t['Device']} ({t['Timestamp']})" for t in tickets]
        selected_ticket_label = st.selectbox("Select Ticket", ticket_labels)
        selected_idx = ticket_labels.index(selected_ticket_label)
        
        if selected_idx is not None and selected_idx >= 0:
            current_ticket = tickets[selected_idx]
            new_status = st.selectbox("New Status", statuses, index=statuses.index(current_ticket["Status"]))
            
            if st.button("🔄 Update Status", use_container_width=True):
                line_index = current_ticket['_line_index']
                if update_ticket_status(line_index, new_status):
                    st.success(f"✓ Ticket status updated to '{new_status}'")
                    st.rerun()
                else:
                    st.error("Failed to update ticket status")
    else:
        st.info("📭 No repair tickets yet. Create one from the 'New Ticket' page.")

# --- PAGE: ANALYTICS ---
elif page == "📊 Analytics":
    st.header("Analytics Dashboard")
    
    tickets = load_tickets_with_indices()
    
    if tickets:
        # Remove internal _line_index for display
        display_tickets = [{k: v for k, v in t.items() if k != '_line_index'} for t in tickets]
        df = pd.DataFrame(display_tickets)
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Tickets", len(df))
        
        with col2:
            total_revenue = df["Price"].sum()
            st.metric("Total Revenue", f"${total_revenue:.2f}")
        
        with col3:
            avg_price = df["Price"].mean()
            st.metric("Average Repair Cost", f"${avg_price:.2f}")
        
        with col4:
            completed = len(df[df["Status"].isin(["Completed", "Ready for Pickup"])])
            st.metric("Completed", completed)
        
        # Charts
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Tickets by Status")
            status_counts = df["Status"].value_counts()
            st.bar_chart(status_counts)
        
        with col2:
            st.subheader("Tickets by Device Type")
            device_counts = df["Device"].value_counts()
            st.bar_chart(device_counts)
        
        st.subheader("Revenue by Service")
        service_revenue = df.groupby("Service")["Price"].sum()
        st.bar_chart(service_revenue)
        
        # Detailed table
        st.markdown("---")
        st.subheader("All Tickets (Detailed)")
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("📭 No repair tickets yet. Create one from the 'New Ticket' page.")

# --- FOOTER ---
st.markdown("---")
st.markdown("🔧 **Repair Manager v1.0** | Built with Streamlit")
