"""
STREAMLIT WEB APP: Repair Manager V2.0
A web-based interface for managing repair tickets using Streamlit
Enhanced with mobile responsiveness, search, and ticket confirmation numbers
"""

import streamlit as st
import datetime
import pandas as pd
from repair_ticket import RepairTicket
import os
import uuid

# --- PAGE CONFIG ---
st.set_page_config(page_title="Repair Manager", layout="wide", initial_sidebar_state="auto")

# --- GLOBAL CONSTANTS ---
PRICES_FILE = "repair_prices.txt"
HISTORY_FILE = "repair_history.txt"
REPORT_FILE = "repair_report.txt"

# --- MOBILE RESPONSIVE CSS ---
st.markdown("""
<style>
    /* Mobile responsive design */
    @media (max-width: 640px) {
        .stColumns {
            gap: 0.5rem;
        }
        .stButton > button {
            width: 100%;
            font-size: 14px;
            padding: 0.5rem;
            min-height: 44px;
        }
        .stTextInput > div > div > input,
        .stSelectbox > div > div > select {
            font-size: 16px;
            min-height: 44px;
            padding: 0.5rem;
        }
        h1 {
            font-size: 24px;
        }
        h2 {
            font-size: 20px;
        }
    }
    
    /* Ticket ID styling */
    .ticket-id-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
    .ticket-id-label {
        font-size: 12px;
        color: #666;
        text-transform: uppercase;
        font-weight: bold;
    }
    .ticket-id-value {
        font-size: 24px;
        font-weight: bold;
        font-family: monospace;
        color: #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

# --- FUNCTIONS ---
def generate_ticket_id():
    """Generates a unique ticket ID"""
    date_str = datetime.datetime.now().strftime("%Y%m%d")
    unique_suffix = str(uuid.uuid4())[:5].upper()
    return f"REPAIR-{date_str}-{unique_suffix}"

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

def save_ticket(customer_info, price, service_name):
    """Saves a new ticket to repair_history.txt with unique ticket ID"""
    name, email, device = customer_info
    ticket_id = generate_ticket_id()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(HISTORY_FILE, "a") as file:
            file.write(f"{ticket_id},{name},{email},{device},{service_name},{price:.2f},Received,{timestamp}\n")
        
        with open(REPORT_FILE, "w") as file:
            file.write(f"[{timestamp}]\n")
            file.write(f"Ticket ID: {ticket_id}\n")
            file.write(f"Customer: {name}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Device: {device}\n")
            file.write(f"Service: {service_name}\n")
            file.write(f"Total: ${price:.2f}\n")
            file.write("-" * 50 + "\n")
        return ticket_id
    except Exception as e:
        st.error(f"Error saving ticket: {e}")
        return None

def parse_history_line(line):
    """Parses a history file line into components"""
    parts = [p.strip() for p in line.split(",")]
    if len(parts) >= 8:
        try:
            return {
                "Ticket ID": parts[0],
                "Name": parts[1],
                "Email": parts[2],
                "Device": parts[3],
                "Service": parts[4],
                "Price": float(parts[5]),
                "Status": parts[6],
                "Timestamp": parts[7]
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
        if len(parts) >= 8:
            parts[6] = new_status
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
    
    # Mobile-responsive layout
    col1, col2 = st.columns(1 if st.session_state.get('mobile_mode', False) else 2)
    
    with col1:
        st.subheader("Customer Information")
        customer_name = st.text_input("Customer Name", placeholder="John Doe")
        customer_email = st.text_input("Customer Email", placeholder="john@example.com")
    
    try:
        with col2:
            st.subheader("Device Information")
            device_type = st.text_input("Device Type", placeholder="Laptop, Desktop, etc.")
    except:
        st.subheader("Device Information")
        device_type = st.text_input("Device Type", placeholder="Laptop, Desktop, etc.")
        
    # Load available services
    prices = load_prices()
    if prices:
        st.subheader("Select Service")
        service = st.selectbox("Service Type", list(prices.keys()))
        price = prices[service]
        
        st.metric("Service Price", f"${price:.2f}")
        
        # Create button
        if st.button("✅ Create Ticket", use_container_width=True, type="primary"):
            if customer_name and customer_email and device_type:
                ticket_id = save_ticket((customer_name, customer_email, device_type), price, service)
                if ticket_id:
                    st.success(f"✓ Ticket created successfully!")
                    st.balloons()
                    
                    # Display receipt with Ticket ID prominently
                    st.markdown("---")
                    st.subheader("🎫 Receipt & Confirmation")
                    
                    # Prominent Ticket ID
                    st.markdown(f"""
                    <div class="ticket-id-box">
                        <div class="ticket-id-label">Your Ticket Number:</div>
                        <div class="ticket-id-value">{ticket_id}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.info(f"📌 **Please save this ticket number for your records!**")
                    
                    # Receipt details
                    receipt_cols = st.columns(1 if st.session_state.get('mobile_mode', False) else 2)
                    with receipt_cols[0]:
                        st.write(f"**Customer:** {customer_name}")
                        st.write(f"**Email:** {customer_email}")
                    try:
                        with receipt_cols[1]:
                            st.write(f"**Device:** {device_type}")
                            st.write(f"**Service:** {service}")
                    except:
                        st.write(f"**Device:** {device_type}")
                        st.write(f"**Service:** {service}")
                    
                    st.write(f"**Total:** ${price:.2f}")
                    st.write(f"**Timestamp:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    st.write(f"**Status:** Received")
            else:
                st.error("Please fill in all fields.")
    else:
        st.error("No services available. Please check repair_prices.txt")

# --- PAGE: VIEW TICKETS ---
elif page == "📂 View Tickets":
    st.header("Repair Ticket History")
    
    tickets = load_tickets_with_indices()
    
    if tickets:
        # QUICK SEARCH FEATURE - FIX #2
        st.subheader("🔍 Quick Search")
        search_col1, search_col2 = st.columns([3, 1])
        
        with search_col1:
            search_term = st.text_input(
                "Search by:",
                placeholder="Customer name, email, device, or ticket ID",
                help="Type to filter tickets in real-time"
            )
        
        with search_col2:
            search_status = st.selectbox(
                "Filter by Status:",
                ["All"] + ["Received", "In Progress", "Completed", "Ready for Pickup", "Cancelled"]
            )
        
        # Filter tickets based on search and status
        filtered_tickets = tickets.copy()
        
        if search_term:
            search_lower = search_term.lower()
            filtered_tickets = [
                t for t in filtered_tickets
                if (search_lower in t.get('Name', '').lower() or
                    search_lower in t.get('Email', '').lower() or
                    search_lower in t.get('Device', '').lower() or
                    search_lower in t.get('Ticket ID', '').lower())
            ]
        
        if search_status != "All":
            filtered_tickets = [t for t in filtered_tickets if t['Status'] == search_status]
        
        # Display search results
        st.markdown(f"**Found {len(filtered_tickets)} ticket(s)**")
        
        if filtered_tickets:
            # Display as table (remove internal _line_index for display)
            display_tickets = [{k: v for k, v in t.items() if k != '_line_index'} for t in filtered_tickets]
            df = pd.DataFrame(display_tickets)
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            # Update Ticket Status
            st.markdown("---")
            st.subheader("🔄 Update Ticket Status")
            statuses = ["Received", "In Progress", "Completed", "Ready for Pickup", "Cancelled"]
            
            ticket_labels = [f"{t['Ticket ID']} - {t['Name']} - {t['Device']}" for t in filtered_tickets]
            selected_ticket_label = st.selectbox("Select Ticket to Update", ticket_labels)
            selected_idx = ticket_labels.index(selected_ticket_label)
            
            if selected_idx is not None and selected_idx >= 0:
                current_ticket = filtered_tickets[selected_idx]
                
                # Show current ticket details
                with st.expander("📋 View Full Details"):
                    st.write(f"**Ticket ID:** {current_ticket['Ticket ID']}")
                    st.write(f"**Customer:** {current_ticket['Name']}")
                    st.write(f"**Email:** {current_ticket['Email']}")
                    st.write(f"**Device:** {current_ticket['Device']}")
                    st.write(f"**Service:** {current_ticket['Service']}")
                    st.write(f"**Price:** ${current_ticket['Price']:.2f}")
                    st.write(f"**Current Status:** {current_ticket['Status']}")
                    st.write(f"**Created:** {current_ticket['Timestamp']}")
                
                col1, col2 = st.columns([2, 1])
                with col1:
                    new_status = st.selectbox(
                        "New Status",
                        statuses,
                        index=statuses.index(current_ticket["Status"])
                    )
                with col2:
                    if st.button("🔄 Update", use_container_width=True, type="primary"):
                        line_index = current_ticket['_line_index']
                        if update_ticket_status(line_index, new_status):
                            st.success(f"✓ Ticket status updated to '{new_status}'")
                            st.rerun()
                        else:
                            st.error("Failed to update ticket status")
        else:
            st.warning("No tickets found matching your search criteria.")
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
        
        # Key metrics (mobile-responsive)
        metrics_cols = st.columns(2 if st.session_state.get('mobile_mode', False) else 4)
        
        with metrics_cols[0]:
            st.metric("Total Tickets", len(df))
        
        with metrics_cols[1]:
            total_revenue = df["Price"].sum()
            st.metric("Total Revenue", f"${total_revenue:.2f}")
        
        if not st.session_state.get('mobile_mode', False):
            with metrics_cols[2]:
                avg_price = df["Price"].mean()
                st.metric("Average Repair Cost", f"${avg_price:.2f}")
            
            with metrics_cols[3]:
                completed = len(df[df["Status"].isin(["Completed", "Ready for Pickup"])])
                st.metric("Completed", completed)
        else:
            with st.columns(2)[0]:
                avg_price = df["Price"].mean()
                st.metric("Average Repair Cost", f"${avg_price:.2f}")
            
            with st.columns(2)[1]:
                completed = len(df[df["Status"].isin(["Completed", "Ready for Pickup"])])
                st.metric("Completed", completed)
        
        # Charts (mobile-responsive)
        st.markdown("---")
        
        chart_cols = st.columns(1 if st.session_state.get('mobile_mode', False) else 2)
        
        with chart_cols[0]:
            st.subheader("Tickets by Status")
            status_counts = df["Status"].value_counts()
            st.bar_chart(status_counts)
        
        if not st.session_state.get('mobile_mode', False):
            with chart_cols[1]:
                st.subheader("Tickets by Device Type")
                device_counts = df["Device"].value_counts()
                st.bar_chart(device_counts)
        else:
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
st.markdown("""
🔧 **Repair Manager v2.0** | Built with Streamlit
- ✅ Mobile-responsive design for all devices
- ✅ Quick search and filter functionality  
- ✅ Unique ticket IDs for customer reference
""")
