#Question ile Quiz yapıcaz soruları cevaplandıracağız.

class Question:
    def __init__(self,text,choices,answer):
        self.text = text#Question classı içinde bir metin yolliyacağız
        self.choices = choices #Question classı içinde bir seçim göndericez
        self.answer =answer ##Question classı içindeki soruları göndericez


    def checkAnswer(self, answer):#değerlendirme olsun diye bir fonksiyon koydum ve bu fonksiyona
       return self.answer == answer#girilen cevabı burdaki cevap parametresi ile aynı mı dır diye geri yolladım.



#Quiz
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex=0

    def getQuestion(self):#soru indexi sürekli 0 olduğundan yani 1. soruya tekabül edeceğinden
        return self.questions[self.questionIndex]#getquestion diye bir fonksiyon oluşturdum ve soru indekini buna atadım.



    def displayQuestion(self):#bunu ekrana yazdırmalık metot atadım.
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}:{question.text}')#

        for q in question.choices:#soruları ekrana getiriyor.
            print('-'+ q)

        answer = input('cevap: ')#cevap girdisi alıyor.
        print(question.checkAnswer(answer))#girilen cevabı,kontrol cevabına yazdırıyor.
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):#girilşen cevabı kontrol ediyor
        question=self.getQuestion()

        if question.checkAnswer(answer):#eğer checkAnswer answerla doğru ise score 1 arttırılıyor.
            self.score +=1
        self.questionIndex  +=1#soruyuda 1 arttır.

        self.displayQuestion()

    def loadQuestion(self):#Bize bir soru yüklesin
        if len(self.questions) ==self.questionsIndex:  #gönderilen soru sayısı eşitse
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()



    def showScore(self):
        print('score: ',self.score)
    def displayProgress(self):
        totalQuestion =len(self.questions)
        questionNumber = self.questionsIndex +1

        if questionNumber > totalQuestion:
             print('Quiz bitti')
        else:
            print()

q1 =Question('en iyi programlama dili hangisidir?',['c#','java','python'],'python')
q2 =Question('en iyi popüler dil hangisidir?',['java','c#','python'],'python')
q3 =Question('en çok kazandıran dil hangisidir?',['c#','python','java'],'python')
questions =[q1,q2,q3]

quiz =Quiz(questions)
question =quiz.getQuestion()
print(question)
quiz.displayQuestion()