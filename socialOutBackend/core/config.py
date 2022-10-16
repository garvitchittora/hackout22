BASE_URL = "https://localhost:8001/api/v1/"


# GET Experience or Product
GET_EXPERIENCE = "experience"
# PARAMS:
# city: could be null
# start_date: could be null (Format: YYYY/MM/DD)
# end_date: could be null (Format: YYYY/MM/DD)


# Interest of experience
GET_INTEREST = "get-interest"
# PARAMS:
# user_id: user id of user whose interest we need to get

POST_INTEREST = "interest"
# PARAMS:
# user_id: user id of user who is interest
# experience_id: experience id in which he is interested


# User GET and POST routes
GET_USER = 'get-user'
# PARAMS:
# user_id: user id of user (Optional)
# email: email of user (Optional)
# prefix: prefix of user name (Optional)

POST_USER = 'user'
# PARAMS:
# email: email of user (Optional)
# name: name of user (Optional)
# image: image of user (Optional)


# ADD or REMOVE Follower Route
USER_ADD_FOLLOW = 'useraddfollow'
# PARAMS:
# user_id: user id of user
# following_id: following id of user we need to follow


USER_REMOVE_FOLLOW = 'userremfollow'
# PARAMS:
# user_id: user id of user
# following_id: following id of user we need to unfollow


# Add comment to Product or experience
GET_COMMENT = 'get-comment'
# PARAMS:
# experience_id: id of product or experience

POST_COMMENT = 'comment'
# PARAMS:
# user_id: user id of user
# experience_id: experience id of user
# comment_text: text of comment


# GET Stories
USER_WITH_STORIES = 'userwithstories'
# user_id: user id of user whose storied we need to get


ANALYTICS = {
    'comment/': 'commented',
    'interest/': 'interested',
    'experience/': 'viewed',
}