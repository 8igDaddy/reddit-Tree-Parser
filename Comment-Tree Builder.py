import praw
import os
import time



def unwrapTree(comments, tree, level):
    for comment in comments:
        if level in temp:
            temp[level].append(comment.body)
        else:
            temp[level] = [comment.body]
        unwrapTree(comment.replies, tree, level + 1)


def formSequences(comments, sequence, out):
    global totalSequences
    flag = True
    
    for comment in comments:
        flag = False
        temp = sequence
        temp = temp + '\n' + comment.body
        formSequences(comment.replies, temp, out)
    if flag is True:
        out.write((sequence + '\n').encode('utf-8'))
        totalSequences = totalSequences + 1
        #print 'Sequence is: ', sequence.encode('utf-8')
        print "Number of Sequences: ", totalSequences



if not os.path.exists("Data/reddit"):
    os.makedirs("Data/reddit")
output = open("Data/reddit/Input.txt", "w")

## Use for specific submission.
#submission = r.get_submission(url = 'https://www.reddit.com/r/greece/comments/3gfnws/%CE%B5%CE%B2%CE%B4%CE%BF%CE%BC%CE%B1%CE%B4%CE%B9%CE%B1%CE%AF%CE%B1_%CF%83%CF%85%CE%B6%CE%AE%CF%84%CE%B7%CF%83%CE%B7_%CF%84%CE%BF%CF%85_rgreece_weekly_rgreece/')
#submission = r.get_submission(submission_id = '3i3tk4')
#submission.replace_more_comments(limit = None, threshold = 0)
#formSequences(submission.comments, submission.title + '\n' + submission.selftext, output)

r = praw.Reddit(user_agent='example')
subreddit = r.get_subreddit('worldnews')

## Use with the unwrapTree() function.
#temp = {}

totalSequences = 0
for s in subreddit.get_top_from_month(limit = 30):
    s.replace_more_comments(limit = 500, threshold = 0)
    formSequences(s.comments, s.title + '\n' + s.selftext, output)




output.close()

