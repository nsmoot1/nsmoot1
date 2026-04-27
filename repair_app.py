"""
Streamlit Web App: Repair Manager
A modern web interface for managing repair tickets
"""

import streamlit as st
import datetime
import pandas as pd
import os
from repair_ticket import RepairTicket

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Repair Manager", layout="wide", initial_sidebar_state="expanded")

# --- FILE PATHS ---
PRICES_FILE = "repair_prices.txt"
HISTORY_FILE = "repair_history.txt"
REPORT_FILE = "repair_report.txt"

# --- UTILITY FUNCTIONS ---
def load_prices():
    """Load repair prices from file"""
    prices = {}
    try:
        with open(PRICES_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    prices[parts[0].strip()] = float(parts[1].strip())
    except FileNotFoundError:
        st.warning("Prices file not found.")
    return prices

def load_history():
    """Load ticket history from file"""
    history = []
    try:
        with open(HISTORY_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) >= 3:
                    history.append({
                        "customer": parts[0].strip(),
                        "price": float(parts[1].strip()),
                        "timestamp": parts[2].strip()
                    })
    except FileNotFoundError:
        pass
    return history

# --- SESSION STATE INITIALIZATION ---
if "tickets" not in st.session_state:
    st.session_state.tickets = []
if "history" not in st.session_state:
    st.session_state.history = load_history()

def save_ticket_to_history(customer_info, price):
    """Save ticket to history file"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    customer_name = customer_info[0]
    try:
        with open(HISTORY_FILE, "a") as file:
            file.write(f"{customer_name}, {price:.2f}, {timestamp}\n")
        st.session_state.history = load_history()
        return timestamp
    except Exception as e:
        st.error(f"Error saving ticket: {e}")
        return None

def save_report(ticket, timestamp):
    """Save repair report to file"""
    try:
        with open(REPORT_FILE, "w") as file:
            file.write(f"[{timestamp}]\n")
            file.write(f"Customer: {ticket.get_name()}\n")
            file.write(f"Email: {ticket.get_email()}\n")
            file.write(f"Device: {ticket.get_device()}\n")
            file.write(f"Service: {ticket.get_service()}\n")
            file.write(f"Price: ${ticket.get_price():.2f}\n")
            file.write(f"Status: {ticket.get_status()}\n")
            file.write("-" * 50 + "\n")
    except Exception as e:
        st.error(f"Error saving report: {e}")



# --- MAIN APP ---
st.title("🔧 Repair Manager")
st.markdown("Professional repair ticket management system")

# --- SIDEBAR NAVIGATION ---
page = st.sidebar.radio("Navigation", ["New Ticket", "View History", "Reports"])

# --- PAGE: NEW TICKET ---
if page == "New Ticket":
    st.header("Create New Repair Ticket")
    
    col1, col2 = st.columns(2)
    
    with col1:
        customer_name = st.text_input("Customer Name", placeholder="Enter full name")
        customer_email = st.text_input("Customer Email", placeholder="Enter email address")
        device_type = st.text_input("Device Type", placeholder="e.g., Laptop, Desktop, Phone")
    
    with col2:
        prices = load_prices()
        service = st.selectbox("Select Service", list(prices.keys()))
        
        if service:
            price = prices.get(service, 0.0)
            st.metric("Service Price", f"${price:.2f}")
    
    if st.button("Create Ticket", use_container_width=True, type="primary"):
        if not customer_name or not customer_email or not device_type or not service:
            st.error("⚠️ Please fill in all fields")
        else:
            # Create ticket object
            ticket = RepairTicket(customer_name, customer_email, device_type)
            ticket.set_service(service)
            ticket.set_price(prices[service])
            ticket.set_status("Received")
            
            # Save to history
            timestamp = save_ticket_to_history((customer_name, customer_email, device_type), prices[service])
            
            if timestamp:
                save_report(ticket, timestamp)
                
                # Display ticket
                st.success("✅ Ticket Created Successfully!")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Ticket Details")
                    st.write(f"**Customer:** {ticket.get_name()}")
                    st.write(f"**Email:** {ticket.get_email()}")
                    st.write(f"**Device:** {ticket.get_device()}")
                
                with col2:
                    st.subheader("Service Information")
                    st.write(f"**Service:** {ticket.get_service()}")
                    st.metric("Total Price", f"${ticket.get_price():.2f}")
                    st.write(f"**Status:** {ticket.get_status()}")
                
                st.divider()
                st.write("**Ticket saved to history. Thank you for your business!**")

# --- PAGE: VIEW HISTORY ---
elif page == "View History":
    st.header("Ticket History")
    
    history = st.session_state.history
    
    if not history:
        st.info("No repair tickets in history yet.")
    else:
        df = pd.DataFrame(history)
        df["price"] = df["price"].apply(lambda x: f"${x:.2f}")
        
        st.subheader(f"Total Tickets: {len(history)}")
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            total_revenue = sum([float(item["price"].replace("$", "")) for item in df.values.tolist()])
            st.metric("Total Revenue", f"${total_revenue:.2f}")
        
        with col2:
            st.metric("Average Ticket", f"${total_revenue / len(history):.2f}")
        
        with col3:
            st.metric("Tickets Today", len([h for h in history if datetime.datetime.now().strftime("%Y-%m-%d") in h["timestamp"]]))

# --- PAGE: REPORTS ---
elif page == "Reports":
    st.header("Reports & Analytics")
    
    history = st.session_state.history
    
    if not history:
        st.info("No data available for reports yet.")
    else:
        df = pd.DataFrame(history)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Tickets", len(df))
        
        with col2:
            st.metric("Total Revenue", f"${df['price'].sum():.2f}")
        
        with col3:
            avg_price = df['price'].mean()
            st.metric("Average Price", f"${avg_price:.2f}")
        
        st.divider()
        
        # Service breakdown
        st.subheader("Service Breakdown")
        prices = load_prices()
        
        service_counts = {}
        for item in history:
            customer = item["customer"]
            service_counts[customer] = service_counts.get(customer, 0) + 1
        
        if service_counts:
            cols = st.columns(len(prices))
            for i, (service, price) in enumerate(prices.items()):
                with cols[i % len(cols)]:
                    st.metric(service, f"${price:.2f}")
        
        # Recent activity
        st.subheader("Recent Tickets")
        recent = df.tail(5).copy()
        recent["price"] = recent["price"].apply(lambda x: f"${x:.2f}")
        st.dataframe(recent, use_container_width=True, hide_index=True)
        
        # Download history
        st.divider()
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download History as CSV",
            data=csv,
            file_name=f"repair_history_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            use_container_width=True
        )

st.sidebar.divider()
st.sidebar.markdown("Built with ❤️ using Streamlit")
