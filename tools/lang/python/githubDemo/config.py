# change array to var???? why using array...
THOUGHTS_LABEL_LIST = [
    "Thoughts",
]
OLD_LABEL_LIST = [
    "Old",
]
BANGUMI_LABEL_LIST = [
    "Bangumi",
]
CONSUME_LABEL_LIST = [
    "Consume",
]
BOOK_LABEL_LIST = [
    "Book",
]
MOVIE_LABEL_LIST = [
    "Movie",
]
PODCAST_LABEL_LIST = [
    "POSTCAST",
]
GAME_LABEL_LIST = [
    "Game",
]
GAME_LABEL_LIST = [
    "Mark",
]

# add new label here
LABEL_DICT = {
    "Thought": {"label_list": THOUGHTS_LABEL_LIST, "comment_name": "my_thought"}
    # "Cook": {"label_list": COOK_LABEL_LIST, "comment_name": "my_cook"},
    # "Movie": {"label_list": MOVIE_LABEL_LIST, "comment_name": "my_movie"},
    # "Read": {"label_list": READ_LABEL_LIST, "comment_name": "my_read"},
    # "Drama": {"label_list": DRAMA_LABEL_LIST, "comment_name": "my_drama"},
    # "Bangumi": {"label_list": BANGUMI_LABEL_LIST, "comment_name": "my_bangumi"},
    # "Game": {"label_list": GAME_LABEL_LIST, "comment_name": "my_game"},
}



# MY_BLOG_REPO = ""

GITHUB_README_COMMENTS = (
    "(<!--START_SECTION:{name}-->\n)(.*)(<!--END_SECTION:{name}-->\n)"
)


##### BASE COMMENT TABLE ######
BASE_ISSUE_STAT_HEAD = "| Name | Start | Update | \n | ---- | ---- | ---- | \n"
BASE_ISSUE_STAT_TEMPLATE = "| {name} | {start} | {update} | \n"

##### BLOG COMMENT ######
BLOG_ISSUE_STAT_HEAD = (
    "| Name | Start | Update | Comments | \n | ---- | ---- | ---- | ---- |\n"
)
BLOG_ISSUE_STAT_TEMPLATE = "| {name} | {start} | {update} | {comments} | \n"




##### Month Summary ######
MONTH_SUMMARY_HEAD = "| Month | Number | \n | ---- | ---- | \n"

MONTH_SUMMARY_STAT_TEMPLATE = "| {month} | {number} |\n"


# +-----------------+
# | General Showing |
# +-----------------+
IssueTableHead = "\
## Issues I Created In 2021\n\
\n\
| Name | Update At | Url |\n\
| ---- | ---- | ---- |\n"

IssueTableTemplate = "\
| {issueName} | {issueUpdate} | {issueUrl} |\n"

