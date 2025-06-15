from flask import Flask, request, render_template
import requests
import re
import time
import os

class FacebookMessengerGroupExtractor:
    def __init__(self, access_token: str):
        """
        Initialize the extractor with Facebook access token
        
        Args:
            access_token (str): Facebook Graph API access token
        """
        self.access_token = access_token
        self.base_url = "https://graph.facebook.com/v18.0"
    
    def get_user_conversations(self) -> Optional[Dict]:
        """
        Get all conversations for the authenticated user
        
        Returns:
            Dict: Response containing conversations data
        """
        url = f"{self.base_url}/me/conversations"
        params = {
            'access_token': self.access_token,
            'fields': 'id,name,participants,message_count,updated_time'
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching conversations: {e}")
            return None
    
    def get_group_conversations(self) -> List[Dict]:
        """
        Filter and return only group conversations (more than 2 participants)
        
        Returns:
            List[Dict]: List of group conversations
        """
        conversations = self.get_user_conversations()
        if not conversations or 'data' not in conversations:
            return []
        
        groups = []
        for conv in conversations['data']:
            # Check if it's a group (more than 2 participants)
            if 'participants' in conv and len(conv['participants']['data']) > 2:
                groups.append({
                    'uid': conv['id'],
                    'name': conv.get('name', 'Unnamed Group'),
                    'participant_count': len(conv['participants']['data']),
                    'message_count': conv.get('message_count', 0),
                    'updated_time': conv.get('updated_time', '')
                })
        
        return groups
    
    def get_group_by_name(self, group_name: str) -> Optional[Dict]:
        """
        Find a specific group by name
        
        Args:
            group_name (str): Name of the group to find
            
        Returns:
            Dict: Group information if found, None otherwise
        """
        groups = self.get_group_conversations()
        
        for group in groups:
            if group['name'].lower() == group_name.lower():
                return group
        
        return None
    
    def get_conversation_details(self, conversation_id: str) -> Optional[Dict]:
        """
        Get detailed information about a specific conversation
        
        Args:
            conversation_id (str): The conversation ID/UID
            
        Returns:
            Dict: Detailed conversation information
        """
        url = f"{self.base_url}/{conversation_id}"
        params = {
            'access_token': self.access_token,
            'fields': 'id,name,participants.limit(100){name,id},message_count,updated_time'
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching conversation details: {e}")
            return None
    
    def display_all_groups(self):
        """
        Display all group conversations with their UIDs
        """
        groups = self.get_group_conversations()
        
        if not groups:
            print("No group conversations found.")
            return
        
        print("Facebook Messenger Groups:")
        print("-" * 50)
        
        for i, group in enumerate(groups, 1):
            print(f"{i}. Group Name: {group['name']}")
            print(f"   UID: {group['uid']}")
            print(f"   Participants: {group['participant_count']}")
            print(f"   Messages: {group['message_count']}")
            print(f"   Last Updated: {group['updated_time']}")
            print("-" * 50)

# Usage example
def main():
    # Replace with your actual Facebook access token
    ACCESS_TOKEN = "YOUR_FACEBOOK_ACCESS_TOKEN_HERE"
    
    # Initialize the extractor
    extractor = FacebookMessengerGroupExtractor(ACCESS_TOKEN)
    
    # Method 1: Display all groups
    print("Method 1: All Groups")
    extractor.display_all_groups()
    
    # Method 2: Find specific group by name
    print("\nMethod 2: Find specific group")
    group_name = "My Group Chat"  # Replace with actual group name
    group = extractor.get_group_by_name(group_name)
    
    if group:
        print(f"Found group: {group['name']}")
        print(f"UID: {group['uid']}")
    else:
        print(f"Group '{group_name}' not found")
    
    # Method 3: Get detailed info for a specific conversation
    print("\nMethod 3: Detailed conversation info")
    conversation_id = "CONVERSATION_ID_HERE"  # Replace with actual conversation ID
    details = extractor.get_conversation_details(conversation_id)
    
    if details:
        print(f"Conversation ID: {details['id']}")
        print(f"Name: {details.get('name', 'No name')}")
        if 'participants' in details:
            print(f"Participants: {len(details['participants']['data'])}")

if __name__ == "__main__":
    main()
