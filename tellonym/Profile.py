from tellonym.Answer import Answer
from tellonym.Config import Config
from tellonym.Link import Link
import tellonym.utils as utils


class Profile:

    def __init__(self, client, input):
        self.__client = client
        self.orig_input = input
        self.id = utils.get_json_attr(input, 'id')
        self.email = utils.get_json_attr(input, 'email')
        self.display_name = utils.get_json_attr(input, 'displayName')
        self.username = utils.get_json_attr(input, 'username')
        self.type = utils.get_json_attr(input, 'type')
        self.language = utils.get_json_attr(input, 'lang')
        self.location = utils.get_json_attr(input, 'location')
        self.page_id = utils.get_json_attr(input, 'pageId')
        self.twitter_username = utils.get_json_attr(input, 'twitterUsername')
        self.instagram_username = utils.get_json_attr(input, 'instagramUsername')
        self.is_email_notifications_enabled = utils.get_json_attr(input, 'isEmailNotificationsEnabled')
        self.email_polling_type = utils.get_json_attr(input, 'emailPollingType')
        self.creation_date = utils.get_json_attr(input, 'createdAt')
        self.is_safety_code_set = utils.get_json_attr(input, 'isSafetyCodeSet')
        self.twitter_id = utils.get_json_attr(input, 'twitterId')
        self.instagram_id = utils.get_json_attr(input, 'instagramId')
        self.theme = utils.get_json_attr(input, 'theme')
        self.about_me = utils.get_json_attr(input, 'aboutMe')
        self.avatar_file_name = utils.get_json_attr(input, 'avatarFileName')
        self.is_searchable = utils.get_json_attr(input, 'isSearchable')
        self.ad_free_until = utils.get_json_attr(input, 'adfreeUntil')
        self.last_active_at = utils.get_json_attr(input, 'lastActiveAt')
        self.likes_count = utils.get_json_attr(input, 'likesCount')
        self.follower_count = utils.get_json_attr(input, 'followerCount')
        self.anonymous_follower_count = utils.get_json_attr(input, 'anonymousFollowerCount')
        self.following_count = utils.get_json_attr(input, 'followingCount')
        self.tell_count = utils.get_json_attr(input, 'tellCount')
        self.answer_count = utils.get_json_attr(input, 'answerCount')
        self.is_verified = utils.get_json_attr(input, 'isVerified')
        self.push_notification_token = utils.get_json_attr(input, 'pushNotificationToken')
        self.is_push_notifications_enabled = utils.get_json_attr(input, 'isPushNotificationsEnabled')
        self.is_push_notifications_enabled_system = utils.get_json_attr(input, 'isPushNotificationsEnabledSystem')
        self.is_push_notifications_tell_enabled = utils.get_json_attr(input, 'isPushNotificationsTellEnabled')
        self.is_push_notifications_answer_enabled = utils.get_json_attr(input, 'isPushNotificationsAnswerEnabled')
        self.is_push_notifications_liked_enabled = utils.get_json_attr(input, 'isPushNotificationsLikedEnabled')
        self.is_push_notifications_anonymous_subscription_enabled = \
            utils.get_json_attr(input, 'isPushNotificationsAnonymousSubscriptionEnabled')
        self.is_push_notifications_public_subscription_enabled = \
            utils.get_json_attr(input, 'isPushNotificationsPublicSubscriptionEnabled')
        self.phone_prefix = utils.get_json_attr(input, 'phonePrefix')
        self.phone_suffix = utils.get_json_attr(input, 'phoneNumber')
        if self.phone_prefix is not None and self.phone_suffix is not None:
            self.phone_number = self.phone_prefix + self.phone_suffix
        self.is_tells_only_from_registered = utils.get_json_attr(input, 'isTellsOnlyFromRegistered')
        self.is_allowed_to_moderate = utils.get_json_attr(input, 'isAllowedToModerate')
        self.link_data = self.__get_link_data(utils.get_json_attr(input, 'linkData'))
        self.has_allowed_emails = utils.get_json_attr(input, 'hasAllowedEmails')
        self.hasAllowedSearchByPhone = utils.get_json_attr(input, 'hasAllowedSearchByPhone')
        self.hasAllowedShowActivity = utils.get_json_attr(input, 'hasAllowedShowActivity')
        self.is_under_16 = utils.get_json_attr(input, 'isUnder16')
        self.parental_email = utils.get_json_attr(input, 'parentalEmail')
        self.safety_level_sex_harass = utils.get_json_attr(input, 'safetyLevelSexHarass')
        self.safety_level_insult = utils.get_json_attr(input, 'safetyLevelInsult')
        self.safety_level_spam = utils.get_json_attr(input, 'safetyLevelSpam')
        self.has_password = utils.get_json_attr(input, 'hasPassword')
        self.is_twitter_connected = utils.get_json_attr(input, 'isTwitterConnected')
        self.is_precise_birthdate = utils.get_json_attr(input, 'isPreciseBirthdate')
        self.gender = utils.get_json_attr(input, 'gender')
        self.birthdate = utils.get_json_attr(input, 'birthdate')
        self.has_allowed_featuring = utils.get_json_attr(input, 'hasAllowedFeaturing')
        self.has_allowed_show_age = utils.get_json_attr(input, 'hasAllowedShowAge')
        self.has_allowed_search_by_location = utils.get_json_attr(input, 'hasAllowedSearchByLocation')
        self.city = utils.get_json_attr(input, 'city')
        self.country = utils.get_json_attr(input, 'country')
        self.answers = self.__get_answers(utils.get_json_attr(input, 'answers'))
        # self.config = Config(utils.get_json_attr(input, 'config'))

    def __get_link_data(self, input):
        """
        Gets the linked accounts from the current user

        Args:
            input (json str): link data input

        Returns:
            Link (class): linked data information
        """

        link_data = []
        for index, _ in enumerate(input):
            link = Link(input[index])
            link_data.append(link)

        return link_data

    def __get_answers(self, input):
        """
        Gets all answers on the current user's profile

        Args:
            input (json str): array of answers

        Returns:
            answers (arr): array of answer classes
        """
        answers = []
        for index, _ in enumerate(input):
            answer = Answer(self.__client, input[index])
            answers.append(answer)

        return answers

    def is_default_phonenumber(self):
        """
        Checks wether or not the phonenumber is default

        Returns:
            True: If phonenumber is default
            False: If phonenumber is not default
        """

        if self.phone_suffix == 12345678:
            return True
        return False

    def __str__(self):
        return "[{0}] Profile {1}".format(self.id, self.display_name)
