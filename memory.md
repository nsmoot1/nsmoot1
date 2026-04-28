# Memory: Repair Manager Streamlit Project

## Project Summary
Built a complete Streamlit web application for the Repair Manager system. Converted a CLI-based ticket management system into an interactive multi-page web app with ticket creation, history viewing, status updates, and analytics.

## Tech Stack
- **Python 3.13**
- **Streamlit 1.56.0** (already installed in environment)
- **Pandas** (for data analysis and charts)
- **File-based storage**: CSV format in repair_history.txt

## Key Files Structure
```
nsmoot1/
├── repair_app_streamlit.py     # Main web app (265 lines)
├── repair_ticket.py            # RepairTicket class (not currently used by Streamlit version)
├── repair_manager.py           # Original CLI version
├── repair_prices.txt           # Service catalog (CSV: service_name,price)
├── repair_history.txt          # Ticket log (auto-generated, CSV format)
├── repair_report.txt           # Latest receipt (auto-generated)
├── requirements.txt            # Dependencies
├── STREAMLIT_README.md         # Full documentation
└── QUICKSTART.md               # Launch instructions
```

## Critical Implementation Details

### Data Format (repair_history.txt)
```
Name,Email,Device,Service,Price,Status,Timestamp
Nick Smoot,nsmoot@email.com,Laptop,Diagnostics,40.00,Received,2026-04-27 18:41:35
```

### Key Functions Architecture
- `load_history()` - Reads all lines from file
- `parse_history_line()` - Converts CSV line to dict (with error handling)
- `load_tickets_with_indices()` - **IMPORTANT**: Tracks line number for each ticket to prevent index mismatches
- `update_ticket_status()` - Modifies a specific line in the history file
- `save_ticket()` - Appends new ticket to history

### Important Implementation Patterns
1. **Index Tracking**: Each ticket dict includes `_line_index` (the position in the file) for accurate updates
2. **Error Resilience**: `parse_history_line()` uses try-catch to skip malformed lines
3. **Display Filtering**: Internal `_line_index` field is removed before displaying to users
4. **Streamlit Reruns**: `st.rerun()` used after status updates to refresh the UI

## App Features
1. **📋 New Ticket** - Create repair tickets with customer info and service selection
2. **📂 View Tickets** - Browse all tickets, update status from dropdown
3. **📊 Analytics** - Dashboard showing metrics (total revenue, completion rate, charts by device/status/service)

## Status Enum
Valid ticket statuses:
- Received (default)
- In Progress
- Completed
- Ready for Pickup
- Cancelled

## Launch Command
```bash
streamlit run repair_app_streamlit.py
```
App runs on `http://localhost:8501`

## GitHub Repository
- URL: https://github.com/nsmoot1/nsmoot1
- Branch: main
- Remote configured and working
- Git config: email=nsmoot@students.mchenry.edu, name=Nick Smoot

## Known Limitations & Future Improvements
1. **No Database** - Currently uses plain text files (not scalable)
2. **No User Authentication** - Anyone with access can modify any ticket
3. **No Ticket Search/Filtering** - Can only view all tickets
4. **No Email Notifications** - Status changes don't notify customers
5. **CSV Format Brittle** - If a customer name contains commas, parsing breaks
6. **No Undo** - Updates are immediate and permanent

### Recommended Next Steps
- Migrate to SQLite database
- Add customer email notifications
- Implement user roles/permissions
- Add proper logging
- Create automated tests
- Add data validation (email format, price > 0, etc.)

## Development Notes for Next Session

### If You Need to Debug Ticket Updates
1. Check that repair_history.txt exists and has correct format
2. Verify `load_tickets_with_indices()` is returning tickets with `_line_index` field
3. The update function reads entire file, modifies one line, writes back entire file
4. Watch for CSV parsing errors with special characters

### If You Want to Add Features
- Analytics are already charting-ready via Streamlit's st.bar_chart()
- Adding new statuses: just add to the `statuses` list on line 174
- Adding new services: edit repair_prices.txt, format: `ServiceName,Price`
- Adding new pages: duplicate page logic and add to sidebar radio

### Common Issues & Solutions
1. **"Port 8501 already in use"** → `streamlit run repair_app_streamlit.py --server.port 8502`
2. **Prices not loading** → Check repair_prices.txt exists and has no extra spaces
3. **Update fails silently** → Check console for error, ensure CSV format is correct
4. **Merge conflicts on next push** → Use `git checkout --ours .` to keep local version

## Session Artifacts
- reflection.md - This reflection document
- memory.md - This file

## What Worked Well to Repeat
✅ Asking clarifying questions early about feature scope
✅ Providing full error tracebacks (makes debugging 10x faster)
✅ Testing incrementally and reporting issues immediately
✅ Clear file naming and organization

## What to Avoid Next Time
❌ Don't edit multi-line code blocks without being careful with function definitions
❌ Don't assume CSV format without validation
❌ Don't push to GitHub without testing locally first
❌ Don't skip the test phase after "fixing" an error
