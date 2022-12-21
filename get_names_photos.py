import os

def get_names_photos (): 

    names_photos = []
    
    
              
 
    
    for address, dirs, files in os.walk('images'):
    
        
        
        for name in files:
        
            path_photo = os.path.join(address, name)
            
            stats = os.stat(path_photo)
              
            if stats.st_size > 20000000:
            
                print('The photo is too big')
    
                continue
            
            names_photos.append(name)
    
    return names_photos