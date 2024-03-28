from flask import Flask, request

app = Flask(__name__)

# Dictionary of SACCOs per city
saccos_by_city = {
    "1": ["Nairobi City SACCO", "SACCO ya Jiji la Nairobi",
          "SACCO la Nairobi City", "Nairobi City Savings and Credit Co-operative Society"],
    "2": ["Mombasa SACCO", "SACCO ya Mombasa", "SACCO la Mombasa", "Mombasa Savings and Credit Co-operative Society"],
    "3": ["Kisumu SACCO", "SACCO ya Kisumu", "SACCO la Kisumu", "Kisumu Savings and Credit Co-operative Society"],
    "4": ["Nakuru SACCO", "SACCO ya Nakuru", "SACCO la Nakuru", "Nakuru Savings and Credit Co-operative Society"],
    "5": ["Eldoret SACCO", "SACCO ya Eldoret", "SACCO la Eldoret", "Eldoret Savings and Credit Co-operative Society"]
}

# Function to display SACCOs based on user input
def display_saccos(location):
    if location in saccos_by_city:
        saccos = saccos_by_city[location]
        response = f"SACCOs in {saccos[0].split()[0]}:\n"  # Extract the city name from the first SACCO name
        for sacco in saccos:
            response += sacco + "\n"
    else:
        response = "Location not found in database."
    return response

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default").strip()

    response = ""
    if text == '':
        response = "CON Choose your loan type:\n1. Short-term loans\n2. Long-term loans\n3. Saving and dividends"
    elif text.lower() == '1':
        
        # Handle short-term loan selection
        response = "CON Choose your city:\n1. Nairobi\n2. Mombasa\n3. Kisumu\n4. Nakuru\n5. Eldoret"
    elif text.lower() == '2':
        # Handle long-term loan selection
        response = "CON Choose your city:\n1. Nairobi\n2. Mombasa\n3. Kisumu\n4. Nakuru\n5. Eldoret"
    elif text.lower() == '3':
        # Handle saving and dividends selection
        response = "CON Choose your city:\n1. Nairobi\n2. Mombasa\n3. Kisumu\n4. Nakuru\n5. Eldoret"
    elif text == '1*1':
        
        response = "CON These are sacco offering loan in your location :\n1. Nairobi City SACCO\n2. SACCO ya Jiji la Nairobi\n3. SACCO la Nairobi City\n4. Nairobi City Savings and Credit Co-operative Society\n5. STIMA SACCO" 
    elif text == '1*1*1':
        
        response = "CON Nairobi City SACCO\n Dial *234# to know more about Nairobi city Sacco, or visit thier website www.ncsacco.com"
    elif text == '1*1*2':
        
        response = "CON SACCO ya Jiji la Nairobi\n Dial *234# to know more about Nairobi city Sacco, or visit thier website www.ncsacco.com"  
    elif text == '1*1*3':
        
        response = "CON SACCO la Nairobi City\n Dial *234# to know more about Nairobi city Sacco, or visit thier website www.ncsacco.com" 
    elif text == '1*1*4':
        
        response = "CON Nairobi City Savings and Credit Co-operative Society\n Dial *234# to know more about Nairobi city Sacco, or visit thier website www.ncsacco.com"
    elif text == '1*1*5':
        
        response = "CON STIMA SACCO\n Dial *234# to know more about Nairobi city Sacco, or visit thier website www.ncsacco.com" 
        
        # 2
    elif text == '1*2':
        
        response = "CON These are sacco offering loan in your location :\n1. Mombasa SACCO\n2. SACCO ya Jiji la Mombasa\n3. SACCO la Mombasa\n4. Mombasa Savings and Credit Co-operative Society\n5. STIMA SACCO" 
    elif text == '1*2*1':
        
        response = "CON Mombasa SACCO\n Dial *234# to know more about Mombasa city Sacco, or visit thier website www.mcsacco.com"
    elif text == '1*2*2':
        
        response = "CON SACCO ya Jiji la Mombasa\n Dial *234# to know more about Mombasa city Sacco, or visit thier website www.mcsacco.com"  
    elif text == '1*2*3':
        
        response = "CON SACCO la Mombasa\n Dial *234# to know more about Mombasa city Sacco, or visit thier website www.mcsacco.com" 
    elif text == '1*2*4':
        
        response = "CON Mombasa Savings and Credit Co-operative Society\n Dial *234# to know more about Mombasa city Sacco, or visit thier website www.mcsacco.com"
    elif text == '1*2*5':
        
        response = "CON STIMA SACCO\n Dial *234# to know more about Mombasa city Sacco, or visit thier website www.mcsacco.com" 
        
    # 3
    elif text == '1*3':
        
        response = "CON These are sacco offering loan in your location :\n1. Kisumu SACCO\n2. SACCO ya Jiji la Kisumu\n3. SACCO la Kisumu\n4. Kisumu Savings and Credit Co-operative Society\n5. STIMA SACCO" 
    elif text == '1*3*1':
        
        response = "CON Kisumu SACCO\n Dial *234# to know more about Kisumu city Sacco, or visit thier website www.kisacusacco.com"
    elif text == '1*3*2':
        
        response = "CON SACCO ya Jiji la Kisumu\n Dial *234# to know more about Kisumu city Sacco, or visit thier website www.kisacusacco.com"  
    elif text == '1*3*3':
        
        response = "CON SACCO la Kisumu\n Dial *234# to know more about Kisumu city Sacco, or visit thier website www.kisacusacco.com" 
    elif text == '1*3*4':
        
        response = "CON Kisumu Savings and Credit Co-operative Society\n Dial *234# to know more about Kisumu city Sacco, or visit thier website www.kisacusacco.com"
    elif text == '1*3*5':
        
        response = "CON STIMA SACCO\n Dial *234# to know more about Kisumu city Sacco, or visit thier website www.kisacusacco.com" 
        
      # 4
    elif text == '1*4':
        
        response = "CON These are sacco offering loan in your location :\n1. Nakuru SACCO\n2. SACCO ya Jiji la Nakuru\n3. SACCO la Nakuru\n4. Nakuru Savings and Credit Co-operative Society\n5. STIMA SACCO" 
    elif text == '1*4*1':
        
        response = "CON Nakuru SACCO\n Dial *234# to know more about Nakuru city Sacco, or visit thier website www.nakurusacco.com"
    elif text == '1*4*2':
        
        response = "CON SACCO ya Jiji la Nakuru\n Dial *234# to know more about Nakuru city Sacco, or visit thier website www.nakurusacco.com"  
    elif text == '1*4*3':
        
        response = "CON SACCO la Nakuru\n Dial *234# to know more about Nakuru city Sacco, or visit thier website www.nakurusacco.com" 
    elif text == '1*4*4':
        
        response = "CON Nakuru Savings and Credit Co-operative Society\n Dial *234# to know more about Nakuru city Sacco, or visit thier website www.nakurusacco.com"
    elif text == '1*4*5':
        
        response = "CON STIMA SACCO\n Dial *234# to know more about Nakuru city Sacco, or visit thier website www.nakurusacco.com"
        # 5
    elif text == '1*5':
        
        response = "CON These are sacco offering loan in your location :\n1. Eldoret SACCO\n2. SACCO ya Jiji la Eldoret\n3. SACCO la Eldoret\n4. Eldoret Savings and Credit Co-operative Society\n5. STIMA SACCO" 
    elif text == '1*5*1':
        
        response = "CON Eldoret SACCO\n Dial *234# to know more about Eldoret city Sacco, or visit thier website www.eldoretsacco.com"
    elif text == '1*5*2':
        
        response = "CON SACCO ya Jiji la Eldoret\n Dial *234# to know more about Eldoret city Sacco, or visit thier website www.eldoretsacco.com"  
    elif text == '1*5*3':
        
        response = "CON SACCO la Eldoret\n Dial *234# to know more about Eldoret city Sacco, or visit thier website www.eldoretsacco.com" 
    elif text == '1*5*4':
        
        response = "CON Eldoret Savings and Credit Co-operative Society\n Dial *234# to know more about Eldoret city Sacco, or visit thier website www.eldoretsacco.com"
    elif text == '1*5*5':
        
        response = "CON STIMA SACCO\n Dial *234# to know more about Eldoret city Sacco, or visit thier website www.eldoretsacco.com" 
    elif text == '2*1':
        
        response = "CON These are sacco offering loan in your Mombasa :\n1. Nairobi City SACCO\n2. SACCO ya Jiji la Mambasa\n3. SACCO la Mambasa City\n4. Mombasa City Savings and Credit Co-operative Society\n5. STIMA SACCO" 
    elif text == '2*1*1':
        
        response = "E Nairobi City SACCO\n Dial *234# to know more about Mombasa city Sacco, or visit thier website www.mombasasacco.com"
    elif text == '2*1*2':
        
        response = "E SACCO ya Jiji la Mambasa\n Dial *234# to know more about Mombasa city Sacco, or visit thier website www.mombasasacco.com"  
    elif text == '2*1*3':
        
        response = "E SACCO la Mambasa City\n Dial *234# to know more about Mombasa city Sacco, or visit thier website www.mombasasacco.com" 
    elif text == '2*1*4':
        
        response = "E Mombasa City Savings and Credit Co-operative Society\n Dial *234# to know more about Mombasa city Sacco, or visit thier website www.mombasasacco.com"
    elif text == '2*1*5':
        
        response = "E STIMA SACCO\n Dial *234# to know more about Mombasa city Sacco, or visit thier website www.mombasasacco.com" 
    else:
        response = "END Invalid input. Choose your loan type:\n1. Short-term loans\n2. Long-term loans\n3. Saving and dividends"

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True, use_reloader=True)
