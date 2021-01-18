class MessageFactory:
    number_ = ""
    operation_ = ""
    second_number_ = ""
    additional_ = ""
    third_number_ = ""
    calculator_ = ""
    command_ = ""
    total_ = ""
    yes_ = ""
    no_ = ""

    def __init__(self, number_, operation_, second_number_, additional_, third_number_, command_, calculator_, yes_,
                 no_):
        self.number_ = number_
        self.operation_ = operation_
        self.second_number_ = second_number_
        self.additional_ = additional_
        self.third_number_ = third_number_
        self.calculator_ = calculator_
        self.command_ = command_
        self.yes_ = yes_
        self.no_ = no_
