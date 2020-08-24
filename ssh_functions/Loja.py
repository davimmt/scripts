class Loja:
    def getLoja01POS(self):
        POS = [
            ['caixa01', '101.101', 4],
            ['caixa02', '101.102', 4],
            ['caixa03', '101.103', 4],
            ['caixa04', '101.104', 4],
            ['caixa05', '101.105', 4],
            ['caixa06', '101.106', 4],
            ['caixa07', '101.107', 4],
            ['caixa08', '101.108', 4],
            ['caixa09', '101.109', 4],
            ['caixa10', '101.110', 4],
            ['caixa11', '101.111', 4],
            ['caixa12', '101.112', 4],
            ['caixa13', '101.113', 4]
        ]

        return POS
    
    def getLoja02POS(self):
        POS = [
            ['caixa01', '102.101', 4],
            ['caixa02', '102.17', 4],
            ['caixa03', '102.109', 4],
            ['caixa04', '102.11', 4],
            ['caixa05', '102.19', 4],
            ['caixa06', '102.106', 4],
            ['caixa07', '102.13', 4],
            ['caixa08', '102.25', 4],
            ['caixa09', '102.22', 4],
            ['caixa10', '102.18', 4],
            ['caixa11', '102.111', 4],
            ['caixa12', '102.112', 4]
        ]

        return POS

    def getLoja03POS(self):
        POS = [
            ['caixa01', '103.101', 4],
            ['caixa_02', '103.102', 4],
            ['caixa03', '103.103', 4],
            ['caixa04', '103.104', 4],
            ['caixa05', '103.105', 4],
            ['caixa06', '103.106', 4],
            ['caixa07', '103.107', 4],
            ['caixa08', '103.108', 4],
            ['caixa09', '103.109', 4],
            ['caixa10', '103.110', 4]
        ]

        return POS

    def getLoja04POS(self):
        POS = [
            ['caoxa01', '104.101', 0], ##
            ['caixa02', '104.102', 4],
            ['caixa03', '104.103', 4],
            ['caixa04', '104.104', 4],
            ['caixa05', '104.105', 4]
        ]

        return POS

    def getLoja05POS(self):
        POS = [
            ['caixa01', '105.101', 4],
            ['caixa02', '105.102', 4],
            ['caixa03', '105.103', 4],
            ['caixa04', '105.104', 4],
            ['caixa05', '105.105', 4]
        ]

        return POS

    def getLoja06POS(self):
        POS = [
            ['caixa01', '106.101', 4],
            ['caixa02', '106.102', 4],
            ['caixa03', '106.103', 4],
            ['caixa04', '106.104', 4],
            ['caixa05', '106.105', 4],
            ['caixa06', '106.106', 4],
            ['caixa07', '106.107', 4],
            ['caixa08', '106.108', 4],
            ['caixa09', '106.109', 4],
            ['caixa10', '106.110', 4],
            ['caixa11', '106.111', 4],
            ['caixa12', '106.112', 4],
            ['caixa13', '106.113', 4],
            ['caixa14', '106.114', 4],
            ['caixa15', '106.115', 4]
        ]

        return POS

    def getAllPOS(self):
        POS = [
            ['1', self.getLoja01POS()],
            ['2', self.getLoja02POS()],
            ['3', self.getLoja03POS()],
            ['4', self.getLoja04POS()],
            ['5', self.getLoja05POS()],
            ['6', self.getLoja06POS()]
        ]

        return POS