class Loja:
    def getExample01(self):
        example = [
            ['username', 'ip', 'password_index']
        ]

        return example
    
    def getExample02(self):
        example = [
            ['username', 'ip', 'password_index']
        ]

        return example

    def getAllExamples(self):
        examples = [
            ['1', self.getExample01()],
            ['2', self.getExample02()]
        ]

        return examples
