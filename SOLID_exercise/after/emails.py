from abc import ABC, abstractmethod


class IContent(ABC):
    @abstractmethod
    def format(self):
        pass


class MyContent(IContent):
    def __init__(self, text: str):
        self.text = text

    def format(self):
        return f'<myML>\n{self.text}\n</myML>'


class IMSender:
    def __init__(self, sender: str):
        self._sender = sender

    def set_sender(self):
        return f"I'm {self._sender}"


class IMReceiver:
    def __init__(self, receiver: str):
        self._receiver = receiver

    def set_receiver(self):
        return f"I'm {self._receiver}"


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
        self._sender = None
        self._receiver = None
        self._content = None

    def set_sender(self, sender: IMSender):
        self._sender = sender.set_sender()

    def set_receiver(self, receiver: IMReceiver):
        self._receiver = receiver.set_receiver()

    def set_content(self, content: IContent):
        self._content = content.format()

    def __repr__(self):
        return f"Sender: {self._sender}\nReceiver: {self._receiver}\nContent:\n{self._content}"


# Example usage:
email = Email()
email.set_sender(IMSender('qmal'))
email.set_receiver(IMReceiver('james'))
content = MyContent('Hello, there!')
email.set_content(content)
print(email)