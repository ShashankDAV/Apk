from fb import *

# sample = [[runs , innings , not outs , hs , avg , 50s , 100s , 150s] , [wickets , 3ws] , [in_played , in_won , in_lost , win%]]

data_r = {'data': [("Nayan" , 110) , ("Shashank" , 170) , ("Anushka" , 30) , ("Ayansh" , 45) , ("Harsh" , 70)]}

data_s = {'stats': [[81, 7, 1, '  25', 0, 0, 0], [7, 0], [1, 0, 1]]}

db = Firebase('https://website-shashankdav-default-rtdb.firebaseio.com/' , '')

db.post_data(data = data_r , path = "rankings/bowl")

#print(db.get_data(path = "harsh"))