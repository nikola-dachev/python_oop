from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MyMl(IContent):
    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class HTML(IContent):
    def format(self):
        return '\n'.join(['<HTML>', self.text, '</HTML>'])

class IProtocol(ABC):
    def __init__(self,sender_receiver):
        self.sender_receiver = sender_receiver

    @abstractmethod
    def format(self):
        pass

class ImProtocol(IProtocol):
    def format(self):
        return ''.join(["I'm ", self.sender_receiver])


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self):

        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = sender.format()

    def set_receiver(self, receiver):
        self.__receiver = receiver.format()

    def set_content(self, content):
        self.__content = content.format()

    def __repr__(self):

        template = f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"

        return template


html = HTML('Hello, there!')
email = Email()
email.set_sender('qmal')
email.set_receiver('james')
email.set_content(html)
print(email)

