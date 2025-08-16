# CyberScan Dashboard

Modern web-based security scanner for automated vulnerability assessment.

## Features
- Basic Info Scan: HTTP headers, security headers, cookies
- Port Scan: Nmap integration
- SQL Injection Test: SQLMap integration
- Clean, privacy-safe web UI
- Results saved automatically

## Project Structure
```
scanner/           # Python scanning modules
output/            # Scan results storage
scanner_ui.html    # Web interface
app.py             # Flask backend
requirements.txt   # Python dependencies
start_dashboard.bat# Windows startup script
```

## Prerequisites
- Python 3.8+
- Nmap ([download](https://nmap.org/download.html))
- SQLMap (install separately if not on Kali Linux)

## Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
1. Start backend: `python app.py`
2. Open `scanner_ui.html` in your browser
3. Enter a target and run scans

## Security Notes
- No scan results or sensitive data are logged to the browser console
- All unnecessary code and banners have been removed for a clean experience

## Usage 📖

1. Enter a target URL (e.g., `https://example.com`)
2. Click "Initiate Full Scan"
3. View real-time results in the dashboard
4. Results are automatically saved to the `output/` folder

## API Endpoints 🔌

- `POST /api/scan` - Run security scans
- `GET /api/health` - Health check

## Security Note ⚠️

This tool is intended for **educational purposes** and **authorized testing only**. Always ensure you have proper authorization before scanning any target systems.

## Dependencies & Licenses 📜

- **Flask** - Web framework
- **React** - Frontend framework
- **Nmap** - Network scanning (requires separate installation)
- **SQLMap** - SQL injection testing (requires separate installation)
- **Tailwind CSS** - UI styling

## Troubleshooting 🔍

### Common Issues:

1. **"Nmap not found"** - Install Nmap and add to PATH
2. **"SQLMap not found"** - Install SQLMap and add to PATH
3. **CORS errors** - Ensure Flask backend is running on port 5000
4. **Port already in use** - Check if other services are using ports 3000 or 5000

### Installation Help:

- **Windows Nmap**: Download from nmap.org and add to system PATH
- **Windows SQLMap**: Download and extract, add to system PATH
- **Node.js**: Download from nodejs.org

## Contributing 🤝

Feel free to fork this project and submit pull requests for improvements!

## License 📄

This project is for educational purposes. Please use responsibly and only on systems you own or have explicit permission to test.
