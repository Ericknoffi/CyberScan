from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import time

from scanner.basic_info import scan_basic_info
from scanner.port_scan import run_port_scan
from scanner.sqlmap_scan import run_sqlmap

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

@app.route('/api/scan', methods=['POST'])
def run_scan():
    try:
        data = request.get_json()
        url = data.get('url')
        scans = data.get('scans', [])

        if not url:
            return jsonify({'error': 'URL is required'}), 400

        # Extract domain from URL
        domain = url.split("//")[-1].split("/")[0]

        results = {}

        # Run each scan and capture results
        for scan_type in scans:
            try:
                if scan_type == 'basic' or scan_type == 'nmap':
                    results['basic_info'] = scan_basic_info(url)
                elif scan_type == 'port':
                    results['port_scan'] = run_port_scan(domain)
                elif scan_type == 'sqlmap':
                    results['sqlmap'] = run_sqlmap(url)
            except Exception as e:
                results[scan_type] = f"Error running {scan_type}: {str(e)}"

        # Save results to output folder
        timestamp = int(time.time())
        output_file = f"c:\\Ashok\\Coding\\Project\\CyberScan (done)\\output\\scan_results_{timestamp}.json"

        scan_data = {
            'url': url,
            'timestamp': timestamp,
            'results': results
        }

        with open(output_file, 'w') as f:
            json.dump(scan_data, f, indent=2)

        return jsonify({
            'success': True,
            'url': url,
            'results': results,
            'output_file': output_file,
            'timestamp': timestamp
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'message': 'Scanner API is running'})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import time

from scanner.basic_info import scan_basic_info
from scanner.port_scan import run_port_scan
from scanner.sqlmap_scan import run_sqlmap

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

@app.route('/api/scan', methods=['POST'])
def run_scan():
    try:
        data = request.get_json()
        url = data.get('url')
        scans = data.get('scans', [])

        if not url:
            return jsonify({'error': 'URL is required'}), 400

        # Extract domain from URL
        domain = url.split("//")[-1].split("/")[0]

        results = {}

        # Run each scan and capture results
        for scan_type in scans:
            try:
                if scan_type == 'basic' or scan_type == 'nmap':
                    results['basic_info'] = scan_basic_info(url)
                elif scan_type == 'port':
                    results['port_scan'] = run_port_scan(domain)
                elif scan_type == 'sqlmap':
                    results['sqlmap'] = run_sqlmap(url)
            except Exception as e:
                results[scan_type] = f"Error running {scan_type}: {str(e)}"

        # Save results to output folder
        timestamp = int(time.time())
        output_file = f"c:\\Ashok\\Coding\\Project\\CyberScan (done)\\output\\scan_results_{timestamp}.json"

        scan_data = {
            'url': url,
            'timestamp': timestamp,
            'results': results
        }

        with open(output_file, 'w') as f:
            json.dump(scan_data, f, indent=2)

        return jsonify({
            'success': True,
            'url': url,
            'results': results,
            'output_file': output_file,
            'timestamp': timestamp
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500
