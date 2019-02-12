import unittest
from app.models import Comment,User
from app import db

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_pakawa = User(username = 'pakawa',password = 'potato')
        self.new_comment = Comment(description='comments',user = self.user_pakawa)

    # def tearDown(self):
    #         Review.query.delete()
    #         User.query.delete()

    def test_check_instance_variables(self):
        self.assertTrue(self.new_comment, Comment)

        # self.assertEquals(self.new_comment.user,self.user_pakawa)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(1234)
        self.assertTrue(len(got_comments) > 0)
