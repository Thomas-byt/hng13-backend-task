#---1. import libraries 
from flask import Flask, jsonify
import requests # used to fetch data from external API
from datetime import datetime

#--- 2. Set up digital app
app = Flask(__name__)

#--- 3. Create frontend route
@app.route('/cat', methods=['GET'])
def my_profile():
    try:
        # Fetch data from external API
        cat_response = requests.get('https://catfact.ninja/fact', timeout=5)
        cat_response.raise_for_status()  # Raise an error for bad responses
        cat_fact = cat_response.json().get('fact', 'No fact found') # Extract cat fact
    except requests.RequestException as e:
        cat_fact = f"Error fetching cat fact: {e}"

    # --- 4. Prepare profile data
    profile_data = {
        "status": "success",
        "user":{
            "email": "Thomasdreh@gmail.com",
            "name": "Dare Thomas Osakinle",
            "stack": "Python/Flask"},
            "timestamp": datetime.utcnow().isoformat() + 'Z',  # Current timestamp in ISO format
            "fact": cat_fact

    }

    # ----5. Send the report back to the client ----
    return jsonify(profile_data), 200 # 200 OK status code
#--- 6. Run the app
if __name__ == '__main__':
   port = int(os.environ.get("PORT", 8000))
   app.run(host="0.0.0.0", port=port)
    ##app.run(debug=True) # Run the app in debug mode for development
    
