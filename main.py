from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

ltext = '''Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего
здоровья.

Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности
сердца при физической нагрузке.

У испытуемого определяют частоту пульса за 15 секунд.

Затем в течение 45 секунд испытуемый выполняет 30 приседаний.

После окончания нагрузки пульс подсчитывается вновь: число пульсаций за первые 15 секунд, 30 секунд
отдыха, число пульсаций за последние 15 секунд.
'''

pulse = '''Замерьте пульс за 15 секунд.
Результат запишите в соответствующее поле.'''

prised = '''Выполните 30 приседаний за 45 секунд.'''

pulse2 = '''В течение минуты замерьте пульс два раза:
за первые 15 секунд минуты, затем за последние 15 секунд.
Резаультаты запишите в соответствующие поля.'''

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
        mainlay1 = BoxLayout(orientation='vertical')
        mainlay2 = BoxLayout(size_hint=(.5, .5))
        mainlay3 = BoxLayout(size_hint=(.5, .5))
        ins = Label(text=ltext, pos_hint={'center_y':0.1})
        inpname = Label(text='Введите имя:')
        inpage = Label(text='Введите возраст:')
        ti1 = TextInput(multiline=False, height='30sp', size_hint_y=None, size_hint=(.6, None), pos_hint={'center_y':0.5})
        ti2 = TextInput(multiline=False, height='30sp', size_hint_y=None, size_hint=(.6, None), pos_hint={'center_y':0.5})

        btn1 = Button(text="Начать", size_hint_y=None, height='100sp', size_hint=(.3, None), pos_hint={'center_x':0.5})
        btn1.on_press = self.next1

        mainlay1.add_widget(ins)

        mainlay2.add_widget(inpname)
        mainlay2.add_widget(ti1)
        mainlay1.add_widget(mainlay2)

        mainlay3.add_widget(inpage)
        mainlay3.add_widget(ti2)
        mainlay1.add_widget(mainlay3)

        mainlay1.add_widget(btn1)
        self.add_widget(mainlay1)

    def next1(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'AScr'

class AScr(Screen):
    def __init__(self, name='AScr'):
        super().__init__(name=name)
        ascrlay1 = BoxLayout(orientation='vertical')
        ascrlay2 = BoxLayout(size_hint=(.5, .5))
        pulseins = Label(text=pulse)
        result = Label(text='Введите результат:')
        ti1 = TextInput(multiline=False, height='30sp', size_hint_y=None, size_hint=(.6, None), pos_hint={'center_y':0.5})

        btn1 = Button(text="Продолжить1", size_hint_y=None, height='100sp', size_hint=(.3, None), pos_hint={'center_x':0.5})
        btn1.on_press = self.next1

        ascrlay1.add_widget(pulseins)

        ascrlay2.add_widget(result)
        ascrlay2.add_widget(ti1)
        ascrlay1.add_widget(ascrlay2)

        ascrlay1.add_widget(btn1)
        self.add_widget(ascrlay1)

    def next1(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'AAScr'

class AAScr(Screen):
    def __init__(self, name='AAScr'):
        super().__init__(name=name)
        aascrlay1 = BoxLayout(orientation='vertical')
        aascrlay2 = BoxLayout()
        prisedins = Label(text=prised)

        btn2 = Button(text="Продолжить2", size_hint_y=None, height='100sp', size_hint=(.3, None), pos_hint={'center_x':0.5})
        btn2.on_press = self.next2

        aascrlay1.add_widget(prisedins)
        
        aascrlay1.add_widget(btn2)
        self.add_widget(aascrlay1)

    def next2(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'AAAScr'

class AAAScr(Screen):
    def __init__(self, name='AAAScr'):
        super().__init__(name=name)
        aaascrlay1 = BoxLayout(orientation='vertical')
        aaascrlay2 = BoxLayout(size_hint=(.5, .5))
        aaascrlay3 = BoxLayout(size_hint=(.5, .5))
        pulse2ins = Label(text=pulse2)
        result1 = Label(text='Результат:')
        result2 = Label(text='Результат после отдыха:')
        ti1 = TextInput(multiline=False, height='30sp', size_hint_y=None, size_hint=(.6, None), pos_hint={'center_y':0.5})
        ti2 = TextInput(multiline=False, height='30sp', size_hint_y=None, size_hint=(.6, None), pos_hint={'center_y':0.5})

        btn3 = Button(text="Завершить", size_hint_y=None, height='100sp', size_hint=(.3, None), pos_hint={'center_x':0.5})
        btn3.on_press = self.next3

        aaascrlay1.add_widget(pulse2ins)

        aaascrlay2.add_widget(result1)
        aaascrlay2.add_widget(ti1)
        aaascrlay1.add_widget(aaascrlay2)

        aaascrlay3.add_widget(result2)
        aaascrlay3.add_widget(ti2)
        aaascrlay1.add_widget(aaascrlay3)

        aaascrlay1.add_widget(btn3)
        self.add_widget(aaascrlay1)

    def next3(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'AAAAScr'

class AAAAScr(Screen):
    def __init__(self, name='AAAAScr'):
        super().__init__(name=name)
        super().__init__(name=name)
        lab1 = Label(text="инпуты", size_hint=(.2, .2))
        self.add_widget(lab1)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(AScr())
        sm.add_widget(AAScr())
        sm.add_widget(AAAScr())
        sm.add_widget(AAAAScr())
        return sm

app = MyApp()
app.run()