# youtube_api/parser.py

from tools import nested_dict_to_dict, cherrypick_dict

def youtube_comment_data_parser(instance, add_data = dict()):
    """
    Parses youtube comment thread into a list of dictionaries only with
    permitted keys.
    
    If the comment has replies, it will include replies while comment without
    will only return a list with one data.
    """
    
    
    comments = instance.return_data.get('items')
    
    return_list = list()
    for comment in comments:

        unwrapped_dict = nested_dict_to_dict(comment)
        return_list.append(cherrypick_dict(unwrapped_dict, instance.header))

        if int(unwrapped_dict.get('totalReplyCount', 0)) > 0:
            for reply_comment_thread in unwrapped_dict.get('comments', list()):
                return_list.append(
                            cherrypick_dict(
                                nested_dict_to_dict(reply_comment_thread), 
                                instance.header
                            )
                )
                
    return return_list