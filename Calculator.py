from MessageFactory import MessageFactory


def addition(firstNum, secondNum, thirdNum):
    return firstNum + secondNum + thirdNum


def subtraction(firstNum, secondNum, thirdNum):
    return firstNum - secondNum - thirdNum


def multiplication(firstNum, secondNum, thirdNum):
    return firstNum * secondNum * thirdNum


def division(firstNum, secondNum, thirdNum):
    return firstNum / secondNum / thirdNum


def lang(language):
    if language.__eq__("EN"):
        return MessageFactory("En ter first number: ", "Enter operation: ", "Enter second number: ", "Enter second "
                                                                                                     "operation: ",
                              "Enter third number: ", "Invalid command",
                              "Enter 'yes' if you want to continue or enter 'no' to close the calculator: ", "yes",
                              "no")
        if language.__eq__("UA"):
            return MessageFactory("Введіть перше число: ", "Введіть операцію: ", "Введіть друге число: ", "Введіть  "
                                                                                                          "другу "
                                                                                                          "операцію: "
                                                                                                          "",
                                  "Введіть третє число: ",
                                  "Неправильна команда",
                                  "Введіть 'так', якщо ви хочете продовжити 'ні', якщо хочете закрити калькулятор: ",
                                  "так",
                                  "ні")
        if language.__eq__("RU"):
            return MessageFactory("Введите первое число: ", "Введите операцию: ", "Введите второе число: ", "Введите "
                                                                                                            "вторую "
                                                                                                            "операцию: ",
                                  "Введите третье число: ",
                                  "Неправильная команда",
                                  "Введите 'да', если хотите продолжить 'нет', если хотите закрыть калькулятор: ", "да",
                                  "нет")


def getResult(operation, firstNum, secondNum, thirdNum):
    if operation.__eq__("+"):
        return addition(firstNum, secondNum, thirdNum)
    elif operation.__eq__("-"):
        return subtraction(firstNum, secondNum, thirdNum)
    elif operation.__eq__("*"):
        return multiplication(firstNum, secondNum, thirdNum)
    elif operation.__eq__("/"):
        return division(firstNum, secondNum, thirdNum)


if __name__ == '__main__':
    language = str(input("Choose language 'UA' 'RU' 'EN': "))
    message = lang(language)
    contNum = message.yes_
    while contNum == message.yes_:
        firstNum = int(input(message.number_))
        operation = str(input(message.operation_))
        secondNum = int(input(message.second_number_))
        additional = str(input(message.additional_))
        thirdNum = int(input(message.second_number_))
        result = getResult(operation, firstNum, secondNum, thirdNum)
    print(result)
    contNum = str(input(message.calculator_))
    while contNum != message.yes_ and contNum != message.no_:
        print(message.command_)
        contNum = str(input(message.calculator_))
