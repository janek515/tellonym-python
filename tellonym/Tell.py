import json

class Tell:

    def __init__(self, client, input):
        self.client = client
        self.id = input['id']
        self.tell = input['tell']
        self.created_at = input['createdAt']
        self.is_from_tellonym = input['isFromTellonym']
        self.is_welcome_tell = input['isWelcomeTell']
        self.is_seen = input['isSeen']
        self.sender_status = input['senderStatus']
        self.is_inappropriate = input['isInappropriate']
        self.sender = input['sender']

    def is_anonymous_tell(self):

        if self.sender_status == 2:
            return False
        return True
        
    def answer(self, input):
        """
        Answers to the recieved tell

        Args:
            input (str): answer string
        """

    def delete(self):
        """
        Deletes the received tell
        """
