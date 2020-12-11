class User:

    def __init__(self, input):
        self.type = input['type']
        self.id = input['id']
        self.display_name = input['displayName']
        self.username = input['username']
        self.status_emoji = input['statusEmoji']
        self.about_me = input['aboutMe']
        self.avatar_file_name = input['avatarFileName']
        self.is_verified = input['isVerified']
        self.is_active = input['isActive']
        self.is_blocked = input['isBlocked']
        self.is_blocked_by = input['isBlockedBy']
        self.is_following = input['isFollowing']

    def get_profile_picture(self):
        return 'userimg.tellonym.me/xs/' + self.avatar_file_name

    def get_profile_thumbnail(self):
        return 'userimg.tellonym.me/thumb/' + self.avatar_file_name

    def __str__(self):
        return "[{0}] User {1}".format(self.id, self.display_name)
