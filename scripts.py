import os

def get_names_photos (): 

    names_photos = []
    
    for address, dirs, files in os.walk('images'):
    
        for name in files:
        
            path_photo = os.path.join(address, name)
            
            if is_photo_small(path_photo):
            
                names_photos.append(name)
    
    return names_photos
    
   
def is_photo_small(path_photo):

    stats = os.stat(path_photo)
              
    if stats.st_size < 20000000:
            
        return True
        
    else:

        print('The photo is too big')
        
        return False


def send_to_telegram(photo_path, chat_id, bot):

    with open(photo_path, 'rb') as photo:

        bot.send_photo(chat_id, photo)  
    