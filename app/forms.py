from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from app.models import User


class LoginForm(FlaskForm):
    username = StringField("用户名", validators=[DataRequired()])
    password = StringField("密码", validators=[DataRequired()])
    rememberme = BooleanField("自动登录")
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField("密码", validators=[DataRequired()])
    password2 = PasswordField('重复密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('点我注册')

    def validate_username(self, username):
        got_user = User.query.filter_by(username=username.data).first()
        if got_user is not None:
            raise ValidationError("此用户名已被使用!")

    def validate_email(self, email):
        got_email = User.query.filter_by(email=email.data).first()
        if got_email is not None:
            raise ValidationError("此邮箱已被其他用户使用!")


class EditProfileForm(FlaskForm):
    username = StringField("用户名", validators=[DataRequired()])
    about_me = TextAreaField('个性签名', validators=[Length(min=0, max=140)])
    submit = SubmitField('提交')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('该用户名已被使用 , 请使用一个不同的用户名!')


class PostForm(FlaskForm):
    body = TextAreaField('说点什么吧...', validators=[DataRequired(), Length(min=1, max=65535)])

    title = StringField('标题', validators=[DataRequired(), Length(min=1, max=256)])

    submit = SubmitField('发布')
