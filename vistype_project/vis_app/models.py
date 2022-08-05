from os import major
from django.db import models

# Create your models here.

class User_info(models.Model):    
    user_id = models.CharField(verbose_name='사용자', max_length=256, primary_key=True)
    sex = models.CharField(max_length=256, verbose_name='성별')
    age = models.CharField(max_length=256, verbose_name='나이')
    major = models.CharField(max_length=256, verbose_name='전공')
    education = models.CharField(max_length=256, verbose_name='최종학력')

    def __str__(self):
        return str(self.user_id) + ' - ' + str(self.major)

    class Meta:
        db_table = 'User_info'
        verbose_name = '사용자 정보'
        verbose_name_plural = '사용자 정보' 

class Vis_test(models.Model):
    test_id = models.SmallIntegerField(verbose_name='test_id', primary_key=True)
    v_number = models.SmallIntegerField(verbose_name='문제번호')
    v_title =models.CharField(max_length=256, verbose_name='시각화제목')
    v_type = models.CharField(max_length=256, verbose_name='시각화종류')
    v_task = models.CharField(max_length=256, verbose_name='task')
    title = models.CharField(max_length=256, verbose_name='문제제목')
    examples_1 = models.CharField(max_length=64, verbose_name='보기1')
    examples_2 = models.CharField(max_length=64, verbose_name='보기2')
    examples_3 = models.CharField(
        max_length=64, null=True, blank=True, verbose_name='보기3')
    examples_4 = models.CharField(
        max_length=64, null=True, blank=True, verbose_name='보기4')
    correct = models.CharField(max_length=64, verbose_name='정답')

    def __str__(self):
        return  str(self.test_id) + ' - ' + str(self.v_type) + ' / ' + str(self.title)

    class Meta:
        db_table = 'Vis_Test'
        verbose_name = '시각화 테스트'
        verbose_name_plural = '시각화 테스트'

class Answer(models.Model):
    answer_id = models.CharField(verbose_name='answer_id', primary_key=True, max_length=256)
    user_id = models.CharField(verbose_name='사용자', max_length=256)
    test_id = models.SmallIntegerField(verbose_name='test_id')
    v_type = models.CharField(max_length=256, verbose_name='시각화종류')
    v_task = models.CharField(max_length=256, verbose_name='task')
    answer = models.CharField(max_length=64, verbose_name='답안')
    status = models.BooleanField(verbose_name='정답여부')
    time = models.CharField(max_length=64, verbose_name='소요시간')

    def __str__(self):
        return str(self.user_id) + ' - '+ str(self.test_id) + ' - ' + str(self.v_type) + '/' + str(self.status)

    class Meta:
        db_table = 'Vis_Answer'
        verbose_name = '답안'
        verbose_name_plural = '답안'

class Vis_Choice_Test(models.Model):
    vis_id = models.SmallIntegerField(verbose_name='vis_id', primary_key=True)
    set_number = models.CharField(max_length=256, verbose_name='set_number')
    vis_title = models.CharField(max_length=256, verbose_name='시각화제목')
    v_task = models.CharField(max_length=256, verbose_name='task')
    v_question = models.CharField(max_length=256, verbose_name='질문')
    vis_1 = models.CharField(max_length=64, verbose_name='보기1')
    vis_2 = models.CharField(max_length=64, verbose_name='보기2')

    def __str__(self):
        return str(self.vis_id) + ' - ' + str(self.set_number) + ' - ' + str(self.vis_title) + ' - ' + str(self.v_task)

    class Meta:
        db_table = 'Vis_Choice_Test'
        verbose_name = '선택지'
        verbose_name_plural = '선택지'

class Choice(models.Model):
    choice_id = models.CharField(verbose_name='choice_id', primary_key=True, max_length=256)      
    user_id = models.CharField(verbose_name='사용자', max_length=256)
    set_number = models.CharField(max_length=256, verbose_name='set_number')
    choice_type = models.CharField(max_length=256, verbose_name='선호 시각화')
    v_task = models.CharField(max_length=256, verbose_name='task')
    v_reason = models.CharField(max_length=256, verbose_name='선택이유')
    time = models.CharField(max_length=64, verbose_name='소요시간')

    def __str__(self):
        return str(self.user_id) + ' - ' + str(self.set_number) + ' - ' + str(self.choice_type)

    class Meta:
        db_table = 'Vis_Choice_Result'
        verbose_name = '선택 결과'
        verbose_name_plural = '선택 결과'

class Vis_prefer(models.Model):
    prefer_id = models.SmallIntegerField(verbose_name='prefer_id', primary_key=True)      
    user_id = models.CharField(verbose_name='사용자', max_length=256)
    vis_type = models.CharField(max_length=256, verbose_name='시각화 종류')
    v_task = models.CharField(max_length=256, verbose_name='task')
    prefer = models.IntegerField(verbose_name='정답 선호도')

    def __str__(self):
        return str(self.user_id) + ' - ' + str(self.vis_type) + ' - ' + str(self.v_task)

    class Meta:
        db_table = 'Vis_prefer'
        verbose_name = '정답 선호도 결과'
        verbose_name_plural = '정답 선호도 결과'    