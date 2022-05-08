import re 
import requests
import json 
import tkinter as tk
from tkinter import*


api_key = 'YOUR_API_KEY'
def get_address(get_address,place,item):
  """ accessing three of google's apis to get customers pickup location and item around address within a 9500m (6miles) radius. 
  
  Args: 
    get_address(str): customers address
    place(str): customers entry of category of place. (For example, restaurant, hardware, )
    item(str):
    
  Side effect:
    price(int): prints price of delivery service 
    get_dist(str): prints distance from location to address
    get_time(int): prints time from location to address
    
   
  """
  try:
    separate = re.findall(r'(\d+\s.*)\s(\w+)\s([A-Z]{2})',get_address)
    
    street_info = list(separate[0][0].split(' '))
    house_number = street_info[0]
    street_name = street_info[1]
    street_suffix = street_info[2]
    city_name = separate[0][1]
    state_name = separate[0][2]
    
    #geocode api to get lnt and lng of customers address
    url_get_att = 'https://maps.googleapis.com/maps/api/geocode/json?address='+house_number+street_name+street_suffix+','+city_name+','+state_name+'&key='+api_key
    
    #------------------------------------------------------------------------
    
    response = requests.get(url_get_att)
    data = json.loads(response.text)
    address_place_id = data['results'][0]['place_id']

    get_cords = data['results'][0]['geometry']['location']
    get_lat = get_cords['lat']
    get_lng = get_cords['lng']
    
    #-------------------------------------------------------------------------
    
    type_place = place
    type_of_food = item
    
    #once tupe of place and what item the customer is looking for, take the information and use google's place ID api to get the stores 
    
    get_restaurants = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+str(get_lat)+','+str(get_lng)+'&radius=9500&type='+type_place+'&keyword='+type_of_food+'&key='+api_key
    
    response_two = requests.get(get_restaurants)
    data_two = json.loads(response_two.text)

    names = []
    place_ids = []
    for i in data_two['results']:     
        
        names.append(i['name']) #get results of places into a list
        
    for x in data_two['results']:
        place_ids.append(x['place_id'])   #get each locations place_id 
    
    
    #tkinter pop up list 
    root=Tk()
    sizex = 600
    sizey = 400
    posx  = 40
    posy  = 20
    root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
    

    def CurSelet(evt):
        """ Tkinter pop up page of list.
        
    
            Args: 
            evt : bind mylistbox 
            Side effect:
            Displays a tkinter page with all of the places in list , allowing user to select a place
        
        """
        
        
        value=str((mylistbox.get(mylistbox.curselection())))

        new_dict = dict(zip(names, place_ids))

        
        for x,y in new_dict.items():
            if value == x:
                
                #each address has their unique place ID 
                #by using the customers ID and place ID, I can find the distance and time 
                url_time_and_distance = 'https://maps.googleapis.com/maps/api/directions/json?origin=place_id:'+y+'&destination=place_id:'+address_place_id+'&key='+api_key
                response_three = requests.get(url_time_and_distance)
                data_three = json.loads(response_three.text)
                    
                get_dist = data_three['routes'][0]['legs'][0]['distance']['text']
                get_time = data_three['routes'][0]['legs'][0]['duration']['text']
                
                remove_mi = re.findall(r'\d*[.,]?\d*',get_dist)
                get_mi = remove_mi[0]
                pass_str = float(get_mi)
                
                fuelCharge = pass_str * 0.8
                price = 4.5 + fuelCharge
        
                print('Price: ',price)
                print(get_dist)
                print(get_time)

    mylistbox=Listbox(root,width=60,height=10,font=('times',13))
    mylistbox.bind('<<ListboxSelect>>',CurSelet)
    mylistbox.place(x=32,y=90)

    for items in names:
        mylistbox.insert(END,items)
    root.mainloop()
  except:
    print("Invalid entry. Please enter a proper address with this format:101 Halpine Road Rockville MD\n For place and item: enter one word (restaurant , hardware etc) for item enter: japanese,american, indian, etc  for restuarant. hammer, drywall, plumbing, etc for hardware.")  
  



if __name__ == "__main__":
  get_address(get_address,get_address,get_address)

  
  