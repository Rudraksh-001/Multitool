import requests

def get_messenger_group_uid(access_token, group_id):
    """
    Extract member UIDs from a Facebook Messenger group
    
    Args:
        access_token (str): Your Facebook Graph API access token
        group_id (str): The ID of the Messenger group
    
    Returns:
        list: List of member UIDs in the group
    """
    try:
        # Facebook Graph API endpoint for group participants
        url = f"https://graph.facebook.com/v19.0/{group_id}/participants"
        
        params = {
            'access_token': access_token,
            'fields': 'id,name'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        if 'data' in data:
            uids = [user['id'] for user in data['data']]
            return uids
        else:
            return []
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching group data: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Replace these with your actual values
    ACCESS_TOKEN = "your_facebook_access_token"
    GROUP_ID = "your_group_id"
    
    member_uids = get_messenger_group_uid(ACCESS_TOKEN, GROUP_ID)
    
    if member_uids:
        print("Member UIDs:")
        for uid in member_uids:
            print(uid)
    else:
        print("No UIDs found or there was an error.")
