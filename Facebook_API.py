import facebook

def main():
    cfg = {
        'page_id': '<page id here>',
        'access_token': '<access token here>'
    }
    api = get_api(cfg)
    post_picture = api.put_photo(image=open('tree.png', 'rb'), message='Xmas tree from python')
    # msg = 'test1234 - autoreply 11:59'
    # status = api.put_wall_post(msg)


def get_api(cfg):
    graph = facebook.GraphAPI(
        access_token=cfg['access_token'])
    return graph
    
if __name__ == '__main__':
    main()
