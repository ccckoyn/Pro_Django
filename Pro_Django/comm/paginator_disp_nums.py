#coding=utf-8

def get_pages(totalpage=1, current_page=1):

    """页码个数由WEB_DISPLAY_PAGE设定"""
    WEB_DISPLAY_PAGE = 5
    front_offset = int(WEB_DISPLAY_PAGE / 2)
    if WEB_DISPLAY_PAGE % 2 == 1:
        behind_offset = front_offset
    else:
        behind_offset = front_offset - 1
    if totalpage < WEB_DISPLAY_PAGE:
        return list(range(1,totalpage+1))
    elif current_page <= front_offset:
        return list(range(1,WEB_DISPLAY_PAGE+1))
    elif current_page >= totalpage-behind_offset:
        start_page = totalpage-WEB_DISPLAY_PAGE+1
        return list(range(start_page, totalpage+1))
    else:
        start_page = current_page - front_offset
        end_page = current_page + behind_offset
        return list(range(start_page, end_page+1))

if __name__ == "__main__":
    res = get_pages(10,10)
    print(res)